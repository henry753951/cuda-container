#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 could not be found. Do you want to install it? (y/n)"
    read response
    if [ "$response" != "y" ]; then
        exit 1
    fi
    command sudo apt-get install python3
fi

# Check if pip is installed
if ! command -v pip &> /dev/null
then
    echo "pip could not be found. Do you want to install it? (y/n)"
    read response
    if [ "$response" != "y" ]; then
        exit 1
    fi
    command sudo apt-get install python3-pip
fi

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate

echo "Setup complete. To activate the virtual environment, run 'source venv/bin/activate'.
