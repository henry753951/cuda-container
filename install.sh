#!/bin/bash
# Check if docker is installed
if ! command -v docker &> /dev/null;
then
    echo "Docker could not be found. Do you want to install it? (y/n)"
    read response
    if [ "$response" != "y" ]; then
        exit 1
    fi
    command sudo apt-get update
    for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do
        command sudo apt-get remove -y $pkg
    done
    command sudo apt-get update
    command sudo apt-get install ca-certificates curl
    command sudo install -m 0755 -d /etc/apt/keyrings
    command sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    command sudo chmod a+r /etc/apt/keyrings/docker.asc
    command echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    command sudo apt-get update
    command sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
fi

# Nvidia toolkit
# TODO: Check if nvidia-docker is installed


# Check if Python 3 is installed
if ! command -v python3.9 &> /dev/null;
then
    echo "Python 3.9 could not be found. Do you want to install it? (y/n)"
    read response
    if [ "$response" != "y" ]; then
        exit 1
    fi
    command sudo apt install software-properties-common
    command sudo add-apt-repository ppa:deadsnakes/ppa
    command sudo apt-get install python3.9
fi

# Check if pip is installed
if ! command -v pip3.9 &> /dev/null;
    echo "pip could not be found. Do you want to install it? (y/n)"
    read response
    if [ "$response" != "y" ]; then
        exit 1
    fi
    command python3.9 get-pip.py
    command sudo apt-get install python3.9-venv
fi

# Upgrade pip
sudo python3.9 -m pip install --upgrade pip

# Install required packages
sudo python3.9 -m pip install -r requirements.txt

echo "Setup complete."
