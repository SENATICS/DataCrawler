VPATH = /home/desa2/PyQt-x11-gpl-4.10.4/designer
CONFIG      += plugin release warn_on

greaterThan(QT_MAJOR_VERSION, 4) {
    QT += designer
}

lessThan(QT_MAJOR_VERSION, 5) {
    CONFIG += designer
}

TARGET      = pyqt4
TEMPLATE    = lib

INCLUDEPATH += /usr/include/python2.7
LIBS        += -L/usr/lib -lpython2.7
DEFINES     += PYTHON_LIB=\\\"libpython2.7.so\\\"

SOURCES     = pluginloader.cpp
HEADERS     = pluginloader.h

# Install.
target.path = /usr/lib/x86_64-linux-gnu/qt4/plugins/designer

python.path = /usr/lib/x86_64-linux-gnu/qt4/plugins/designer
python.files = python

INSTALLS    += target python
