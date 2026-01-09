"""Flask route handlers."""

from flask import Flask, render_template, request, jsonify
from .parser import get_all_modules, parse_exercise, get_module_exercises
from .executor import execute_exercise


def register_routes(app: Flask):
    """Register all routes with the Flask app."""

    @app.route("/")
    def index():
        """Home page - list all modules."""
        exercises_dir = app.config['EXERCISES_DIR']
        modules = get_all_modules(exercises_dir)
        return render_template("index.html", modules=modules)

    @app.route("/module/<module_id>")
    def module_view(module_id: str):
        """Module page - list exercises in module."""
        exercises_dir = app.config['EXERCISES_DIR']
        exercises = get_module_exercises(exercises_dir, module_id)

        if not exercises:
            return "Module not found", 404

        module_name = module_id.split('_', 1)[1].replace('_', ' ').title()
        return render_template(
            "module.html",
            module_id=module_id,
            module_name=module_name,
            exercises=exercises
        )

    @app.route("/exercise/<module_id>/<exercise_id>")
    def exercise_view(module_id: str, exercise_id: str):
        """Exercise page - display with editor."""
        exercises_dir = app.config['EXERCISES_DIR']
        exercise_path = exercises_dir / module_id / f"{exercise_id}.py"

        if not exercise_path.exists():
            return "Exercise not found", 404

        exercise = parse_exercise(exercise_path)

        # Get prev/next navigation
        all_exercises = get_module_exercises(exercises_dir, module_id)
        current_idx = next(
            (i for i, ex in enumerate(all_exercises)
             if ex.exercise_id == exercise_id),
            -1
        )

        prev_ex = all_exercises[current_idx - 1].exercise_id if current_idx > 0 else None
        next_ex = all_exercises[current_idx + 1].exercise_id if current_idx < len(all_exercises) - 1 else None

        # Get all modules for sidebar navigation
        modules = get_all_modules(exercises_dir)

        return render_template(
            "exercise.html",
            exercise=exercise,
            prev_exercise=prev_ex,
            next_exercise=next_ex,
            modules=modules
        )

    @app.route("/run", methods=["POST"])
    def run_code():
        """Execute user code and return results."""
        data = request.json
        module_id = data.get("module_id")
        exercise_id = data.get("exercise_id")
        user_code = data.get("code", "")

        exercises_dir = app.config['EXERCISES_DIR']
        project_root = app.config['PROJECT_ROOT']
        exercise_path = exercises_dir / module_id / f"{exercise_id}.py"

        if not exercise_path.exists():
            return jsonify({"error": "Exercise not found"}), 404

        result = execute_exercise(exercise_path, user_code, project_root)

        return jsonify({
            "success": result.success,
            "output": result.output,
            "error": result.error,
            "passed": result.passed,
            "passed_count": result.passed_count,
            "failed_count": result.failed_count
        })
