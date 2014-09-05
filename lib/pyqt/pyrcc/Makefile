TARGET = pyrcc4
OFILES = main.o rcc.o
HFILES = rcc.h

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DQT_NO_DEBUG -DQT_CORE_LIB -DQT_XML_LIB -I. -I/usr/mkspecs/linux-g++ -I/usr/include/qt4/QtCore -I/usr/include/qt4/QtXml -I/usr/include/qt4
CFLAGS = -m64 -pipe -O2 -Wall -W -D_REENTRANT
CXXFLAGS = -m64 -pipe -O2 -Wall -W -D_REENTRANT
LFLAGS =  -Wl,-O1 -Wl,-rpath,/usr/lib/x86_64-linux-gnu
LIBS = -L/usr/lib/x86_64-linux-gnu -lQtCore -lQtXml -lpthread
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
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/usr/bin || mkdir -p $(DESTDIR)/usr/bin
	cp -f $(TARGET) $(DESTDIR)/usr/bin/$(TARGET)

clean:
	-rm -f $(TARGET)
	-rm -f main.o
	-rm -f rcc.o
