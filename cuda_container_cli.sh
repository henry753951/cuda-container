#!/bin/bash

# Check if virtual environment exists
if [ ! -d "venv" ]; then
  echo "Virtual environment not found. Please run install.sh first."
  exit 1
fi

# Activate the virtual environment
source venv/bin/activate

# Run the docker CLI script
python docker_cli.py

# Deactivate the virtual environment
deactivate
