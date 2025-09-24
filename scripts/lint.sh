#!/usr/bin/env bash

set -e
set -x

mypy finesql
ruff check finesql tests docs_src
ruff format finesql tests docs_src --check
