"""Parse exercise files to extract displayable components."""

import re
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Exercise:
    """Parsed exercise data."""
    module_id: str           # e.g., "01_fundamentals"
    module_name: str         # e.g., "Fundamentals"
    exercise_id: str         # e.g., "ex01_indexing"
    exercise_num: int        # e.g., 1
    title: str               # e.g., "Zero-Indexing Basics"
    docstring: str           # Full docstring content
    setup_code: str          # Code before user section
    user_code: str           # Editable section (default template)
    grading_code: str        # Code after user section
    file_path: Path          # Absolute path to exercise


def parse_exercise(file_path: Path) -> Exercise:
    """Parse a single exercise file."""
    content = file_path.read_text(encoding='utf-8')

    # Extract docstring
    docstring_match = re.search(r'^"""(.*?)"""', content, re.DOTALL)
    docstring = docstring_match.group(1).strip() if docstring_match else ""

    # Extract title from docstring (first line after "EXERCISE N:")
    title_match = re.search(r'EXERCISE \d+:\s*(.+)', docstring)
    title = title_match.group(1).strip() if title_match else file_path.stem

    # Split by markers
    user_start = "# ---- YOUR CODE HERE ----"
    user_end = "# ---- END YOUR CODE ----"

    start_idx = content.find(user_start)
    end_idx = content.find(user_end)

    if start_idx != -1 and end_idx != -1:
        # Find end of docstring
        doc_end = content.find('"""', 3) + 3
        setup_code = content[doc_end:start_idx].strip()
        user_code = content[start_idx + len(user_start):end_idx].strip()
        grading_code = content[end_idx + len(user_end):].strip()
    else:
        setup_code = ""
        user_code = ""
        grading_code = ""

    # Parse module and exercise info from path
    module_id = file_path.parent.name
    module_name = module_id.split('_', 1)[1].replace('_', ' ').title()
    exercise_id = file_path.stem
    # Handle exercise number extraction (ex01 -> 1)
    num_match = re.search(r'ex(\d+)', exercise_id)
    exercise_num = int(num_match.group(1)) if num_match else 0

    return Exercise(
        module_id=module_id,
        module_name=module_name,
        exercise_id=exercise_id,
        exercise_num=exercise_num,
        title=title,
        docstring=docstring,
        setup_code=setup_code,
        user_code=user_code,
        grading_code=grading_code,
        file_path=file_path
    )


def get_all_modules(exercises_dir: Path) -> dict[str, list[Exercise]]:
    """Get all modules and their exercises, sorted."""
    modules = {}
    for module_dir in sorted(exercises_dir.iterdir()):
        if module_dir.is_dir() and not module_dir.name.startswith('.'):
            exercises = []
            for ex_file in sorted(module_dir.glob("ex*.py")):
                exercises.append(parse_exercise(ex_file))
            if exercises:
                modules[module_dir.name] = exercises
    return modules


def get_module_exercises(exercises_dir: Path, module_id: str) -> list[Exercise]:
    """Get all exercises for a specific module."""
    module_dir = exercises_dir / module_id
    if not module_dir.exists():
        return []

    exercises = []
    for ex_file in sorted(module_dir.glob("ex*.py")):
        exercises.append(parse_exercise(ex_file))
    return exercises
