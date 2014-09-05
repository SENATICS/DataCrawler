TARGET = QtWebKit.so
OFILES = sipQtWebKitcmodule.o sipQtWebKitQList0100QWebDatabase.o sipQtWebKitQList0100QWebSecurityOrigin.o sipQtWebKitQList0100QWebPluginFactoryPlugin.o sipQtWebKitQList0100QWebHistoryItem.o sipQtWebKitQMultiMap0100QString0100QString.o sipQtWebKitQList0101QWebFrame.o sipQtWebKitQList0100QWebElement.o sipQtWebKitQList0100QWebPluginFactoryMimeType.o sipQtWebKitQWebView.o sipQtWebKitQWebSettings.o sipQtWebKitQWebSecurityOrigin.o sipQtWebKitQWebPluginFactoryExtensionReturn.o sipQtWebKitQWebPluginFactoryExtensionOption.o sipQtWebKitQWebPluginFactoryPlugin.o sipQtWebKitQWebPluginFactoryMimeType.o sipQtWebKitQWebPluginFactory.o sipQtWebKitQWebPageViewportAttributes.o sipQtWebKitQWebPageErrorPageExtensionReturn.o sipQtWebKitQWebPageErrorPageExtensionOption.o sipQtWebKitQWebPageChooseMultipleFilesExtensionReturn.o sipQtWebKitQWebPageChooseMultipleFilesExtensionOption.o sipQtWebKitQWebPageExtensionReturn.o sipQtWebKitQWebPageExtensionOption.o sipQtWebKitQWebPageFindFlags.o sipQtWebKitQWebPage.o sipQtWebKitQWebInspector.o sipQtWebKitQWebHistoryInterface.o sipQtWebKitQWebHistory.o sipQtWebKitQWebHistoryItem.o sipQtWebKitQWebFrame.o sipQtWebKitQWebHitTestResult.o sipQtWebKitQWebElementCollection.o sipQtWebKitQWebElement.o sipQtWebKitQWebDatabase.o sipQtWebKitQGraphicsWebView.o
HFILES = sipAPIQtWebKit.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_WEBKIT_LIB -DQT_GUI_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I. -I/usr/include/python2.7 -I/usr/mkspecs/linux-g++ -I/usr/include/qt4/QtWebKit -I/usr/include/qt4/QtGui -I/usr/include/qt4/QtNetwork -I/usr/include/qt4/QtCore -I/usr/include/qt4 -I/usr/X11R6/include
CFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
CXXFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
LFLAGS = -shared  -Wl,-O1 -Wl,-rpath,/usr/lib/x86_64-linux-gnu -Wl,--version-script=QtWebKit.exp
LIBS = -L/usr/lib/x86_64-linux-gnu -L/usr/X11R6/lib64 -lQtWebKit -lQtGui -lQtNetwork -lQtCore -lXext -lX11 -lm -lpthread
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
	@echo '{ global: initQtWebKit; local: *; };' > QtWebKit.exp
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4 || mkdir -p $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4
	cp -f $(TARGET) $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	strip $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	@test -d $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit || mkdir -p $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/qwebdatabase.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/qwebdatabase.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/qwebkitversion.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/qwebkitversion.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/qwebhistoryinterface.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/qwebhistoryinterface.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/qwebview.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/qwebview.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/qwebsecurityorigin.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/qwebsecurityorigin.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/qwebhistory.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/qwebhistory.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/qwebpage.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/qwebpage.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/qwebelement.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/qwebelement.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/qwebinspector.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/qwebinspector.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/qwebkitglobal.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/qwebkitglobal.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/qwebframe.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/qwebframe.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/qgraphicswebview.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/qgraphicswebview.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/qwebsettings.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/qwebsettings.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/QtWebKitmod.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/QtWebKitmod.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtWebKit/qwebpluginfactory.sip $(DESTDIR)/usr/share/sip/PyQt4/QtWebKit/qwebpluginfactory.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtWebKitcmodule.o
	-rm -f sipQtWebKitQList0100QWebDatabase.o
	-rm -f sipQtWebKitQList0100QWebSecurityOrigin.o
	-rm -f sipQtWebKitQList0100QWebPluginFactoryPlugin.o
	-rm -f sipQtWebKitQList0100QWebHistoryItem.o
	-rm -f sipQtWebKitQMultiMap0100QString0100QString.o
	-rm -f sipQtWebKitQList0101QWebFrame.o
	-rm -f sipQtWebKitQList0100QWebElement.o
	-rm -f sipQtWebKitQList0100QWebPluginFactoryMimeType.o
	-rm -f sipQtWebKitQWebView.o
	-rm -f sipQtWebKitQWebSettings.o
	-rm -f sipQtWebKitQWebSecurityOrigin.o
	-rm -f sipQtWebKitQWebPluginFactoryExtensionReturn.o
	-rm -f sipQtWebKitQWebPluginFactoryExtensionOption.o
	-rm -f sipQtWebKitQWebPluginFactoryPlugin.o
	-rm -f sipQtWebKitQWebPluginFactoryMimeType.o
	-rm -f sipQtWebKitQWebPluginFactory.o
	-rm -f sipQtWebKitQWebPageViewportAttributes.o
	-rm -f sipQtWebKitQWebPageErrorPageExtensionReturn.o
	-rm -f sipQtWebKitQWebPageErrorPageExtensionOption.o
	-rm -f sipQtWebKitQWebPageChooseMultipleFilesExtensionReturn.o
	-rm -f sipQtWebKitQWebPageChooseMultipleFilesExtensionOption.o
	-rm -f sipQtWebKitQWebPageExtensionReturn.o
	-rm -f sipQtWebKitQWebPageExtensionOption.o
	-rm -f sipQtWebKitQWebPageFindFlags.o
	-rm -f sipQtWebKitQWebPage.o
	-rm -f sipQtWebKitQWebInspector.o
	-rm -f sipQtWebKitQWebHistoryInterface.o
	-rm -f sipQtWebKitQWebHistory.o
	-rm -f sipQtWebKitQWebHistoryItem.o
	-rm -f sipQtWebKitQWebFrame.o
	-rm -f sipQtWebKitQWebHitTestResult.o
	-rm -f sipQtWebKitQWebElementCollection.o
	-rm -f sipQtWebKitQWebElement.o
	-rm -f sipQtWebKitQWebDatabase.o
	-rm -f sipQtWebKitQGraphicsWebView.o
	-rm -f QtWebKit.exp
