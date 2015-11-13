#!/bin/bash

# IMPORTANT: This script must be run within the virtual environment

PATH_PYTHON_VENV=$1

. $PATH_PYTHON_VENV/bin/activate

echo $1

# Scrapy dependencies
sudo apt-get install libffi-dev libxslt1-dev libxslt1.1 libxml2-dev libxml2 libssl-dev -y

# Other dependencies
sudo apt-get install python-dev libjpeg-dev -y

# RDFLib
echo "--------- Installing RDFlib"
pip install rdflib
cd lib/

# Copiar el archivo microdata.py dentro de rdflib/plugins/serializers
cp microdata.py $PATH_PYTHON_VENV/lib/python2.7/site-packages/rdflib/plugins/serializers

cd ..

echo "---------------------------- Process completed"
