# Python for R Data Scientists: Interactive Tutorial Scope

## Project Overview

An interactive, self-paced Python tutorial with auto-graded exercises. Designed for experienced R users transitioning to Python, with emphasis on pandas, Polars, statistical modeling, plotly visualization, and Python's syntactic quirks that trip up R users.

---

## Target Audience

- Proficient R programmers
- Data science practitioners
- Comfortable with statistical concepts, data manipulation logic
- Need syntax translation and gotcha awareness, not concept explanation

---

## Technical Implementation

### Platform: Local .py files with uv

**Structure:**
```
python-tutorial/
├── pyproject.toml
├── src/
│   └── grader/
│       ├── __init__.py
│       └── check.py          # Grading utilities
├── exercises/
│   ├── 01_fundamentals/
│   │   ├── ex01_indexing.py
│   │   ├── ex02_slicing.py
│   │   └── ...
│   ├── 02_control_flow/
│   ├── 03_functions/
│   ├── 04_data_structures/
│   ├── 05_numpy/
│   ├── 06_pandas/
│   ├── 07_polars/
│   ├── 08_stats/
│   ├── 09_plotly/
│   └── 10_project/
└── tests/
    ├── test_01_fundamentals.py
    └── ...
```

**Workflow:**
1. Open `ex01_indexing.py` in IDE
2. Read problem, write solution in designated area
3. Run `uv run python exercises/01_fundamentals/ex01_indexing.py` — immediate feedback
4. Or run `uv run pytest tests/test_01_fundamentals.py` — batch grade module

### Exercise File Template

```python
# exercises/01_fundamentals/ex01_indexing.py
"""
EXERCISE: Zero-Indexing Basics

In R, the first element is x[1]. In Python, it's x[0].

Given the list `letters`, return the THIRD element.
"""

letters = ['a', 'b', 'c', 'd', 'e']

# ---- YOUR CODE HERE ----
result = None  # Replace with your answer
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check
    check(result, expected='c', hint="Remember: Python is 0-indexed, so third = index 2")
```

### Grading Module

```python
# src/grader/check.py
import numpy as np
import pandas as pd
import polars as pl

def check(got, expected, hint=None, rtol=1e-6):
    """Universal checker — handles scalars, arrays, DataFrames."""
    try:
        if isinstance(expected, (pd.DataFrame, pd.Series)):
            pd.testing.assert_frame_equal(got, expected, check_dtype=False)
        elif isinstance(expected, pl.DataFrame):
            assert got.equals(expected), "Polars DataFrames don't match"
        elif isinstance(expected, np.ndarray):
            np.testing.assert_allclose(got, expected, rtol=rtol)
        elif isinstance(expected, float):
            assert abs(got - expected) < rtol, f"Expected ~{expected}, got {got}"
        else:
            assert got == expected, f"Expected {expected!r}, got {got!r}"
        print("✓ Correct!")
        return True
    except AssertionError as e:
        print(f"✗ Not quite. {e}")
        if hint:
            print(f"  Hint: {hint}")
        return False

def check_model(model, param, expected, rtol=0.1):
    """Check statsmodels coefficient within tolerance."""
    if hasattr(model, 'params'):
        actual = model.params[param]
    else:
        raise ValueError("Not a statsmodels results object")
    assert np.isclose(actual, expected, rtol=rtol), \
        f"Coefficient '{param}': expected ~{expected}, got {actual:.4f}"
    print(f"✓ Coefficient '{param}' correct: {actual:.4f}")
    return True
```

### pyproject.toml

```toml
[project]
name = "python-tutorial"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "numpy>=1.24",
    "pandas>=2.0",
    "polars>=0.20",
    "plotly>=5.15",
    "statsmodels>=0.14",
    "scipy>=1.11",
    "scikit-learn>=1.3",
    "pytest>=7.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/grader"]
```

---

## Module Structure

### Module 1: Python Fundamentals (The Syntax Shock)

**Learning Objectives:**
- Write syntactically correct Python without R habits
- Understand 0-indexing deeply
- Navigate Python's type system

**Topics:**

1. **Indentation is syntax** — no braces, no `end`
2. **0-indexing** — `lst[0]` is first element
3. **Slice notation** — `[start:stop:step]`, stop is exclusive
4. **Assignment vs mutation** — `=` binds names, doesn't copy
5. **Truthiness** — empty list is falsy, `None` vs `NA` vs `NaN`
6. **String formatting** — f-strings, not `paste0()`

