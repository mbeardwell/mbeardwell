#!/bin/bash
cd "$(dirname "$0")"

source ../venv/bin/activate
python3 create-table.py
python3 create-readme.py
deactivate
