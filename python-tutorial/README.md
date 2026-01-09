# Python for R Data Scientists - Interactive Tutorial

An interactive, self-paced Python tutorial with auto-graded exercises designed for experienced R users transitioning to Python.

## Getting Started

### 1. Install dependencies with uv

```bash
cd python-tutorial
uv sync
```

### 2. Run an individual exercise

```bash
uv run python exercises/01_fundamentals/ex01_indexing.py
```

### 3. Run all tests for a module

```bash
uv run pytest tests/test_01_fundamentals.py -v
```

### 4. Run all tests

```bash
uv run pytest
```

## Tutorial Structure

```
python-tutorial/
├── pyproject.toml              # Dependencies and project config
├── src/grader/                 # Auto-grading utilities
│   ├── __init__.py
│   └── check.py
├── exercises/                  # 93 exercises across 10 modules
│   ├── 01_fundamentals/        # Python basics (8 exercises)
│   ├── 02_control_flow/        # Loops, comprehensions (10 exercises)
│   ├── 03_functions/           # Functions & scope (8 exercises)
│   ├── 04_data_structures/     # Lists, dicts, nesting (10 exercises)
│   ├── 05_numpy/               # NumPy arrays (10 exercises)
│   ├── 06_pandas/              # Pandas DataFrames (12 exercises)
│   ├── 07_polars/              # Polars modern DataFrame (10 exercises)
│   ├── 08_stats/               # Statistical modeling (10 exercises)
│   ├── 09_plotly/              # Data visualization (8 exercises)
│   └── 10_capstone/            # Full project (7 exercises)
└── tests/                      # Pytest test files for batch grading
```

## How to Use

1. Open an exercise file in your editor
2. Read the docstring explaining the R vs Python differences
3. Write your solution in the `# YOUR CODE HERE` section
4. Run the file to check your answer immediately

### Example Exercise

```python
# exercises/01_fundamentals/ex01_indexing.py
"""
EXERCISE: Zero-Indexing Basics

In R, the first element is x[1]. In Python, it's x[0].

TASK: Return the THIRD element from the list.
"""

letters = ['a', 'b', 'c', 'd', 'e']

# ---- YOUR CODE HERE ----
result = None  # Replace with your answer
# ---- END YOUR CODE ----
```

## Modules Overview

| Module | Topic | Focus |
|--------|-------|-------|
| 1 | Fundamentals | 0-indexing, slicing, references, truthiness |
| 2 | Control Flow | for/while loops, comprehensions, try/except |
| 3 | Functions | def, args/kwargs, scope, lambdas |
| 4 | Data Structures | lists, dicts, sets, nested data |
| 5 | NumPy | Arrays, broadcasting, axis operations |
| 6 | Pandas | DataFrame ops (tidyverse translation) |
| 7 | Polars | Modern, fast DataFrame library |
| 8 | Stats | statsmodels, scipy.stats |
| 9 | Plotly | Interactive visualization (ggplot2 translation) |
| 10 | Capstone | End-to-end data analysis project |

## Key R to Python Gotchas Covered

- **0-indexing**: Python starts at 0, R at 1
- **Slice exclusivity**: `x[1:4]` excludes index 4
- **Reference vs copy**: `y = x` creates reference, not copy
- **Mutable defaults**: `def f(lst=[])` trap
- **Late binding closures**: Lambda in loop trap
- **SettingWithCopyWarning**: Pandas view vs copy
- **No intercept trap**: statsmodels array API
- **Categorical variables**: Must use `C()` explicitly

## Dependencies

- Python >= 3.11
- numpy, pandas, polars
- plotly, statsmodels, scipy
- pytest (for testing)

Happy learning!
