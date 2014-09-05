# Tell the original .pro file about additional directories.
INCLUDEPATH = "/usr/include/python2.7" "../../QtDBus" "/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtDBus"
CONFIG += release
VPATH = /home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtDBus
include(/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtDBus/qpydbus.pro)
