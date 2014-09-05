TARGET = QtDBus.so
OFILES = sipQtDBuscmodule.o sipQtDBusQDBusReply0100QString.o sipQtDBusQDBusReply0100QStringList.o sipQtDBusQDBusReply0100QDBusConnectionInterfaceRegisterServiceReply.o sipQtDBusQDBusReply1900.o sipQtDBusQDBusReply2600.o sipQtDBusQDBusReply0400.o sipQtDBusQPyDBusReply.o sipQtDBusQPyDBusPendingReply.o sipQtDBusQDBusUnixFileDescriptor.o sipQtDBusQDBusServiceWatcherWatchMode.o sipQtDBusQDBusServiceWatcher.o sipQtDBusQDBusPendingCallWatcher.o sipQtDBusQDBusPendingCall.o sipQtDBusQDBusMessage.o sipQtDBusQDBusInterface.o sipQtDBusQDBusVariant.o sipQtDBusQDBusSignature.o sipQtDBusQDBusObjectPath.o sipQtDBusQDBusError.o sipQtDBusQDBusConnectionInterface.o sipQtDBusQDBusConnectionConnectionCapabilities.o sipQtDBusQDBusConnectionRegisterOptions.o sipQtDBusQDBusConnection.o sipQtDBusQDBus.o sipQtDBusQDBusArgument.o sipQtDBusQDBusAbstractInterface.o sipQtDBusQDBusAbstractAdaptor.o
HFILES = sipAPIQtDBus.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_CORE_LIB -I. -I/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtDBus -I/usr/include/python2.7 -I/usr/mkspecs/linux-g++ -I/usr/include/qt4/QtDBus -I/usr/include/qt4/QtCore -I/usr/include/qt4
CFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
CXXFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
LFLAGS = -shared  -Wl,-O1 -Wl,-rpath,/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtDBus -Wl,-rpath,/usr/lib/x86_64-linux-gnu -Wl,--version-script=QtDBus.exp
LIBS = -L/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtDBus -L/usr/lib/x86_64-linux-gnu -lqpydbus -lQtDBus -lQtCore -lpthread
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
	@echo '{ global: initQtDBus; local: *; };' > QtDBus.exp
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4 || mkdir -p $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4
	cp -f $(TARGET) $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	strip $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	@test -d $(DESTDIR)/usr/share/sip/PyQt4/QtDBus || mkdir -p $(DESTDIR)/usr/share/sip/PyQt4/QtDBus
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qdbuserror.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/qdbuserror.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qdbusextratypes.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/qdbusextratypes.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qpydbuspendingreply.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/qpydbuspendingreply.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qdbusconnection.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/qdbusconnection.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qpydbusreply.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/qpydbusreply.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qdbusabstractinterface.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/qdbusabstractinterface.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qdbusservicewatcher.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/qdbusservicewatcher.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qdbusconnectioninterface.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/qdbusconnectioninterface.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qdbusinterface.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/qdbusinterface.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qdbusargument.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/qdbusargument.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/QtDBusmod.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/QtDBusmod.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qdbusabstractadaptor.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/qdbusabstractadaptor.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qdbusmessage.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/qdbusmessage.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qdbusunixfiledescriptor.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/qdbusunixfiledescriptor.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qdbuspendingcall.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDBus/qdbuspendingcall.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtDBuscmodule.o
	-rm -f sipQtDBusQDBusReply0100QString.o
	-rm -f sipQtDBusQDBusReply0100QStringList.o
	-rm -f sipQtDBusQDBusReply0100QDBusConnectionInterfaceRegisterServiceReply.o
	-rm -f sipQtDBusQDBusReply1900.o
	-rm -f sipQtDBusQDBusReply2600.o
	-rm -f sipQtDBusQDBusReply0400.o
	-rm -f sipQtDBusQPyDBusReply.o
	-rm -f sipQtDBusQPyDBusPendingReply.o
	-rm -f sipQtDBusQDBusUnixFileDescriptor.o
	-rm -f sipQtDBusQDBusServiceWatcherWatchMode.o
	-rm -f sipQtDBusQDBusServiceWatcher.o
	-rm -f sipQtDBusQDBusPendingCallWatcher.o
	-rm -f sipQtDBusQDBusPendingCall.o
	-rm -f sipQtDBusQDBusMessage.o
	-rm -f sipQtDBusQDBusInterface.o
	-rm -f sipQtDBusQDBusVariant.o
	-rm -f sipQtDBusQDBusSignature.o
	-rm -f sipQtDBusQDBusObjectPath.o
	-rm -f sipQtDBusQDBusError.o
	-rm -f sipQtDBusQDBusConnectionInterface.o
	-rm -f sipQtDBusQDBusConnectionConnectionCapabilities.o
	-rm -f sipQtDBusQDBusConnectionRegisterOptions.o
	-rm -f sipQtDBusQDBusConnection.o
	-rm -f sipQtDBusQDBus.o
	-rm -f sipQtDBusQDBusArgument.o
	-rm -f sipQtDBusQDBusAbstractInterface.o
	-rm -f sipQtDBusQDBusAbstractAdaptor.o
	-rm -f QtDBus.exp
