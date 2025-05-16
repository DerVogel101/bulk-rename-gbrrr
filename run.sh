#!/bin/bash
cd "$(dirname "$0")" || exit
uv run flet run -d ./app.py
