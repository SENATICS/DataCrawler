TEMPLATE = app
QT -= gui
QT += xml
CONFIG += warn_on release
target.path = /usr/bin
INSTALLS += target
INCLUDEPATH += /home/desa2/PyQt-x11-gpl-4.10.4/pyrcc
VPATH = /home/desa2/PyQt-x11-gpl-4.10.4/pyrcc
HEADERS = rcc.h
SOURCES = rcc.cpp main.cpp