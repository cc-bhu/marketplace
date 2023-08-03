#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

poetry run python -m marketplace.manage collectstatic --no-input
poetry run python -m marketplace.manage migrate
