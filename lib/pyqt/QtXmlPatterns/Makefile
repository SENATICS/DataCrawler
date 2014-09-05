TARGET = QtXmlPatterns.so
OFILES = sipQtXmlPatternscmodule.o sipQtXmlPatternsQVector0100QXmlNodeModelIndex.o sipQtXmlPatternsQVector0100QXmlName.o sipQtXmlPatternsQXmlSchemaValidator.o sipQtXmlPatternsQXmlSchema.o sipQtXmlPatternsQXmlResultItems.o sipQtXmlPatternsQXmlQuery.o sipQtXmlPatternsQXmlNamePool.o sipQtXmlPatternsQXmlName.o sipQtXmlPatternsQXmlFormatter.o sipQtXmlPatternsQXmlSerializer.o sipQtXmlPatternsQSourceLocation.o sipQtXmlPatternsQSimpleXmlNodeModel.o sipQtXmlPatternsQAbstractXmlReceiver.o sipQtXmlPatternsQXmlItem.o sipQtXmlPatternsQAbstractXmlNodeModel.o sipQtXmlPatternsQXmlNodeModelIndex.o sipQtXmlPatternsQAbstractUriResolver.o sipQtXmlPatternsQAbstractMessageHandler.o
HFILES = sipAPIQtXmlPatterns.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_XMLPATTERNS_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I. -I/usr/include/python2.7 -I/usr/mkspecs/linux-g++ -I/usr/include/qt4/QtXmlPatterns -I/usr/include/qt4/QtNetwork -I/usr/include/qt4/QtCore -I/usr/include/qt4
CFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
CXXFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
LFLAGS = -shared  -Wl,-O1 -Wl,-rpath,/usr/lib/x86_64-linux-gnu -Wl,--version-script=QtXmlPatterns.exp
LIBS = -L/usr/lib/x86_64-linux-gnu -lQtXmlPatterns -lQtNetwork -lQtCore -lpthread
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
	@echo '{ global: initQtXmlPatterns; local: *; };' > QtXmlPatterns.exp
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4 || mkdir -p $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4
	cp -f $(TARGET) $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	strip $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	@test -d $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns || mkdir -p $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/qxmlnamepool.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/qxmlnamepool.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/qsourcelocation.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/qsourcelocation.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/QtXmlPatternsmod.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/QtXmlPatternsmod.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/qxmlresultitems.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/qxmlresultitems.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/qabstractxmlreceiver.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/qabstractxmlreceiver.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/qxmlname.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/qxmlname.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/qabstracturiresolver.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/qabstracturiresolver.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/qxmlformatter.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/qxmlformatter.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/qabstractxmlnodemodel.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/qabstractxmlnodemodel.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/qxmlquery.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/qxmlquery.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/qabstractmessagehandler.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/qabstractmessagehandler.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/qsimplexmlnodemodel.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/qsimplexmlnodemodel.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/qxmlschema.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/qxmlschema.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/qxmlschemavalidator.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/qxmlschemavalidator.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtXmlPatterns/qxmlserializer.sip $(DESTDIR)/usr/share/sip/PyQt4/QtXmlPatterns/qxmlserializer.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtXmlPatternscmodule.o
	-rm -f sipQtXmlPatternsQVector0100QXmlNodeModelIndex.o
	-rm -f sipQtXmlPatternsQVector0100QXmlName.o
	-rm -f sipQtXmlPatternsQXmlSchemaValidator.o
	-rm -f sipQtXmlPatternsQXmlSchema.o
	-rm -f sipQtXmlPatternsQXmlResultItems.o
	-rm -f sipQtXmlPatternsQXmlQuery.o
	-rm -f sipQtXmlPatternsQXmlNamePool.o
	-rm -f sipQtXmlPatternsQXmlName.o
	-rm -f sipQtXmlPatternsQXmlFormatter.o
	-rm -f sipQtXmlPatternsQXmlSerializer.o
	-rm -f sipQtXmlPatternsQSourceLocation.o
	-rm -f sipQtXmlPatternsQSimpleXmlNodeModel.o
	-rm -f sipQtXmlPatternsQAbstractXmlReceiver.o
	-rm -f sipQtXmlPatternsQXmlItem.o
	-rm -f sipQtXmlPatternsQAbstractXmlNodeModel.o
	-rm -f sipQtXmlPatternsQXmlNodeModelIndex.o
	-rm -f sipQtXmlPatternsQAbstractUriResolver.o
	-rm -f sipQtXmlPatternsQAbstractMessageHandler.o
	-rm -f QtXmlPatterns.exp
