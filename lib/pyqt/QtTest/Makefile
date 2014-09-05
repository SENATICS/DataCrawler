TARGET = QtTest.so
OFILES = sipQtTestcmodule.o sipQtTestQTest.o
HFILES = sipAPIQtTest.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_TEST_LIB -DQT_GUI_LIB -DQT_CORE_LIB -I. -I/usr/include/python2.7 -I/usr/mkspecs/linux-g++ -I/usr/include/qt4/QtTest -I/usr/include/qt4/QtGui -I/usr/include/qt4/QtCore -I/usr/include/qt4 -I/usr/X11R6/include
CFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
CXXFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
LFLAGS = -shared  -Wl,-O1 -Wl,-rpath,/usr/lib/x86_64-linux-gnu -Wl,--version-script=QtTest.exp
LIBS = -L/usr/lib/x86_64-linux-gnu -L/usr/X11R6/lib64 -lQtTest -lQtGui -lQtCore -lXext -lX11 -lm -lpthread
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
	@echo '{ global: initQtTest; local: *; };' > QtTest.exp
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4 || mkdir -p $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4
	cp -f $(TARGET) $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	strip $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	@test -d $(DESTDIR)/usr/share/sip/PyQt4/QtTest || mkdir -p $(DESTDIR)/usr/share/sip/PyQt4/QtTest
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtTest/QtTestmod.sip $(DESTDIR)/usr/share/sip/PyQt4/QtTest/QtTestmod.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtTest/qtestkeyboard.sip $(DESTDIR)/usr/share/sip/PyQt4/QtTest/qtestkeyboard.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtTest/qtestmouse.sip $(DESTDIR)/usr/share/sip/PyQt4/QtTest/qtestmouse.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtTest/qtestcase.sip $(DESTDIR)/usr/share/sip/PyQt4/QtTest/qtestcase.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtTest/qtestsystem.sip $(DESTDIR)/usr/share/sip/PyQt4/QtTest/qtestsystem.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtTestcmodule.o
	-rm -f sipQtTestQTest.o
	-rm -f QtTest.exp