**Quirky Problems:**

```python
# What does this print?
x = [1, 2, 3]
y = x
y.append(4)
print(x)  # Answer: [1, 2, 3, 4] — same object!

# Fix the bug:
def add_to_list(item, lst=[]):  # Mutable default argument trap
    lst.append(item)
    return lst
```

**Exercises:** 8 problems

---

### Module 2: Control Flow & Loops

**Learning Objectives:**
- Write Pythonic loops (and know when not to)
- Use list/dict comprehensions fluently
- Handle exceptions gracefully

**Topics:**

1. **for loops** — iterate over objects directly, not indices
2. **enumerate() and zip()** — the Pythonic way
3. **while loops** — rare in data science, but know them
4. **Comprehensions** — list, dict, set, generator expressions
5. **try/except** — Python's error handling (vs R's `tryCatch`)

**Quirky Problems:**

```python
# R habit: for(i in 1:length(x))
# Python trap:
for i in range(len(lst)):  # Works but unpythonic
    print(lst[i])

# Pythonic:
for item in lst:
    print(item)

# Late binding closure trap:
funcs = [lambda: x**2 for x in range(5)]
print([f() for f in funcs])  # All return 16!
```

**Exercises:** 10 problems

---

### Module 3: Functions & Scope

**Learning Objectives:**
- Define functions with proper argument patterns
- Understand Python's scoping rules (LEGB)
- Use `*args`, `**kwargs` effectively

**Topics:**

1. **def syntax** — positional, keyword, default arguments
2. **Return behavior** — explicit `return`, multiple returns via tuple
3. **Scope** — local, enclosing, global, built-in (LEGB rule)
4. **Lambda functions** — anonymous functions, limitations
5. **`*args, **kwargs`** — flexible function signatures

**Quirky Problems:**

```python
# Positional after keyword error:
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet(greeting="Hi", "Alice")  # SyntaxError!

# Scope trap:
x = 10
def bar():
    print(x)  # UnboundLocalError!
    x = 20
```

**Exercises:** 8 problems

---

### Module 4: Data Structures — Lists, Dicts, Nesting

**Learning Objectives:**
- Choose appropriate data structures
- Understand mutability implications
- Navigate nested structures fluently (JSON-like data)

**Topics:**

1. **Lists vs tuples** — mutability, when to use each
2. **Dictionaries** — Python's workhorse (like R's named lists)
3. **Sets** — unique values, set operations
4. **Nested structures** — lists of lists, lists of dicts, dicts of lists
5. **JSON-like data** — the lingua franca of APIs
6. **Copying** — shallow vs deep (`copy.deepcopy()`)

**Nested Data Patterns:**

```python
# List of dicts — most common! Like records/rows
users = [
    {"name": "Alice", "age": 30, "city": "NYC"},
    {"name": "Bob", "age": 25, "city": "LA"},
]
users[0]["name"]  # "Alice"
[u["name"] for u in users]  # Extract "column"

# Dict of lists — columnar format
data = {"name": ["Alice", "Bob"], "age": [30, 25]}
# Easy: pd.DataFrame(data)

# Nested dicts — config files, hierarchical data
config = {
    "database": {"host": "localhost", "port": 5432},
    "api": {"timeout": 30, "retries": 3},
}
config.get("missing", {}).get("key", "default")  # Safe nested access
```

**Quirky Problems:**

```python
# Nested mutation trap:
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]] — inner lists shared!

# Building list of dicts wrong:
template = {"a": 0}
records = []
for i in range(3):
    template["a"] = i
    records.append(template)  # Same object 3 times!
print(records)  # [{"a": 2}, {"a": 2}, {"a": 2}]
```

**Exercises:** 10 problems

---

### Module 5: NumPy Essentials

**Learning Objectives:**
- Create and manipulate arrays
- Understand broadcasting rules
- Perform vectorized operations

**Topics:**

