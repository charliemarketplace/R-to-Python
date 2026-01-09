"""Flask application for Python tutorial web GUI."""

from flask import Flask
from pathlib import Path


def create_app(project_root: Path | None = None) -> Flask:
    """Create and configure Flask app."""
    app = Flask(
        __name__,
        template_folder=Path(__file__).parent / "templates",
        static_folder=Path(__file__).parent / "static"
    )

    # Store project root for exercise discovery
    if project_root is None:
        # Default: go up from src/webapp to project root
        project_root = Path(__file__).parent.parent.parent
    app.config['PROJECT_ROOT'] = project_root
    app.config['EXERCISES_DIR'] = project_root / "exercises"

    # Register routes
    from . import routes
    routes.register_routes(app)

    return app
