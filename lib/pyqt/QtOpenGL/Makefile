TARGET = QtOpenGL.so
OFILES = sipQtOpenGLcmodule.o sipQtOpenGLQList0101QGLShader.o sipQtOpenGLQGLShaderProgram.o sipQtOpenGLQGLShaderShaderType.o sipQtOpenGLQGLShader.o sipQtOpenGLQGLPixelBuffer.o sipQtOpenGLQGLFramebufferObjectFormat.o sipQtOpenGLQGLFramebufferObject.o sipQtOpenGLQGLColormap.o sipQtOpenGLQGLBuffer.o sipQtOpenGLQGLWidget.o sipQtOpenGLQGLContextBindOptions.o sipQtOpenGLQGLContext.o sipQtOpenGLQGLFormatOpenGLVersionFlags.o sipQtOpenGLQGLFormat.o sipQtOpenGLQGLFormatOptions.o sipQtOpenGLQGL.o
HFILES = sipAPIQtOpenGL.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DSIP_PROTECTED_IS_PUBLIC -Dprotected=public -DQT_NO_DEBUG -DQT_OPENGL_LIB -DQT_GUI_LIB -DQT_CORE_LIB -I. -I/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtOpenGL -I/usr/include/python2.7 -I/usr/mkspecs/linux-g++ -I/usr/include/qt4/QtOpenGL -I/usr/include/qt4/QtGui -I/usr/include/qt4/QtCore -I/usr/include/qt4 -I/usr/X11R6/include
CFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
CXXFLAGS = -m64 -pipe -fPIC -O2 -Wall -W -D_REENTRANT
LFLAGS = -shared  -Wl,-O1 -Wl,-rpath,/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtOpenGL -Wl,-rpath,/usr/lib/x86_64-linux-gnu -Wl,--version-script=QtOpenGL.exp
LIBS = -L/home/desa2/PyQt-x11-gpl-4.10.4/qpy/QtOpenGL -L/usr/lib/x86_64-linux-gnu -L/usr/X11R6/lib64 -lqpyopengl -lQtOpenGL -lQtGui -lQtCore -lGL -lXext -lX11 -lm -lpthread
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
	@echo '{ global: initQtOpenGL; local: *; };' > QtOpenGL.exp
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4 || mkdir -p $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4
	cp -f $(TARGET) $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	strip $(DESTDIR)/usr/lib/python2.7/dist-packages/PyQt4/$(TARGET)
	@test -d $(DESTDIR)/usr/share/sip/PyQt4/QtOpenGL || mkdir -p $(DESTDIR)/usr/share/sip/PyQt4/QtOpenGL
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtOpenGL/qgl.sip $(DESTDIR)/usr/share/sip/PyQt4/QtOpenGL/qgl.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtOpenGL/qglframebufferobject.sip $(DESTDIR)/usr/share/sip/PyQt4/QtOpenGL/qglframebufferobject.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtOpenGL/qglcolormap.sip $(DESTDIR)/usr/share/sip/PyQt4/QtOpenGL/qglcolormap.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtOpenGL/QtOpenGLmod.sip $(DESTDIR)/usr/share/sip/PyQt4/QtOpenGL/QtOpenGLmod.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtOpenGL/qglshaderprogram.sip $(DESTDIR)/usr/share/sip/PyQt4/QtOpenGL/qglshaderprogram.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtOpenGL/qglbuffer.sip $(DESTDIR)/usr/share/sip/PyQt4/QtOpenGL/qglbuffer.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtOpenGL/opengl_types.sip $(DESTDIR)/usr/share/sip/PyQt4/QtOpenGL/opengl_types.sip
	cp -f /home/desa2/PyQt-x11-gpl-4.10.4/sip/QtOpenGL/qglpixelbuffer.sip $(DESTDIR)/usr/share/sip/PyQt4/QtOpenGL/qglpixelbuffer.sip

clean:
	-rm -f $(TARGET)
	-rm -f sipQtOpenGLcmodule.o
	-rm -f sipQtOpenGLQList0101QGLShader.o
	-rm -f sipQtOpenGLQGLShaderProgram.o
	-rm -f sipQtOpenGLQGLShaderShaderType.o
	-rm -f sipQtOpenGLQGLShader.o
	-rm -f sipQtOpenGLQGLPixelBuffer.o
	-rm -f sipQtOpenGLQGLFramebufferObjectFormat.o
	-rm -f sipQtOpenGLQGLFramebufferObject.o
	-rm -f sipQtOpenGLQGLColormap.o
	-rm -f sipQtOpenGLQGLBuffer.o
	-rm -f sipQtOpenGLQGLWidget.o
	-rm -f sipQtOpenGLQGLContextBindOptions.o
	-rm -f sipQtOpenGLQGLContext.o
	-rm -f sipQtOpenGLQGLFormatOpenGLVersionFlags.o
	-rm -f sipQtOpenGLQGLFormat.o
	-rm -f sipQtOpenGLQGLFormatOptions.o
	-rm -f sipQtOpenGLQGL.o
	-rm -f QtOpenGL.exp
