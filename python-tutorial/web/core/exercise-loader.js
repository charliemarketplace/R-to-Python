// Exercise loader - fetches and parses exercise files

const exerciseCache = new Map();

/**
 * Parse a Python exercise file into structured data.
 */
function parseExerciseFile(content, moduleId, exerciseNum) {
  // Extract docstring
  const docstringMatch = content.match(/^"""([\s\S]*?)"""/);
  const docstring = docstringMatch ? docstringMatch[1].trim() : '';

  // Extract title from docstring
  const titleMatch = docstring.match(/EXERCISE \d+:\s*(.+)/);
  const title = titleMatch ? titleMatch[1].trim() : `Exercise ${exerciseNum}`;

  // Split by markers
  const userStartMarker = '# ---- YOUR CODE HERE ----';
  const userEndMarker = '# ---- END YOUR CODE ----';
  const gradingMarker = '# ---- GRADING';

  const startIdx = content.indexOf(userStartMarker);
  const endIdx = content.indexOf(userEndMarker);
  const gradingIdx = content.indexOf(gradingMarker);

  let setupCode = '';
  let starterCode = '';
  let gradingCode = '';

  if (startIdx !== -1 && endIdx !== -1) {
    // Find end of docstring
    const docEnd = content.indexOf('"""', 3) + 3;
    setupCode = content.substring(docEnd, startIdx).trim();
    starterCode = content.substring(startIdx + userStartMarker.length, endIdx).trim();

    if (gradingIdx !== -1) {
      gradingCode = content.substring(gradingIdx);
    }
  }

  // Parse checks from grading code
  const checks = parseGradingChecks(gradingCode);

  // Extract hint from check calls
  const hintMatch = gradingCode.match(/hint=['"](.*?)['"]/);
  const hint = hintMatch ? hintMatch[1] : null;

  return {
    moduleId,
    exerciseNum,
    title,
    docstring,
    setupCode,
    starterCode,
    checks,
    hint,
  };
}

/**
 * Parse grading code to extract check assertions.
 */
function parseGradingChecks(gradingCode) {
  const checks = [];

  // Match check() calls - extract variable being checked and expected value
  const checkPattern = /check\s*\(\s*([^,]+),\s*expected\s*=\s*([^,)]+)/g;
  let match;

  while ((match = checkPattern.exec(gradingCode)) !== null) {
    const varName = match[1].trim();
    const expected = match[2].trim();

    checks.push({
      description: `Check ${varName}`,
      assertion: `
import numpy as np
_got = ${varName}
_expected = ${expected}

# Handle numpy arrays
if isinstance(_expected, np.ndarray):
    assert isinstance(_got, np.ndarray), f"Expected numpy array, got {type(_got).__name__}"
    np.testing.assert_allclose(_got, _expected, rtol=1e-6)
# Handle floats
elif isinstance(_expected, float):
    assert abs(_got - _expected) < 1e-6, f"Expected {_expected}, got {_got}"
# Handle lists with floats
elif isinstance(_expected, list) and len(_expected) > 0 and isinstance(_expected[0], float):
    for i, (g, e) in enumerate(zip(_got, _expected)):
        assert abs(g - e) < 1e-6, f"Element {i}: expected {e}, got {g}"
# Default comparison
else:
    assert _got == _expected, f"Expected {_expected!r}, got {_got!r}"
`,
    });
  }

  // Match check_model() calls
  const modelPattern = /check_model\s*\(\s*([^,]+),\s*['"](.*?)['"],\s*expected\s*=\s*([^,)]+)/g;
  while ((match = modelPattern.exec(gradingCode)) !== null) {
    const modelVar = match[1].trim();
    const param = match[2];
    const expected = match[3].trim();

    checks.push({
      description: `Check model coefficient '${param}'`,
      assertion: `
_model = ${modelVar}
assert hasattr(_model, 'params'), "Not a statsmodels result object"
assert '${param}' in _model.params, f"Parameter '${param}' not found"
_actual = _model.params['${param}']
_expected = ${expected}
assert abs(_actual - _expected) / abs(_expected) < 0.1, f"Coefficient '${param}': expected ~{_expected:.4f}, got {_actual:.4f}"
`,
    });
  }

  // Match check_plot() calls
  const plotPattern = /check_plot\s*\(\s*([^,]+),\s*['"](.*?)['"]/g;
  while ((match = plotPattern.exec(gradingCode)) !== null) {
    const figVar = match[1].trim();
    const plotType = match[2];

    checks.push({
      description: `Check plot type is '${plotType}'`,
      assertion: `
_fig = ${figVar}
assert _fig is not None, "Figure not created"
assert hasattr(_fig, 'data'), "Not a valid plotly figure"
assert len(_fig.data) > 0, "Figure has no data"
_types = [t.type for t in _fig.data]
assert '${plotType}' in [t.lower() for t in _types], f"Expected '${plotType}' trace, found: {_types}"
`,
    });
  }

  // If no checks found, create a basic one
  if (checks.length === 0) {
    checks.push({
      description: 'Basic check',
      assertion: 'assert True  # No specific checks defined',
    });
  }

  return checks;
}

/**
 * Fetch an exercise from the exercises directory.
 */
export async function loadExercise(moduleId, exerciseNum) {
  const cacheKey = `${moduleId}/${exerciseNum}`;

  if (exerciseCache.has(cacheKey)) {
    return exerciseCache.get(cacheKey);
  }

  // Format exercise number with leading zero
  const exNum = String(exerciseNum).padStart(2, '0');

  // Fetch the exercise file
  const basePath = window.EXERCISES_BASE_PATH || '../exercises';
  const url = `${basePath}/${moduleId}/ex${exNum}_*.py`;

  // We need to discover the full filename - fetch the directory listing or use a manifest
  // For now, we'll try common patterns
  const exercise = await fetchExerciseFile(moduleId, exerciseNum);

  if (exercise) {
    exerciseCache.set(cacheKey, exercise);
  }

  return exercise;
}

/**
 * Fetch exercise file trying different name patterns.
 */
async function fetchExerciseFile(moduleId, exerciseNum) {
  const exNum = String(exerciseNum).padStart(2, '0');
  const basePath = window.EXERCISES_BASE_PATH || '../exercises';

  // Try to fetch using the manifest
  try {
    const manifestResponse = await fetch(`${basePath}/manifest.json`);
    if (manifestResponse.ok) {
      const manifest = await manifestResponse.json();
      const moduleExercises = manifest[moduleId];
      if (moduleExercises && moduleExercises[exerciseNum]) {
        const filename = moduleExercises[exerciseNum];
        const response = await fetch(`${basePath}/${moduleId}/${filename}`);
        if (response.ok) {
          const content = await response.text();
          return parseExerciseFile(content, moduleId, exerciseNum);
        }
      }
    }
  } catch (e) {
    // Manifest not available, continue with direct fetch
  }

  // Try fetching with known exercise names from embedded data
  const exerciseNames = getExerciseNames();
  const key = `${moduleId}/${exerciseNum}`;

  if (exerciseNames[key]) {
    try {
      const response = await fetch(`${basePath}/${moduleId}/${exerciseNames[key]}`);
      if (response.ok) {
        const content = await response.text();
        return parseExerciseFile(content, moduleId, exerciseNum);
      }
    } catch (e) {
      console.error(`Failed to load exercise ${key}:`, e);
    }
  }

  return null;
}

/**
 * Get exercise file names - this would ideally be generated at build time.
 */
function getExerciseNames() {
  return {
    '01_fundamentals/1': 'ex01_indexing.py',
    '01_fundamentals/2': 'ex02_negative_indexing.py',
    '01_fundamentals/3': 'ex03_slicing_basics.py',
    '01_fundamentals/4': 'ex04_slice_step.py',
    '01_fundamentals/5': 'ex05_reference_vs_copy.py',
    '01_fundamentals/6': 'ex06_truthiness.py',
    '01_fundamentals/7': 'ex07_fstrings.py',
    '01_fundamentals/8': 'ex08_mutable_default.py',
    '02_control_flow/1': 'ex01_for_loops.py',
    '02_control_flow/2': 'ex02_range.py',
    '02_control_flow/3': 'ex03_enumerate.py',
    '02_control_flow/4': 'ex04_zip.py',
    '02_control_flow/5': 'ex05_while_loops.py',
    '02_control_flow/6': 'ex06_list_comprehension.py',
    '02_control_flow/7': 'ex07_dict_comprehension.py',
    '02_control_flow/8': 'ex08_conditional_expression.py',
    '02_control_flow/9': 'ex09_try_except.py',
    '02_control_flow/10': 'ex10_closure_trap.py',
    '03_functions/1': 'ex01_basic_functions.py',
    '03_functions/2': 'ex02_keyword_args.py',
    '03_functions/3': 'ex03_default_args.py',
    '03_functions/4': 'ex04_multiple_returns.py',
    '03_functions/5': 'ex05_args.py',
    '03_functions/6': 'ex06_kwargs.py',
    '03_functions/7': 'ex07_scope.py',
    '03_functions/8': 'ex08_lambda.py',
    '04_data_structures/1': 'ex01_lists.py',
    '04_data_structures/2': 'ex02_tuples.py',
    '04_data_structures/3': 'ex03_dicts_basics.py',
    '04_data_structures/4': 'ex04_dict_methods.py',
    '04_data_structures/5': 'ex05_sets.py',
    '04_data_structures/6': 'ex06_list_of_dicts.py',
    '04_data_structures/7': 'ex07_dict_of_lists.py',
    '04_data_structures/8': 'ex08_nested_dicts.py',
    '04_data_structures/9': 'ex09_safe_nested_access.py',
    '04_data_structures/10': 'ex10_deep_copy.py',
    '05_numpy/1': 'ex01_array_creation.py',
    '05_numpy/2': 'ex02_indexing.py',
    '05_numpy/3': 'ex03_boolean_indexing.py',
    '05_numpy/4': 'ex04_reshape.py',
    '05_numpy/5': 'ex05_broadcasting_basics.py',
    '05_numpy/6': 'ex06_broadcasting_gotcha.py',
    '05_numpy/7': 'ex07_aggregations.py',
    '05_numpy/8': 'ex08_vectorized_ops.py',
    '05_numpy/9': 'ex09_views_vs_copies.py',
    '05_numpy/10': 'ex10_practical.py',
    '06_pandas/1': 'ex01_dataframe_creation.py',
    '06_pandas/2': 'ex02_selecting_columns.py',
    '06_pandas/3': 'ex03_filtering_rows.py',
    '06_pandas/4': 'ex04_loc_iloc.py',
    '06_pandas/5': 'ex05_adding_columns.py',
    '06_pandas/6': 'ex06_groupby.py',
    '06_pandas/7': 'ex07_sorting.py',
    '06_pandas/8': 'ex08_missing_values.py',
    '06_pandas/9': 'ex09_merging.py',
    '06_pandas/10': 'ex10_melt.py',
    '06_pandas/11': 'ex11_pivot.py',
    '06_pandas/12': 'ex12_settingwithcopy.py',
    '07_polars/1': 'ex01_dataframe_creation.py',
    '07_polars/2': 'ex02_selecting.py',
    '07_polars/3': 'ex03_filtering.py',
    '07_polars/4': 'ex04_with_columns.py',
    '07_polars/5': 'ex05_expressions.py',
    '07_polars/6': 'ex06_groupby.py',
    '07_polars/7': 'ex07_sorting.py',
    '07_polars/8': 'ex08_nulls.py',
    '07_polars/9': 'ex09_lazy.py',
    '07_polars/10': 'ex10_pandas_conversion.py',
    '08_stats/1': 'ex01_linear_regression.py',
    '08_stats/2': 'ex02_model_results.py',
    '08_stats/3': 'ex03_intercept_trap.py',
    '08_stats/4': 'ex04_categorical.py',
    '08_stats/5': 'ex05_logistic.py',
    '08_stats/6': 'ex06_ttest.py',
    '08_stats/7': 'ex07_correlation.py',
    '08_stats/8': 'ex08_chi_squared.py',
    '08_stats/9': 'ex09_distributions.py',
    '08_stats/10': 'ex10_practical.py',
    '09_plotly/1': 'ex01_scatter.py',
    '09_plotly/2': 'ex02_line.py',
    '09_plotly/3': 'ex03_bar.py',
    '09_plotly/4': 'ex04_histogram.py',
    '09_plotly/5': 'ex05_box.py',
    '09_plotly/6': 'ex06_facets.py',
    '09_plotly/7': 'ex07_layout.py',
    '09_plotly/8': 'ex08_graph_objects.py',
    '10_capstone/1': 'ex01_load_explore.py',
    '10_capstone/2': 'ex02_cleaning.py',
    '10_capstone/3': 'ex03_transform.py',
    '10_capstone/4': 'ex04_grouped_analysis.py',
    '10_capstone/5': 'ex05_modeling.py',
    '10_capstone/6': 'ex06_visualization.py',
    '10_capstone/7': 'ex07_export.py',
  };
}

/**
 * Get total exercises for a module.
 */
export function getModuleExerciseCount(moduleId) {
  const names = getExerciseNames();
  return Object.keys(names).filter(k => k.startsWith(moduleId + '/')).length;
}
