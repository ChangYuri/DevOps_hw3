# Sample Flask app and tests for CI

This repository contains a tiny Flask app and pytest tests intended as a simple target for CI using GitHub Actions or Jenkins.

Files added:

- `app/app.py` — minimal Flask app exposing `/daily`, `/recommend`, and `/recipe/<id>`.
- `tests/test_app.py` — five pytest tests covering the endpoints.
- `requirements.txt` — lists `Flask` and `pytest`.
- `.github/workflows/ci.yml` — GitHub Actions workflow to run tests.
- `.prettierrc` — configuration file for Prettier.
- `eslint.config.js` — configuration file for ESLint.
- `package.json` — lists Prettier and ESLint as dev dependencies.

What the tests cover

- daily endpoint returns a recipe
- recommend endpoint returns matching recipes when all required ingredients provided
- recommend returns empty list when no matches
- recipe endpoint returns a known recipe by id
- recipe endpoint returns 404 for missing id

The GitHub Actions workflow

The app has a simple CI workflow defined in `.github/workflows/ci.yml` that runs on pushes and pull requests. It sets up Python, installs dependencies, lints the code with flake8, and runs the pytest tests. To run the app, follow the procedures inside the workflow file, and use `uv run python -m app.app` to start the Flask server.