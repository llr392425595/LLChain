#!/usr/bin/env bash

python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
export FLASK_APP="main.py"

flask run -p 5500