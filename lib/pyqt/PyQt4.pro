TEMPLATE = subdirs
CONFIG += ordered
SUBDIRS = qpy QtCore QtGui QtHelp QtNetwork QtDeclarative QtScript QtScriptTools QtXml QtOpenGL QtSql QtSvg QtTest QtWebKit QtXmlPatterns QtDesigner QtDBus Qt pylupdate pyrcc designer

init_py.files = /home/desa2/PyQt-x11-gpl-4.10.4/__init__.py
init_py.path = /usr/local/lib/python2.7/dist-packages/PyQt4
INSTALLS += init_py

uic_package.files = /home/desa2/PyQt-x11-gpl-4.10.4/pyuic/uic
uic_package.path = /usr/local/lib/python2.7/dist-packages/PyQt4
INSTALLS += uic_package

pyuic4.files = pyuic4
pyuic4.path = /usr/bin
INSTALLS += pyuic4
