#!/bin/bash

python3 -m venv pyswip_env

source pyswip_env/bin/activate

echo "pip"

pip install pyswip
pip install nltk

echo "Enter swipl executable path"

read $1

echo "Enter libswipl.dylib file path"

read $2


export PATH=$PATH:$1
export DYLD_FALLBACK_LIBRARY_PATH=$2

