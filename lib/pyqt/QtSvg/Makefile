TARGET = QtSvg.so
OFILES = sipQtSvgcmodule.o sipQtSvgQSvgWidget.o sipQtSvgQSvgRenderer.o sipQtSvgQSvgGenerator.o sipQtSvgQGraphicsSvgItem.o
HFILES = sipAPIQtSvg.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_GUI_LIB -DQT_CORE_LIB -I. -I/usr/include/python2.7 -I/usr/mkspecs/linux-g++ -I/usr/include/qt4/QtSvg -I/usr/include/qt4/QtGui -I/usr/include/qt4/QtCore -I/usr/include/qt4 -I/usr/X11R6/include
CFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
CXXFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
LFLAGS = -shared  -Wl,-O1 -Wl,-rpath,/usr/lib/x86_64-linux-gnu -Wl,--version-script=QtSvg.exp
LIBS = -L/usr/lib/x86_64-linux-gnu -L/usr/X11R6/lib64 -lQtSvg -lQtGui -lQtCore -lXext -lX11 -lm -lpthread
MOC = /usr/bin/moc-qt4
.SUFFIXES: .c .o .cpp .cc .cxx .C


.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.C.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.c.o:
	$(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<

all: $(TARGET)

$(OFILES): $(HFILES)

$(TARGET): $(OFILES)
	@echo '{ global: initQtSvg; local: *; };' > QtSvg.exp
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4 || mkdir -p $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4
	cp -f $(TARGET) $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	strip $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	@test -d $(DESTDIR)/usr/share/sip/PyQt4/QtSvg || mkdir -p $(DESTDIR)/usr/share/sip/PyQt4/QtSvg
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtSvg/QtSvgmod.sip $(DESTDIR)/usr/share/sip/PyQt4/QtSvg/QtSvgmod.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtSvg/qsvgrenderer.sip $(DESTDIR)/usr/share/sip/PyQt4/QtSvg/qsvgrenderer.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtSvg/qgraphicssvgitem.sip $(DESTDIR)/usr/share/sip/PyQt4/QtSvg/qgraphicssvgitem.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtSvg/qsvggenerator.sip $(DESTDIR)/usr/share/sip/PyQt4/QtSvg/qsvggenerator.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtSvg/qsvgwidget.sip $(DESTDIR)/usr/share/sip/PyQt4/QtSvg/qsvgwidget.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtSvgcmodule.o
	-rm -f sipQtSvgQSvgWidget.o
	-rm -f sipQtSvgQSvgRenderer.o
	-rm -f sipQtSvgQSvgGenerator.o
	-rm -f sipQtSvgQGraphicsSvgItem.o
	-rm -f QtSvg.exp
