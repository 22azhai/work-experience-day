from __future__ import annotations

from pathlib import Path
import shutil
import importlib
import importlib.util

if importlib.util.find_spec("flask") is None:
    class Flask:  # type: ignore[override]
        def __init__(self, name: str):
            self.name = name

        def route(self, _path: str):
            def decorator(func):
                return func

            return decorator

        def run(self, host: str, port: int):
            raise RuntimeError(
                "Flask is not installed. Install Flask to run the local development server."
            )

    def render_template(template_name: str) -> str:
        return Path(template_name).read_text(encoding="utf-8")
else:
    flask_module = importlib.import_module("flask")
    Flask = flask_module.Flask
    render_template = flask_module.render_template

app = Flask(__name__)


@app.route("/")
def home() -> str:
    return render_template("index.html")


def build_static(output_dir: str = "dist") -> Path:
    """Copy index.html to dist/index.html for GitHub Pages deployment."""
    source = Path("index.html")
    if not source.exists():
        raise FileNotFoundError("index.html was not found at repository root.")

    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    destination = target_dir / "index.html"
    shutil.copyfile(source, destination)
    return destination


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Alexa Marketing Playground")
    parser.add_argument(
        "--build",
        action="store_true",
        help="Copy index.html to dist/index.html for GitHub Pages deployment",
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()

    if args.build:
        output = build_static()
        print(f"Built static page: {output}")
    else:
        app.run(host=args.host, port=args.port)
