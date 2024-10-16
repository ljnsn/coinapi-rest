#!/usr/bin/env bash

set -e
set -x

if [ "$1" == "--network" ]; then
  coverage run -m pytest -m 'network'
else
  coverage run -m pytest -m 'not network'
fi

coverage report
coverage xml
