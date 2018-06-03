#!/bin/bash
source ../venv/bin/activate
python get_one.py > note.html
open note.html
deactivate
