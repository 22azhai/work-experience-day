# Alexa Marketing Playground

A simple starter project for work experience day.

## What this repo does
- Uses a minimal Flask app (`app.py`) to serve the page at `/`.
- Keeps all UI markup in a single `index.html` file.
- Deploys automatically to GitHub Pages via GitHub Actions.

## Local usage
```bash
python app.py --build
```
Build output is written to `dist/index.html`.

To run the Flask dev server (when Flask is installed):
```bash
python app.py
```
