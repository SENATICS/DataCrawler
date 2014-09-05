TARGET = QtScriptTools.so
OFILES = sipQtScriptToolscmodule.o sipQtScriptToolsQScriptEngineDebugger.o
HFILES = sipAPIQtScriptTools.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_SCRIPTTOOLS_LIB -DQT_GUI_LIB -DQT_SCRIPT_LIB -DQT_CORE_LIB -I. -I/usr/include/python2.7 -I/usr/mkspecs/linux-g++ -I/usr/include/qt4/QtScriptTools -I/usr/include/qt4/QtGui -I/usr/include/qt4/QtScript -I/usr/include/qt4/QtCore -I/usr/include/qt4 -I/usr/X11R6/include
CFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
CXXFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
LFLAGS = -shared  -Wl,-O1 -Wl,-rpath,/usr/lib/x86_64-linux-gnu -Wl,--version-script=QtScriptTools.exp
LIBS = -L/usr/lib/x86_64-linux-gnu -L/usr/X11R6/lib64 -lQtScriptTools -lQtGui -lQtScript -lQtCore -lXext -lX11 -lm -lpthread
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
	@echo '{ global: initQtScriptTools; local: *; };' > QtScriptTools.exp
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4 || mkdir -p $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4
	cp -f $(TARGET) $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	strip $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	@test -d $(DESTDIR)/usr/share/sip/PyQt4/QtScriptTools || mkdir -p $(DESTDIR)/usr/share/sip/PyQt4/QtScriptTools
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtScriptTools/QtScriptToolsmod.sip $(DESTDIR)/usr/share/sip/PyQt4/QtScriptTools/QtScriptToolsmod.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtScriptTools/qscriptenginedebugger.sip $(DESTDIR)/usr/share/sip/PyQt4/QtScriptTools/qscriptenginedebugger.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtScriptToolscmodule.o
	-rm -f sipQtScriptToolsQScriptEngineDebugger.o
	-rm -f QtScriptTools.exp
