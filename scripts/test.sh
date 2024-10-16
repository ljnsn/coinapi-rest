#!/usr/bin/env bash

set -e
set -x

if [ "$1" == "--network" ]; then
  uv run coverage run -m pytest -m 'network'
else
  uv run coverage run -m pytest -m 'not network'
fi

uv run coverage report
uv run coverage xml
