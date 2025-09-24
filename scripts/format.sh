#!/bin/sh -e
set -x

ruff check finesql tests docs_src --fix
ruff format finesql tests docs_src
