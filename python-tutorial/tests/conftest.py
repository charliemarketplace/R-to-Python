"""Pytest configuration and fixtures for the Python tutorial tests."""

import pytest
import sys
from pathlib import Path

# Add src to path so grader can be imported
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Add exercises to path
exercises_path = Path(__file__).parent.parent / "exercises"
sys.path.insert(0, str(exercises_path))


@pytest.fixture
def capture_output(capsys):
    """Fixture to capture and return stdout."""
    def _capture():
        captured = capsys.readouterr()
        return captured.out
    return _capture
