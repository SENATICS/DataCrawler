TARGET = QtDesigner.so
OFILES = sipQtDesignercmodule.o sipQtDesignerQList0101QDesignerCustomWidgetInterface.o sipQtDesignerQPyDesignerTaskMenuExtension.o sipQtDesignerQPyDesignerPropertySheetExtension.o sipQtDesignerQPyDesignerMemberSheetExtension.o sipQtDesignerQPyDesignerCustomWidgetPlugin.o sipQtDesignerQPyDesignerCustomWidgetCollectionPlugin.o sipQtDesignerQPyDesignerContainerExtension.o sipQtDesignerQDesignerTaskMenuExtension.o sipQtDesignerQExtensionManager.o sipQtDesignerQDesignerPropertySheetExtension.o sipQtDesignerQDesignerMemberSheetExtension.o sipQtDesignerQFormBuilder.o sipQtDesignerQAbstractExtensionManager.o sipQtDesignerQExtensionFactory.o sipQtDesignerQAbstractExtensionFactory.o sipQtDesignerQDesignerCustomWidgetCollectionInterface.o sipQtDesignerQDesignerCustomWidgetInterface.o sipQtDesignerQDesignerContainerExtension.o sipQtDesignerQDesignerWidgetBoxInterface.o sipQtDesignerQDesignerPropertyEditorInterface.o sipQtDesignerQDesignerObjectInspectorInterface.o sipQtDesignerQDesignerFormWindowManagerInterface.o sipQtDesignerQDesignerFormWindowCursorInterface.o sipQtDesignerQDesignerFormWindowInterfaceFeature.o sipQtDesignerQDesignerFormWindowInterface.o sipQtDesignerQDesignerFormEditorInterface.o sipQtDesignerQAbstractFormBuilder.o sipQtDesignerQDesignerActionEditorInterface.o
HFILES = sipAPIQtDesigner.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_GUI_LIB -DQT_CORE_LIB -I. -I/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtDesigner -I/usr/include/python2.7 -I/usr/mkspecs/linux-g++ -I/usr/include/qt4/QtDesigner -I/usr/include/qt4/QtGui -I/usr/include/qt4/QtCore -I/usr/include/qt4 -I/usr/X11R6/include
CFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
CXXFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
LFLAGS = -shared  -Wl,-O1 -Wl,-rpath,/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtDesigner -Wl,-rpath,/usr/lib/x86_64-linux-gnu -Wl,--version-script=QtDesigner.exp
LIBS = -L/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtDesigner -L/usr/lib/x86_64-linux-gnu -L/usr/X11R6/lib64 -lqpydesigner -lQtDesigner -lQtGui -lQtCore -lXext -lX11 -lm -lpthread
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
	@echo '{ global: initQtDesigner; local: *; };' > QtDesigner.exp
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4 || mkdir -p $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4
	cp -f $(TARGET) $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	strip $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	@test -d $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner || mkdir -p $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/container.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/container.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/abstractformwindowmanager.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/abstractformwindowmanager.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/propertysheet.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/propertysheet.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/extension.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/extension.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/abstractobjectinspector.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/abstractobjectinspector.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/abstractpropertyeditor.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/abstractpropertyeditor.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/formbuilder.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/formbuilder.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/qpydesignercustomwidgetcollectionplugin.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/qpydesignercustomwidgetcollectionplugin.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/customwidget.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/customwidget.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/QtDesignermod.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/QtDesignermod.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/qpydesignercustomwidgetplugin.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/qpydesignercustomwidgetplugin.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/abstractformwindowcursor.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/abstractformwindowcursor.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/qpydesignertaskmenuextension.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/qpydesignertaskmenuextension.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/qpydesignermembersheetextension.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/qpydesignermembersheetextension.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/taskmenu.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/taskmenu.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/abstractwidgetbox.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/abstractwidgetbox.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/membersheet.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/membersheet.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/abstractactioneditor.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/abstractactioneditor.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/abstractformbuilder.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/abstractformbuilder.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/abstractformwindow.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/abstractformwindow.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/qpydesignercontainerextension.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/qpydesignercontainerextension.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/default_extensionfactory.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/default_extensionfactory.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/qpydesignerpropertysheetextension.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/qpydesignerpropertysheetextension.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/qextensionmanager.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/qextensionmanager.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDesigner/abstractformeditor.sip $(DESTDIR)/usr/share/sip/PyQt4/QtDesigner/abstractformeditor.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtDesignercmodule.o
	-rm -f sipQtDesignerQList0101QDesignerCustomWidgetInterface.o
	-rm -f sipQtDesignerQPyDesignerTaskMenuExtension.o
	-rm -f sipQtDesignerQPyDesignerPropertySheetExtension.o
	-rm -f sipQtDesignerQPyDesignerMemberSheetExtension.o
	-rm -f sipQtDesignerQPyDesignerCustomWidgetPlugin.o
	-rm -f sipQtDesignerQPyDesignerCustomWidgetCollectionPlugin.o
	-rm -f sipQtDesignerQPyDesignerContainerExtension.o
	-rm -f sipQtDesignerQDesignerTaskMenuExtension.o
	-rm -f sipQtDesignerQExtensionManager.o
	-rm -f sipQtDesignerQDesignerPropertySheetExtension.o
	-rm -f sipQtDesignerQDesignerMemberSheetExtension.o
	-rm -f sipQtDesignerQFormBuilder.o
	-rm -f sipQtDesignerQAbstractExtensionManager.o
	-rm -f sipQtDesignerQExtensionFactory.o
	-rm -f sipQtDesignerQAbstractExtensionFactory.o
	-rm -f sipQtDesignerQDesignerCustomWidgetCollectionInterface.o
	-rm -f sipQtDesignerQDesignerCustomWidgetInterface.o
	-rm -f sipQtDesignerQDesignerContainerExtension.o
	-rm -f sipQtDesignerQDesignerWidgetBoxInterface.o
	-rm -f sipQtDesignerQDesignerPropertyEditorInterface.o
	-rm -f sipQtDesignerQDesignerObjectInspectorInterface.o
	-rm -f sipQtDesignerQDesignerFormWindowManagerInterface.o
	-rm -f sipQtDesignerQDesignerFormWindowCursorInterface.o
	-rm -f sipQtDesignerQDesignerFormWindowInterfaceFeature.o
	-rm -f sipQtDesignerQDesignerFormWindowInterface.o
	-rm -f sipQtDesignerQDesignerFormEditorInterface.o
	-rm -f sipQtDesignerQAbstractFormBuilder.o
	-rm -f sipQtDesignerQDesignerActionEditorInterface.o
	-rm -f QtDesigner.exp
