#!/bin/bash
cd "$(dirname "$0")"

cleanup() {
    rm -rf __pycache__ components/__pycache__ venv
}

trap cleanup EXIT

if ! [ -d ./venv ]; then
    python3 -m venv venv
fi

source venv/bin/activate
python3 -m pip install -r ../requirements.txt
python3 -m playwright install chromium
python3 readme.py
deactivate
