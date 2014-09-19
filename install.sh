#!/bin/bash

# IMPORTANT: This script must be run within the virtual environment

PATH_PYTHON_VENV=$1

. $PATH_PYTHON_VENV/bin/activate

echo $1

# Scrapy dependencies
sudo apt-get install libffi-dev libxslt1-dev libxslt1.1 libxml2-dev libxml2 libssl-dev -y

# PyQt4 dependencies
sudo apt-get install python-dev python-qt4 python-qt4-dev python-sip python-sip-dev build-essential gfortran libqt4-dev qt4-qmake libpq-dev libsqlite3-dev qt4-dev-#tools qt4-doc unixodbc-dev pyqt4-dev-tools -y

# RDFLib
echo "--------- Installing RDFlib"
pip install rdflib
cd lib/
# Copiar el archivo microdata.py dentro de rdflib/plugins/serializers
cp microdata.py $PATH_PYTHON_VENV/lib/python2.7/site-packages/rdflib/plugins/serializers

# SIP
cd lib
cd sip
echo "--------- Installing SIP 4.16.2"
python configure.py
make
sudo make install

# re2
cd ../re2
echo "--------- Installing re2"
#make test
sudo make install
#sudo make testinstall
pip install re2

# PyQt4
cd ..
echo "--------- Downloading and Installing PyQt 4.10.04"
wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.10.4/PyQt-x11-gpl-4.10.4.tar.gz
tar xzvf PyQt-x11-gpl-4.10.4.tar.gz
cd PyQt-x11-gpl-4.10.4
python configure-ng.py
make
sudo make install
sudo cp -r /usr/lib/python2.7/dist-packages/PyQt4 $PATH_PYTHON_VENV/lib/python2.7/site-packages/
sudo rm -f $PATH_PYTHON_VENV/lib/python2.7/site-packages/sip.so
sudo cp /usr/lib/python2.7/dist-packages/sip.so $PATH_PYTHON_VENV/lib/python2.7/site-packages/

cd ../..

# Splash
echo "--------- Installing Splash"
pip install splash

echo "---------------------------- Process completed"
