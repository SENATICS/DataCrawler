# Tell the original .pro file about additional directories.
INCLUDEPATH = "/usr/include/python2.7" "../../QtOpenGL" "/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtOpenGL"
CONFIG += release
VPATH = /home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtOpenGL
include(/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtOpenGL/qpyopengl.pro)
