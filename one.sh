#!/bin/bash
source venv/bin/activate
python get_one.py > note.html
google-chrome note.html
deactivate
