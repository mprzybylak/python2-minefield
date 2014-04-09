#!/usr/bin/env bash

echo "Installing Python..."
apt-get update
apt-get install -y -q python-software-properties
add-apt-repository -y ppa:fkrull/deadsnakes
apt-get update
apt-get install -y -q python3.4
