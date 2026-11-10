# Git Flow Workflow Demo

This public demo models Git Flow for GitFlow Analyzer. It is a small workflow fixture, not a statistically representative team benchmark.

## Branch rules

- `main` contains production-ready releases and is the source for GitHub Pages deployments.
- `develop` is the integration branch for the next release.
- `feature/*` branches start from `develop` and return through pull requests.
- `release/*` branches start from `develop`; after stabilization, merge them to `main` and back to `develop`.
- `hotfix/*` branches start from `main` and merge to both `main` and `develop`.

## Automation

GitHub Actions runs the Python smoke test on pushes to `main`, `develop`, and `release/*`, and on pull requests targeting `main` or `develop`. GitHub Pages deploys from `main` only.
