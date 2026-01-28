# Sample Flask app and tests for CI

This repository contains a tiny Flask app and pytest tests intended as a simple target for CI using GitHub Actions or Jenkins.

Files added:

- `app/app.py` — minimal Flask app exposing `/daily`, `/recommend`, and `/recipe/<id>`.
- `tests/test_app.py` — five pytest tests covering the endpoints.
- `requirements.txt` — lists `Flask` and `pytest`.
- `.github/workflows/ci.yml` — GitHub Actions workflow to run tests.

How to run locally

1. Create and activate a venv:

```bash
python3 -m venv .venv
. .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run tests:

```bash
pytest -q
```

What the tests cover

- daily endpoint returns a recipe
- recommend endpoint returns matching recipes when all required ingredients provided
- recommend returns empty list when no matches
- recipe endpoint returns a known recipe by id
- recipe endpoint returns 404 for missing id

Notes

These are intentionally small, deterministic tests to make CI runs reliable. You can extend the app and tests as needed for homework exercises.
