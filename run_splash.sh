#!/bin/bash
PATH=$1
echo "virtualenv -->" $PATH
source $PATH/bin/activate
python -m splash.server