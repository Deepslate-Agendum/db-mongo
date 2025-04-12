#!/usr/bin/env bash

set -x
cd ~/agendum-database
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r db_python_util/requirements.txt
python3 db_initialization.py
