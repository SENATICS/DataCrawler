TARGET = QtDeclarative.so
OFILES = sipQtDeclarativecmodule.o sipQtDeclarativeQList0100QDeclarativeError.o sipQtDeclarativeQPyDeclarativePropertyValueSource.o sipQtDeclarativeQDeclarativeListProperty0100QObject.o sipQtDeclarativeQDeclarativeView.o sipQtDeclarativeQDeclarativeScriptString.o sipQtDeclarativeQDeclarativePropertyValueSource.o sipQtDeclarativeQDeclarativePropertyMap.o sipQtDeclarativeQDeclarativeProperty.o sipQtDeclarativeQDeclarativeNetworkAccessManagerFactory.o sipQtDeclarativeQDeclarativeListReference.o sipQtDeclarativeQDeclarativeItem.o sipQtDeclarativeQDeclarativeParserStatus.o sipQtDeclarativeQDeclarativeImageProvider.o sipQtDeclarativeQDeclarativeExtensionPlugin.o sipQtDeclarativeQDeclarativeExpression.o sipQtDeclarativeQDeclarativeError.o sipQtDeclarativeQDeclarativeEngine.o sipQtDeclarativeQDeclarativeContext.o sipQtDeclarativeQDeclarativeComponent.o
HFILES = sipAPIQtDeclarative.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_DECLARATIVE_LIB -DQT_GUI_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I. -I/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtDeclarative -I/usr/include/python2.7 -I/usr/mkspecs/linux-g++ -I/usr/include/qt4/QtDeclarative -I/usr/include/qt4/QtGui -I/usr/include/qt4/QtNetwork -I/usr/include/qt4/QtCore -I/usr/include/qt4 -I/usr/X11R6/include
CFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
CXXFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
LFLAGS = -shared  -Wl,-O1 -Wl,-rpath,/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtDeclarative -Wl,-rpath,/usr/lib/x86_64-linux-gnu -Wl,--version-script=QtDeclarative.exp
LIBS = -L/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtDeclarative -L/usr/lib/x86_64-linux-gnu -L/usr/X11R6/lib64 -lqpydeclarative -lQtDeclarative -lQtGui -lQtNetwork -lQtCore -lXext -lX11 -lm -lpthread
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
	@echo '{ global: initQtDeclarative; local: *; };' > QtDeclarative.exp
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4 || mkdir -p $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4
	cp -f $(TARGET) $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	strip $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	@test -d $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative || mkdir -p $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativecontext.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativecontext.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativecomponent.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativecomponent.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativeparserstatus.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativeparserstatus.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativescriptstring.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativescriptstring.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativelist.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativelist.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qpydeclarativelistproperty.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qpydeclarativelistproperty.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativenetworkaccessmanagerfactory.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativenetworkaccessmanagerfactory.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativepropertymap.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativepropertymap.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/QtDeclarativemod.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/QtDeclarativemod.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qpydeclarativepropertyvaluesource.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qpydeclarativepropertyvaluesource.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativeview.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativeview.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativepropertyvaluesource.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativepropertyvaluesource.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativeitem.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativeitem.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativeexpression.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativeexpression.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativeimageprovider.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativeimageprovider.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativeerror.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativeerror.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativeextensionplugin.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativeextensionplugin.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativeengine.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativeengine.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDeclarative/qdeclarativeproperty.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDeclarative/qdeclarativeproperty.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtDeclarativecmodule.o
	-rm -f sipQtDeclarativeQList0100QDeclarativeError.o
	-rm -f sipQtDeclarativeQPyDeclarativePropertyValueSource.o
	-rm -f sipQtDeclarativeQDeclarativeListProperty0100QObject.o
	-rm -f sipQtDeclarativeQDeclarativeView.o
	-rm -f sipQtDeclarativeQDeclarativeScriptString.o
	-rm -f sipQtDeclarativeQDeclarativePropertyValueSource.o
	-rm -f sipQtDeclarativeQDeclarativePropertyMap.o
	-rm -f sipQtDeclarativeQDeclarativeProperty.o
	-rm -f sipQtDeclarativeQDeclarativeNetworkAccessManagerFactory.o
	-rm -f sipQtDeclarativeQDeclarativeListReference.o
	-rm -f sipQtDeclarativeQDeclarativeItem.o
	-rm -f sipQtDeclarativeQDeclarativeParserStatus.o
	-rm -f sipQtDeclarativeQDeclarativeImageProvider.o
	-rm -f sipQtDeclarativeQDeclarativeExtensionPlugin.o
	-rm -f sipQtDeclarativeQDeclarativeExpression.o
	-rm -f sipQtDeclarativeQDeclarativeError.o
	-rm -f sipQtDeclarativeQDeclarativeEngine.o
	-rm -f sipQtDeclarativeQDeclarativeContext.o
	-rm -f sipQtDeclarativeQDeclarativeComponent.o
	-rm -f QtDeclarative.exp