1. **Array creation** — `np.array()`, `zeros()`, `arange()`, `linspace()`
2. **Indexing** — integer, boolean, fancy indexing
3. **Broadcasting** — how shapes align (different from R's recycling)
4. **Vectorized operations** — avoid Python loops
5. **Axis parameter** — `axis=0` vs `axis=1`

**Quirky Problems:**

```python
# Broadcasting surprise:
a = np.array([[1], [2], [3]])  # Shape (3, 1)
b = np.array([10, 20, 30])     # Shape (3,)
print((a + b).shape)  # (3, 3) — outer product-like!

# View vs copy:
arr = np.array([1, 2, 3, 4, 5])
slice_view = arr[1:4]
slice_view[0] = 99
print(arr)  # [1, 99, 3, 4, 5] — slices are views!
```

**Exercises:** 10 problems

---

### Module 6: Pandas — The Tidyverse Translation

**Learning Objectives:**
- Translate dplyr/tidyr mental models to pandas
- Chain operations fluently
- Handle missing data the pandas way

**Translations:**

| R (tidyverse) | pandas |
|---------------|--------|
| `select(col1, col2)` | `df[['col1', 'col2']]` |
| `filter(x > 5)` | `df[df['x'] > 5]` or `df.query('x > 5')` |
| `mutate(new = a + b)` | `df.assign(new=df['a'] + df['b'])` |
| `group_by(g) %>% summarize(m = mean(x))` | `df.groupby('g')['x'].mean()` |
| `arrange(x)` | `df.sort_values('x')` |
| `pivot_longer()` | `df.melt()` |
| `pivot_wider()` | `df.pivot_table()` |
| `left_join(other, by='key')` | `df.merge(other, on='key', how='left')` |

**Quirky Problems:**

```python
# SettingWithCopyWarning trap:
df_subset = df[df['A'] > 0]
df_subset['B'] = 99  # Warning! Ambiguous

# Fix:
df_subset = df[df['A'] > 0].copy()
df_subset['B'] = 99

# Chained indexing — unpredictable:
df['A']['B']  # Don't! Use df.loc[row, col]
```

**Exercises:** 12 problems

---

### Module 7: Polars — The Modern Alternative

**Learning Objectives:**
- Understand Polars' expression-based paradigm
- Use lazy evaluation for performance
- Choose between pandas and Polars appropriately

**Why Polars:**
- Faster than pandas (Rust-based)
- No index (cleaner mental model)
- Lazy evaluation (query optimization)
- Better null handling

**Pandas → Polars:**

| pandas | Polars |
|--------|--------|
| `df['col']` | `df.select('col')` |
| `df[df['A'] > 5]` | `df.filter(pl.col('A') > 5)` |
| `df.assign(new=df['A']*2)` | `df.with_columns((pl.col('A')*2).alias('new'))` |
| `df.groupby('g').agg({'x':'mean'})` | `df.group_by('g').agg(pl.col('x').mean())` |

**The Expression System:**

```python
import polars as pl

# Composable expressions
sales = pl.col('sales')
costs = pl.col('costs')
margin = (sales - costs) / sales

df.with_columns(margin.alias('profit_margin'))

# Lazy evaluation
lf = pl.scan_csv('big_file.csv')  # Nothing loaded yet
query = lf.filter(pl.col('x') > 0).group_by('cat').agg(pl.col('y').mean())
result = query.collect()  # Optimized execution here
```

**Quirky Problems:**

```python
# No index! Use filter() and select()
# No .loc, .iloc

# Nulls vs NaN:
# Polars uses null (not NaN) for missing — cleaner

# Expression context matters:
pl.col('x').mean()  # Only valid in agg context
```

**Exercises:** 10 problems

---

### Module 8: Statistical Modeling

**Learning Objectives:**
- Fit linear and logistic regression models
- Perform common statistical tests
- Work with distributions

**R → Python Translations:**

| R | Python (statsmodels) |
|---|----------------------|
| `lm(y ~ x1 + x2, data)` | `smf.ols('y ~ x1 + x2', data).fit()` |
| `glm(..., family=binomial)` | `smf.glm(..., family=sm.families.Binomial()).fit()` |
| `summary(model)` | `model.summary()` |
| `coef(model)` | `model.params` |
| `confint(model)` | `model.conf_int()` |
| `predict(model, newdata)` | `model.predict(newdata)` |
| `t.test(x, y)` | `scipy.stats.ttest_ind(x, y)` |
| `cor.test(x, y)` | `scipy.stats.pearsonr(x, y)` |
| `chisq.test(table)` | `scipy.stats.chi2_contingency(table)` |
| `pnorm(q)` / `qnorm(p)` | `stats.norm.cdf(q)` / `stats.norm.ppf(p)` |
| `rnorm(n)` | `stats.norm.rvs(size=n)` |

**Formula API (familiar from R):**

```python
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats

# Linear regression — formula API adds intercept
model = smf.ols('mpg ~ horsepower + weight', data=mtcars).fit()
print(model.summary())
model.params        # Coefficients
model.pvalues       # p-values
model.rsquared      # R²
model.conf_int()    # 95% CI

# Logistic regression
logit = smf.glm('survived ~ age + C(sex) + C(pclass)', 
                data=titanic,
                family=sm.families.Binomial()).fit()

# Hypothesis tests
t_stat, p_val = stats.ttest_ind(group1, group2)
r, p = stats.pearsonr(x, y)

# Distributions
norm = stats.norm(loc=0, scale=1)
norm.cdf(1.96)   # P(X <= 1.96) — like pnorm()
norm.ppf(0.975)  # Quantile — like qnorm()
norm.rvs(100)    # Random sample — like rnorm()
```

**Quirky Problems:**

```python
# Array API doesn't add intercept!
X = df[['x1', 'x2']]
model = sm.OLS(y, X).fit()  # NO INTERCEPT
model = sm.OLS(y, sm.add_constant(X)).fit()  # Fixed

# Formula API DOES add intercept (like R)
model = smf.ols('y ~ x1 + x2', data=df).fit()  # Has intercept

# Categorical variables need C():
model = smf.ols('y ~ C(category) + x', data=df).fit()
# R does this automatically, Python needs explicit C()
```

**Exercises:** 10 problems

---

### Module 9: Data Visualization with Plotly

**Learning Objectives:**
- Create interactive visualizations
- Translate ggplot2 thinking to plotly
- Customize layouts and theming

**ggplot2 → Plotly:**

```python
# R: ggplot(df, aes(x, y, color=group)) + geom_point() + facet_wrap(~cat)
# Python:
import plotly.express as px
fig = px.scatter(df, x='x', y='y', color='group', facet_col='cat')
fig.show()
```

**Topics:**

1. **plotly.express** — high-level API
2. **Common plots** — scatter, line, bar, histogram, box, heatmap
3. **Faceting** — `facet_row`, `facet_col`
4. **Theming** — templates, custom styling
5. **Graph objects** — lower-level control

**Exercises:** 8 problems

---

### Module 10: Capstone Project

**Structure:**

1. Load messy real-world dataset (CSV with issues)
2. Explore and document data quality issues
3. Clean with pandas or Polars
4. Perform grouped analysis
5. Fit statistical model(s)
6. Create visualization dashboard with plotly
7. Export clean data

**Grading:** Multi-part with checks at each stage

---

## Content Inventory

| Module | Topic | Exercises | Est. Time |
|--------|-------|-----------|-----------|
| 1 | Fundamentals | 8 | 1 hr |
| 2 | Control Flow | 10 | 1.5 hrs |
| 3 | Functions | 8 | 1 hr |
| 4 | Data Structures | 10 | 1.5 hrs |
| 5 | NumPy | 10 | 1.5 hrs |
| 6 | Pandas | 12 | 2 hrs |
| 7 | Polars | 10 | 1.5 hrs |
| 8 | Stats Modeling | 10 | 1.5 hrs |
| 9 | Plotly | 8 | 1 hr |
| 10 | Capstone | 7 | 2 hrs |
| **Total** | | **93** | **~14.5 hrs** |

---

## Dependencies

```toml
# pyproject.toml dependencies
numpy>=1.24
pandas>=2.0
polars>=0.20
plotly>=5.15
statsmodels>=0.14
scipy>=1.11
pytest>=7.0
```

---

## Success Criteria

- Write pandas/Polars pipelines without StackOverflow
- Recognize and avoid Python gotchas
- Fit and interpret statistical models
- Produce Pythonic code (not "R with Python syntax")
- Navigate nested JSON-like data structures

---

## Out of Scope (v1)

- OOP deep dive (classes, inheritance)
- Web scraping / APIs
- ML libraries (sklearn pipelines, etc.)
- Async programming
- Package development