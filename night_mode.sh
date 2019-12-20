#!/usr/bin/env bash

ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
${ROOT_DIR}/.venv/bin/python ${ROOT_DIR}/night_mode.py
