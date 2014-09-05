# This script generates the Makefiles for building PyQt.  It has no dependency
# on the sipconfig module.
#
# Copyright (c) 2014 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt.
# 
# This file may be used under the terms of the GNU General Public
# License versions 2.0 or 3.0 as published by the Free Software
# Foundation and appearing in the files LICENSE.GPL2 and LICENSE.GPL3
# included in the packaging of this file.  Alternatively you may (at
# your option) use any later version of the GNU General Public
# License if such license has been publicly approved by Riverbank
# Computing Limited (or its successors, if any) and the KDE Free Qt
# Foundation. In addition, as a special exception, Riverbank gives you
# certain additional rights. These rights are described in the Riverbank
# GPL Exception version 1.1, which can be found in the file
# GPL_EXCEPTION.txt in this package.
# 
# If you are unsure which license is appropriate for your use, please
# contact the sales department at sales@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import glob
import optparse
import os
import shutil
import stat
import sys

try:
    import sysconfig
except ImportError:
    from distutils import sysconfig


# Initialise the constants.
PYQT_VERSION_STR = "4.10.4"

SIP_MIN_VERSION = '4.15.5'


class ModuleMetadata:
    """ This class encapsulates the meta-data about a PyQt4 module. """

    def __init__(self, qmake_CONFIG='', qmake_LIBS='', qmake_QT=None, qmake_TARGET='', qpy_lib='', in_consolidated=True):
        """ Initialise the meta-data. """

        # The value to add to qmake's CONFIG variable.
        self.qmake_CONFIG = qmake_CONFIG

        # The value to add to qmake's LIBS variable.
        self.qmake_LIBS = qmake_LIBS

        # The values to update qmake's QT variable.
        self.qmake_QT = [] if qmake_QT is None else qmake_QT

        # The value to set qmake's TARGET variable to.  It defaults to the name
        # of the module.
        self.qmake_TARGET = qmake_TARGET

        # The name of the qpy support library.
        self.qpy_lib = qpy_lib

        # Set if the module is to be included in a consolidated module.
        self.in_consolidated = in_consolidated


# The module meta-data for Qt4.
QT4_MODULES = {
    'dbus':             ModuleMetadata(qmake_QT=['-gui'], qmake_TARGET='qt',
                                in_consolidated=False),
    'QAxContainer':     ModuleMetadata(qmake_CONFIG='qaxcontainer'),
    'Qt':               ModuleMetadata(qmake_QT=['-core', '-gui'],
                                in_consolidated=False),
    'QtAssistant':      ModuleMetadata(qmake_LIBS='-lqassistantclient'),
    'QtCore':           ModuleMetadata(qmake_QT=['-gui'], qpy_lib='qpycore'),
    'QtDBus':           ModuleMetadata(qmake_QT=['dbus', '-gui'],
                                qpy_lib='qpydbus'),
    'QtDeclarative':    ModuleMetadata(qmake_QT=['declarative', 'network'],
                                qpy_lib='qpydeclarative'),
    'QtDesigner':       ModuleMetadata(qmake_CONFIG='designer',
                                qpy_lib='qpydesigner'),
    'QtGui':            ModuleMetadata(qpy_lib='qpygui'),
    'QtHelp':           ModuleMetadata(qmake_CONFIG='help'),
    'QtMultimedia':     ModuleMetadata(qmake_QT=['multimedia']),
    'QtNetwork':        ModuleMetadata(qmake_QT=['network', '-gui']),
    'QtOpenGL':         ModuleMetadata(qmake_QT=['opengl'],
                                qpy_lib='qpyopengl'),
    'QtScript':         ModuleMetadata(qmake_QT=['script', '-gui']),
    'QtScriptTools':    ModuleMetadata(qmake_QT=['scripttools', 'script']),
    'QtSql':            ModuleMetadata(qmake_QT=['sql']),
    'QtSvg':            ModuleMetadata(qmake_QT=['svg']),
    'QtTest':           ModuleMetadata(qmake_QT=['testlib']),
    'QtWebKit':         ModuleMetadata(qmake_QT=['webkit', 'network']),
    'QtXml':            ModuleMetadata(qmake_QT=['xml', '-gui']),
    'QtXmlPatterns':    ModuleMetadata(
                                qmake_QT=['xmlpatterns', '-gui', 'network']),
    'phonon':           ModuleMetadata(qmake_QT=['phonon'])
}

# The module meta-data for Qt5.
QT5_MODULES = {
    'dbus':             ModuleMetadata(qmake_QT=['-gui'], qmake_TARGET='qt',
                                in_consolidated=False),
    'QAxContainer':     ModuleMetadata(qmake_QT=['axcontainer']),
    'Qt':               ModuleMetadata(qmake_QT=['-core', '-gui'],
                                in_consolidated=False),
    'QtCore':           ModuleMetadata(qmake_QT=['-gui'], qpy_lib='qpycore'),
    'QtDBus':           ModuleMetadata(qmake_QT=['dbus', '-gui'],
                                qpy_lib='qpydbus'),
    'QtDeclarative':    ModuleMetadata(qmake_QT=['declarative', 'network'],
                                qpy_lib='qpydeclarative'),
    'QtDesigner':       ModuleMetadata(qmake_QT=['designer'],
                                qpy_lib='qpydesigner'),
    'QtGui':            ModuleMetadata(qmake_QT=['widgets', 'printsupport'],
                                qpy_lib='qpygui'),
    'QtHelp':           ModuleMetadata(qmake_QT=['help']),
    'QtMultimedia':     ModuleMetadata(qmake_QT=['multimedia']),
    'QtNetwork':        ModuleMetadata(qmake_QT=['network', '-gui']),
    'QtOpenGL':         ModuleMetadata(qmake_QT=['opengl'],
                                qpy_lib='qpyopengl'),
    'QtScript':         ModuleMetadata(qmake_QT=['script', '-gui']),
    'QtScriptTools':    ModuleMetadata(
                                qmake_QT=['scripttools', 'script', 'widgets']),
    'QtSql':            ModuleMetadata(qmake_QT=['sql', 'widgets']),
    'QtSvg':            ModuleMetadata(qmake_QT=['svg']),
    'QtTest':           ModuleMetadata(qmake_QT=['testlib', 'widgets']),
    'QtWebKit':         ModuleMetadata(
                                qmake_QT=['webkit', 'webkitwidgets',
                                        'network']),
    'QtXml':            ModuleMetadata(qmake_QT=['xml', '-gui']),
    'QtXmlPatterns':    ModuleMetadata(
                                qmake_QT=['xmlpatterns', '-gui', 'network'])
}


def error(msg):
    """ Display an error message and terminate.  msg is the text of the error
    message.
    """

    sys.stderr.write(format("Error: " + msg) + "\n")
    sys.exit(1)


def inform(msg):
    """ Display an information message.  msg is the text of the error message.
    """

    sys.stdout.write(format(msg) + "\n")


def format(msg, left_margin=0, right_margin=78):
    """ Format a message by inserting line breaks at appropriate places.  msg
    is the text of the message.  left_margin is the position of the left
    margin.  right_margin is the position of the right margin.  Returns the
    formatted message.
    """

    curs = left_margin
    fmsg = " " * left_margin

    for w in msg.split():
        l = len(w)
        if curs != left_margin and curs + l > right_margin:
            fmsg = fmsg + "\n" + (" " * left_margin)
            curs = left_margin

        if curs > left_margin:
            fmsg = fmsg + " "
            curs = curs + 1

        fmsg = fmsg + w
        curs = curs + l

    return fmsg


def version_to_sip_tag(version):
    """ Convert a version number to a SIP tag.  version is the version number.
    """

    # The dictionary of tags keyed by version number.  The tag used is the one
    # with the smallest key (ie. earliest version) that is greater than the
    # given version number.
    tags = {
        0x040101: None,
        0x040102: 'Qt_4_1_1',
        0x040103: 'Qt_4_1_2',
        0x040200: 'Qt_4_1_3',
        0x040202: 'Qt_4_2_0',
        0x040300: 'Qt_4_2_2',
        0x040303: 'Qt_4_3_0',
        0x040400: 'Qt_4_3_3',
        0x040401: 'Qt_4_4_0',
        0x040500: 'Qt_4_4_1',
        0x040501: 'Qt_4_5_0',
        0x040600: 'Qt_4_5_1',
        0x040601: 'Qt_4_6_0',
        0x040602: 'Qt_4_6_1',
        0x040603: 'Qt_4_6_2',
        0x040700: 'Qt_4_6_3',
        0x040701: 'Qt_4_7_0',
        0x040702: 'Qt_4_7_1',
        0x040800: 'Qt_4_7_2',
        0x040803: 'Qt_4_8_0',
        0x040804: 'Qt_4_8_3',
        0x050000: 'Qt_4_8_4',
        0x060000: 'Qt_5_0_0'
    }

    v_list = list(tags.keys())
    v_list.sort()

    for v in v_list:
        if version < v:
            tag = tags[v]
            break
    else:
        error("Unsupported Qt version: 0x%06x." % version)

    return tag


def version_to_string(version):
    """ Convert a 3 part version number encoded as a hexadecimal value to a
    string.  version is the version number.  Returns the string.
    """

    return "%u.%u.%u" % (
            ((version >> 16) & 0xff), ((version >> 8) & 0xff),
            (version & 0xff))


class HostPythonConfiguration:
    """ A container for the host Python configuration. """

    def __init__(self):
        """ Initialise the configuration. """

        self.platform = sys.platform
        self.version = sys.hexversion >> 8

        if hasattr(sysconfig, 'get_path'):
            # The modern API.
            self.inc_dir = sysconfig.get_path('include')
            self.module_dir = sysconfig.get_path('platlib')
        else:
            # The legacy distutils API.
            self.inc_dir = sysconfig.get_python_inc(plat_specific=1)
            self.module_dir = sysconfig.get_python_lib(plat_specific=1)

        if sys.platform == 'win32':
            self.bin_dir = sys.exec_prefix
            self.data_dir = sys.prefix
            self.lib_dir = sys.prefix + '\\libs'
        else:
            self.bin_dir = sys.exec_prefix + '/bin'
            self.data_dir = sys.prefix + '/share'
            self.lib_dir = sys.prefix + '/lib'

        # The name of the interpreter used by the pyuic4 wrapper.
        if sys.platform == 'darwin':
            # The installation of MacOS's python is a mess that changes from
            # version to version and where sys.executable is useless.

            py_major = self.version >> 16
            py_minor = (self.version >> 8) & 0xff

            # In Python v3.4 and later there is no pythonw.
            if (py_major == 3 and py_minor >= 4) or py_major >= 4:
                exe = "python"
            else:
                exe = "pythonw"

            self.pyuic_interpreter = '%s%d.%d' % (exe, py_major, py_minor)
        else:
            self.pyuic_interpreter = sys.executable


class TargetQtConfiguration:
    """ A container for the target Qt configuration. """

    def __init__(self, qmake):
        """ Initialise the configuration.  qmake is the full pathname of the
        qmake executable that will provide the configuration.
        """

        inform("Querying qmake about your Qt installation...")

        pipe = os.popen(' '.join([qmake, '-query']))

        for l in pipe:
            l = l.strip()

            tokens = l.split(':', 1)
            if isinstance(tokens, list):
                if len(tokens) != 2:
                    error("Unexpected output from qmake: '%s'\n" % l)

                name, value = tokens
            else:
                name = tokens
                value = None

            name = name.replace('/', '_')

            setattr(self, name, value)

        pipe.close()


class TargetConfiguration:
    """ A container for configuration information about the target. """

    def __init__(self):
        """ Initialise the configuration with default values. """

        # Values based on the host Python configuration.
        py_config = HostPythonConfiguration()
        self.bin_dir = py_config.bin_dir
        self.module_dir = py_config.module_dir
        self.py_inc_dir = py_config.inc_dir
        self.py_lib_dir = py_config.lib_dir
        self.py_platform = py_config.platform
        self.py_version = py_config.version
        self.pyuic_interpreter = py_config.pyuic_interpreter
        self.sip_dir = os.path.join(py_config.data_dir, 'sip', 'PyQt4')
        self.sip_inc_dir = py_config.inc_dir
        self.vend_inc_dir = py_config.inc_dir
        self.vend_lib_dir = py_config.lib_dir

        # The default qmake spec.
        if self.py_platform == 'win32':
            if self.py_version >= 0x030300:
                self.qmake_spec = 'win32-msvc2010'
            elif self.py_version >= 0x020600:
                self.qmake_spec = 'win32-msvc2008'
            elif self.py_version >= 0x020400:
                self.qmake_spec = 'win32-msvc.net'
            else:
                self.qmake_spec = 'win32-msvc'
        else:
            # Use the Qt default.  (We may update it for MacOS/X later.)
            self.qmake_spec = ''

        # Remaining values.
        self.consolidate = False
        self.dbus_inc_dirs = []
        self.dbus_lib_dirs = []
        self.dbus_libs = []
        self.debug = False
        self.designer_plugin_dir = ''
        self.modules = []
        self.no_deprecated = False
        self.no_designer_plugin = False
        self.no_docstrings = False
        self.prot_is_public = (self.py_platform.startswith('linux') or self.py_platform == 'darwin')
        self.qmake = self._find_exe('qmake')
        self.qmake_variables = []
        self.pydbus_inc_dir = ''
        self.pydbus_module_dir = ''
        self.qsci_api = False
        self.qsci_api_dir = ''
        self.qt_disabled_features = []
        self.qt_framework = False
        self.qt_licensee = ''
        self.qt_shared = False
        self.qt_version = 0
        self.sip = self._find_exe('sip')
        self.static = False
        self.static_plugins = []
        self.vend_enabled = False

    def from_configuration_file(self, config_file):
        """ Initialise the configuration with values from a file.  config_file
        is the name of the configuration file.
        """

        inform("Reading configuration from %s..." % config_file)

        cfg = open(config_file)
        line_nr = 0

        for l in cfg:
            line_nr += 1
            l = l.strip()

            if len(l) == 0 or l[0] == '#':
                continue

            eq = l.find('=')
            if eq > 0:
                name = l[:eq - 1].rstrip()
                value = l[eq + 1:].lstrip()
            else:
                name = value = ''

            if name == '' or value == '':
                error("%s:%d: Invalid line." % (config_file, line_nr))

            default_value = getattr(self, name, None)
            if default_value is None:
                error(
                        "%s:%d: Unknown item: %s." %
                                (config_file, line_nr, name))

            if isinstance(default_value, int):
                if value.startswith('0x'):
                    value = int(value, 16)
                else:
                    value = int(value)
            elif isinstance(default_value, list):
                value = value.split()

            setattr(self, name, value)

        cfg.close()

    def from_introspection(self, verbose):
        """ Initialise the configuration by introspecting the system. """

        inform("Determining the details of your Qt installation...")

        out_file = 'qtdetail.out'

        source = '''#include <QCoreApplication>
#include <QFile>
#include <QLibraryInfo>
#include <QTextStream>

int main(int argc, char **argv)
{
    QCoreApplication app(argc, argv);
    QFile outf("%s");

    if (!outf.open(QIODevice::WriteOnly|QIODevice::Truncate|QIODevice::Text))
        return 1;

    QTextStream out(&outf);

    out << QLibraryInfo::licensee() << '\\n';

#if defined(QT_SHARED) || defined(QT_DLL)
    out << "shared\\n";
#else
    out << "\\n";
#endif

    // Determine which features should be disabled.

#if defined(QT_NO_ACCESSIBILITY)
    out << "PyQt_Accessibility\\n";
#endif

#if defined(QT_NO_SESSIONMANAGER)
    out << "PyQt_SessionManager\\n";
#endif

#if defined(QT_NO_STATUSTIP)
    out << "PyQt_StatusTip\\n";
#endif

#if defined(QT_NO_TOOLTIP)
    out << "PyQt_ToolTip\\n";
#endif

#if defined(QT_NO_WHATSTHIS)
    out << "PyQt_WhatsThis\\n";
#endif

#if defined(QT_NO_OPENSSL)
    out << "PyQt_OpenSSL\\n";
#endif

#if defined(QT_NO_SIZEGRIP)
    out << "PyQt_SizeGrip\\n";
#endif

#if defined(QT_NO_SYSTEMTRAYICON)
    out << "PyQt_SystemTrayIcon\\n";
#endif

#if defined(QT_NO_PRINTDIALOG)
    out << "PyQt_PrintDialog\\n";
#endif

#if defined(QT_NO_PRINTER)
    out << "PyQt_Printer\\n";
#endif

#if defined(QT_NO_PRINTPREVIEWDIALOG)
    out << "PyQt_PrintPreviewDialog\\n";
#endif

#if defined(QT_NO_PRINTPREVIEWWIDGET)
    out << "PyQt_PrintPreviewWidget\\n";
#endif

#if defined(QT_NO_RAWFONT)
    out << "PyQt_RawFont\\n";
#endif

#if !defined(QT3_SUPPORT) || QT_VERSION >= 0x040200
    out << "PyQt_NoPrintRangeBug\\n";
#endif

#if defined(QT_OPENGL_ES)
    out << "PyQt_NoOpenGLES\\n";
#endif

#if defined(QT_NO_FPU) || defined(QT_ARCH_ARM) || defined(QT_ARCH_WINDOWSCE) || defined(QT_ARCH_SYMBIAN) || defined(QT_ARCH_VXWORKS)
    out << "PyQt_qreal_double\\n";
#endif

    return 0;
}
''' % out_file

        cmd = compile_qt_program(self, verbose, 'qtdetail', source, 'QtCore')
        if cmd is None:
            error("Failed to determine the detail of your Qt installation. Try again using the --verbose flag to see more detail about the problem.")

        # Create the output file, first making sure it doesn't exist.
        remove_file(out_file)
        run_command(cmd, verbose)

        if not os.access(out_file, os.F_OK):
            error("%s failed to create %s. Make sure your Qt installation is correct." % (cmd, out_file))

        # Read the details.
        f = open(out_file)
        lines = f.read().strip().split('\n')
        f.close()

        self.qt_licensee = lines[0]
        self.qt_shared = (lines[1] == 'shared')
        self.qt_disabled_features = lines[2:]

        # 'Nokia' is the value that is used by Maemo's version of Qt.
        if self.qt_licensee in ('Open Source', 'Nokia'):
            self.qt_licensee = ''

    def get_qt_configuration(self, opts):
        """ Get the Qt configuration that can be extracted from qmake.  opts
        are the command line options.
        """

        try:
            qmake = opts.qmake
        except AttributeError:
            # Windows.
            qmake = None

        if qmake is not None:
            self.qmake = qmake
        elif self.qmake is None:
            # Under Windows qmake and the Qt DLLs must be on the system PATH
            # otherwise the dynamic linker won't be able to resolve the
            # symbols.  On other systems we assume we can just run qmake by
            # using its full pathname.
            if sys.platform == 'win32':
                error("Make sure you have a working Qt qmake on your PATH.")
            else:
                error(
                        "Use the --qmake argument to explicitly specify a "
                        "working Qt qmake.")

        # Query qmake.
        qt_config = TargetQtConfiguration(self.qmake)

        self.qt_version = 0
        try:
            qt_version_str = qt_config.QT_VERSION
            for v in qt_version_str.split('.'):
                self.qt_version *= 256
                self.qt_version += int(v)
        except AttributeError:
            qt_version_str = None

        # Check the Qt version number as soon as possible.  Note that I'm not
        # sure when the -query flag was added to qmake (maybe not until v4.6),
        # so we try to cover all bases with the error message.
        if qt_version_str is None:
            if sys.platform == 'win32':
                error(
                        "PyQt4 requires Qt v4.1.0 or later. Make sure the "
                        "correct version of qmake is on your PATH. If you are "
                        "sure you are using Qt v4 then try the configure.py "
                        "script instead of this one.")
            else:
                error(
                        "PyQt4 requires Qt v4.1.0 or later. Use the --qmake "
                        "flag to specify the correct version of qmake. If you "
                        "are sure you are using Qt v4 then try the "
                        "configure.py script instead of this one.")

        if self.qt_version < 0x040100:
            if sys.platform == 'win32':
                error(
                        "PyQt4 requires Qt v4.1.0 or later. You seem to be "
                        "using v%s. Make sure the correct version of qmake is "
                        "on your PATH." % qt_version_str)
            else:
                error(
                        "PyQt4 requires Qt v4.1.0 or later. You seem to be "
                        "using v%s. Use the --qmake flag to specify the "
                        "correct version of qmake." % qt_version_str)

        self.designer_plugin_dir = qt_config.QT_INSTALL_PLUGINS + '/designer'

        # By default, install the API file if QScintilla seems to be installed
        # in the default location.
        self.qsci_api_dir = os.path.join(qt_config.QT_INSTALL_DATA, 'qsci')
        self.qsci_api = os.path.isdir(self.qsci_api_dir)

        if opts.qmakespec is not None:
            self.qmake_spec = opts.qmakespec

        if sys.platform == 'darwin':
            if opts.qmakespec is None:
                # The binary MacOS/X Qt installer defaults to XCode.  If this
                # is what we might have then use macx-clang (Qt v5) or macx-g++
                # (Qt v4).
                try:
                    # Qt v5.
                    if qt_config.QMAKE_SPEC == 'macx-xcode':
                        # This will exist (and we can't check anyway).
                        self.qmake_spec = 'macx-clang'
                except AttributeError:
                    # Qt v4.
                    self.qmake_spec = 'macx-g++'

            # See if it is a framework.
            if os.access(os.path.join(qt_config.QT_INSTALL_LIBS, 'QtCore.framework'), os.F_OK):
                self.qt_framework = True

    def override_defaults(self, opts):
        """ Override the defaults from the command line.  opts are the command
        line options.
        """

        if opts.assumeshared:
            self.qt_shared = True

        if opts.bindir is not None:
            self.bin_dir = opts.bindir

        if opts.consolidate:
            self.consolidate = True

        if opts.debug:
            self.debug = True

        if opts.designerplugindir is not None:
            self.designer_plugin_dir = opts.designerplugindir

        if opts.destdir is not None:
            self.module_dir = opts.destdir

        if len(opts.modules) > 0:
            self.modules = opts.modules

        if opts.nodeprecated:
            self.no_deprecated = True

        if opts.nodesignerplugin:
            self.no_designer_plugin = True

        if opts.nodocstrings:
            self.no_docstrings = True

        if opts.protispublic is not None:
            self.prot_is_public = opts.protispublic

        if opts.pydbusincdir is not None:
            self.pydbus_inc_dir = opts.pydbusincdir

        if opts.pyuicinterpreter is not None:
            self.pyuic_interpreter = opts.pyuicinterpreter

        if opts.qmakespec is not None:
            self.qmake_spec = opts.qmakespec

        if opts.qsciapidir is not None:
            self.qsci_api_dir = opts.qsciapidir

            # Assume we want to install the API file if we have provided an
            # installation directory.
            self.qsci_api = True

        if opts.qsciapi is not None:
            self.qsci_api = opts.qsciapi

        if opts.qsciapidir is not None:
            self.qsci_api_dir = opts.qsciapidir

        if opts.sip is not None:
            self.sip = opts.sip

        if opts.sipdir is not None:
            self.sip_dir = opts.sipdir

        if opts.sipincdir is not None:
            self.sip_inc_dir = opts.sipincdir

        if opts.static:
            self.static = True

        if len(opts.staticplugins) > 0:
            self.static_plugins = opts.staticplugins

        if opts.vendenabled:
            self.vend_enabled = True

        if opts.vendincdir is not None:
            self.vend_inc_dir = opts.vendincdir

        if opts.vendlibdir is not None:
            self.vend_lib_dir = opts.vendlibdir

        # Handle any conflicts.
        if self.qt_shared:
            if len(self.static_plugins) != 0:
                inform(
                        "Static plugins are disabled because Qt has been "
                        "built as shared libraries.")
                self.static_plugins = []
        else:
            if self.consolidate or self.static:
                pass
            else:
                error(
                        "Qt has been built as static libraries so either the "
                        "--consolidate or --static argument should be used.")

        if self.vend_enabled and self.static:
            error(
                    "Using the VendorID package when building static "
                    "libraries makes no sense.")

    @staticmethod
    def _find_exe(exe):
        """ Find an executable, ie. the first on the path. """

        try:
            path = os.environ['PATH']
        except KeyError:
            path = ''

        if sys.platform == 'win32':
            exe = exe + '.exe'

        for d in path.split(os.pathsep):
            exe_path = os.path.join(d, exe)

            if os.path.isfile(exe_path) and os.access(exe_path, os.X_OK):
                return exe_path

        return None


def create_optparser(target_config):
    """ Create the parser for the command line.  target_config is the target
    configuration containing default values.
    """

    def store_abspath(option, opt_str, value, parser):
        setattr(parser.values, option.dest, os.path.abspath(value))

    def store_abspath_dir(option, opt_str, value, parser):
        if not os.path.isdir(value):
            raise optparse.OptionValueError("'%s' is not a directory" % value)
        setattr(parser.values, option.dest, os.path.abspath(value))

    def store_abspath_exe(option, opt_str, value, parser):
        if not os.access(value, os.X_OK):
            raise optparse.OptionValueError("'%s' is not an executable" % value)
        setattr(parser.values, option.dest, os.path.abspath(value))

    def store_abspath_file(option, opt_str, value, parser):
        if not os.path.isfile(value):
            raise optparse.OptionValueError("'%s' is not a file" % value)
        setattr(parser.values, option.dest, os.path.abspath(value))

    p = optparse.OptionParser(usage="python %prog [opts] [name=value] "
            "[name+=value]", version=PYQT_VERSION_STR)

    # Note: we don't use %default to be compatible with Python 2.3.
    p.add_option("--static", "-k", dest='static', default=False,
            action='store_true',
            help="build modules as static libraries")
    p.add_option("--no-docstrings", dest='nodocstrings', default=False,
            action='store_true',
            help="disable the generation of docstrings")
    p.add_option("--trace", "-r", dest='tracing', default=False,
            action='store_true',
            help="build modules with tracing enabled")
    p.add_option("--debug", "-u", dest='debug', default=False,
            action='store_true',
            help="build modules with debugging symbols")
    p.add_option("--verbose", "-w", dest='verbose', default=False,
            action='store_true',
            help="enable verbose output during configuration")

    p.add_option("--concatenate", "-c", dest='concat', default=False,
            action='store_true',
            help="concatenate each module's C++ source files")
    p.add_option("--concatenate-split", "-j", dest='split', type='int',
            default=1, metavar="N",
            help="split the concatenated C++ source files into N pieces "
                    "[default: 1]")
    p.add_option("--consolidate", "-g", dest='consolidate', default=False,
            action='store_true',
            help="create a single module which links against all the Qt "
                    "libraries")

    # Configuration.
    g = optparse.OptionGroup(p, title="Configuration")
    g.add_option("--confirm-license", dest='license_confirmed', default=False,
            action='store_true',
            help="confirm acceptance of the license")
    g.add_option("--spec", dest='qmakespec', default=None, action='store',
            metavar="SPEC",
            help="pass -spec SPEC to qmake [default: %s]" % "don't pass -spec" if target_config.qmake_spec == '' else target_config.qmake_spec)
    g.add_option("--enable", "-e", dest='modules', default=[], action='append',
            metavar="MODULE",
            help="enable checks for the specified MODULE [default: checks for "
                    "all modules will be enabled]")
    g.add_option("--no-designer-plugin", dest='nodesignerplugin',
            default=False, action='store_true',
            help="disable the building of the Python plugin for Qt Designer "
                    "[default: enabled]")
    g.add_option("--plugin", "-t", dest='staticplugins', default=[],
            action='append', metavar="PLUGIN",
            help="add PLUGIN to the list be linked (if Qt is built as static "
                    "libraries)")
    g.add_option("--assume-shared", dest='assumeshared', default=False,
            action='store_true',
            help="assume that the Qt libraries have been built as shared "
                    "libraries [default: check]")
    g.add_option("--no-timestamp", "-T", dest='notimestamp', default=False,
            action='store_true',
            help="suppress timestamps in the header comments of generated "
                    "code [default: include timestamps]")
    g.add_option("--no-deprecated", dest='nodeprecated', default=False,
            action='store_true',
            help="disable Qt v4 features deprecated in Qt v5 [default: "
                    "enabled]")
    g.add_option("--configuration", dest='config_file', type='string',
            action='callback', callback=store_abspath_file, metavar="FILE",
            help="FILE contains the target configuration")

    g.add_option("--protected-is-public", dest='protispublic', default=None,
            action='store_true',
            help="enable building with 'protected' redefined as 'public' "
                    "[default: %s]" %
                            "enabled" if target_config.prot_is_public
                            else "disabled")
    g.add_option("--protected-not-public", dest='protispublic', default=None,
            action='store_false',
            help="disable building with 'protected' redefined as 'public'")

    g.add_option("--pyuic4-interpreter", dest='pyuicinterpreter',
            type='string', default=None, action='callback',
            callback=store_abspath_exe, metavar="FILE",
            help="the name of the Python interpreter to run the pyuic4 "
                    "wrapper is FILE [default: %s]" %
                            target_config.pyuic_interpreter)

    if sys.platform != 'win32':
        g.add_option("--qmake", "-q", dest='qmake', type='string',
                default=None, action='callback', callback=store_abspath_exe,
                metavar="FILE",
                help="the pathname of qmake is FILE [default: "
                        "%s]" % (target_config.qmake or "search PATH"))

    g.add_option("--sip", dest='sip', type='string', default=None,
            action='callback', callback=store_abspath_exe, metavar="FILE",
            help="the pathname of sip is FILE [default: "
                    "%s]" % (target_config.sip or "None"))
    g.add_option("--sip-incdir", dest='sipincdir', type='string',
            default=None, action='callback', callback=store_abspath_dir,
            metavar="DIR",
            help="the directory containing the sip.h header file is DIR "
                    "[default: %s]" % target_config.sip_inc_dir)

    g.add_option("--dbus", "-s", dest='pydbusincdir', type='string',
            default=None, action='callback', callback=store_abspath_dir,
            metavar="DIR",
            help="the directory containing the dbus/dbus-python.h header is "
            "DIR [default: supplied by pkg-config]")
    p.add_option_group(g)

    # Installation.
    g = optparse.OptionGroup(p, title="Installation")
    g.add_option("--bindir", "-b", dest='bindir', type='string', default=None,
            action='callback', callback=store_abspath, metavar="DIR",
            help="install pyuic4, pyrcc4 and pylupdate4 in DIR [default: "
                    "%s]" % target_config.bin_dir)
    g.add_option("--destdir", "-d", dest='destdir', type='string',
            default=None, action='callback', callback=store_abspath,
            metavar="DIR",
            help="install the PyQt4 Python package in DIR [default: "
                    "%s]" % target_config.module_dir)
    g.add_option("--designer-plugindir", dest='designerplugindir',
            type='string', default=None, action='callback',
            callback=store_abspath, metavar="DIR",
            help="install the Python plugin for Qt Designer in DIR "
                    "[default: QT_INSTALL_PLUGINS/designer]")
    g.add_option("--no-sip-files", action="store_false", default=True,
            dest="install_sipfiles", help="disable the installation of the "
            ".sip files [default: enabled]")
    g.add_option("--sipdir", "-v", dest='sipdir', type='string', default=None,
            action='callback', callback=store_abspath, metavar="DIR",
            help="install the PyQt4 .sip files in DIR [default: %s]" %
                    target_config.sip_dir)
    p.add_option_group(g)

    # Vendor ID.
    g = optparse.OptionGroup(p, title="VendorID support")
    g.add_option("--vendorid", "-i", dest='vendenabled', default=False,
            action='store_true',
            help="enable checking of signed interpreters using the VendorID "
                    "package [default: %s]" %
                    "enabled" if target_config.vend_enabled else "disabled")
    g.add_option("--vendorid-incdir", "-l", dest='vendincdir', type='string',
            default=None, action='callback', callback=store_abspath_dir,
            metavar="DIR",
            help="the VendorID header file is installed in DIR [default: "
                    "%s]" % target_config.vend_inc_dir)
    g.add_option("--vendorid-libdir", "-m", dest='vendlibdir', type='string',
            default=None, action='callback', callback=store_abspath_dir,
            metavar="DIR",
            help="the VendorID library is installed in DIR [default: "
                    "%s]" % target_config.vend_lib_dir)
    p.add_option_group(g)

    # QScintilla.
    g = optparse.OptionGroup(p, title="QScintilla support")
    g.add_option("--qsci-api", "-a", dest='qsciapi', default=None,
            action='store_true',
            help="always install the PyQt API file for QScintilla [default: "
                    "install only if QScintilla installed]")
    g.add_option("--no-qsci-api", dest='qsciapi', default=None,
            action='store_false',
            help="do not install the PyQt API file for QScintilla [default: "
                    "install only if QScintilla installed]")
    g.add_option("--qsci-api-destdir", "-n", dest='qsciapidir', type='string',
            default=None, action='callback', callback=store_abspath,
            metavar="DIR",
            help="install the PyQt4 API file for QScintilla in DIR [default: "
                    "QT_INSTALL_DATA/qsci]")
    p.add_option_group(g)

    return p


def check_modules(target_config, verbose):
    """ Check which modules can be built and update the target configuration
    accordingly.  target_config is the target configuration.  verbose is set if
    the output is to be displayed.
    """

    # Note that the order in which we check is important for the consolidated
    # module - a module's dependencies must be checked first.

    target_config.modules.append('QtCore')

    check_module(target_config, verbose, 'QtGui', 'qwidget.h', 'new QWidget()')
    check_module(target_config, verbose, 'QtHelp', 'qhelpengine.h',
            'new QHelpEngine("foo")')
    check_module(target_config, verbose, 'QtMultimedia', 'QAudioDeviceInfo',
            'new QAudioDeviceInfo()')
    check_module(target_config, verbose, 'QtNetwork', 'qhostaddress.h',
            'new QHostAddress()')

    if target_config.qt_version < 0x050000 or not target_config.no_deprecated:
        check_module(target_config, verbose, 'QtDeclarative',
                'qdeclarativeview.h', 'new QDeclarativeView()')
        check_module(target_config, verbose, 'QtScript', 'qscriptengine.h',
                'new QScriptEngine()')
        check_module(target_config, verbose, 'QtScriptTools',
                'qscriptenginedebugger.h', 'new QScriptEngineDebugger()')
        check_module(target_config, verbose, 'QtXml', 'qdom.h',
                'new QDomDocument()')

    check_module(target_config, verbose, 'QtOpenGL', 'qgl.h',
            'new QGLWidget()')
    check_module(target_config, verbose, 'QtSql', 'qsqldatabase.h',
            'new QSqlDatabase()')
    check_module(target_config, verbose, 'QtSvg', 'qsvgwidget.h',
            'new QSvgWidget()')
    check_module(target_config, verbose, 'QtTest', 'QtTest',
            'QTest::qSleep(0)')
    check_module(target_config, verbose, 'QtWebKit', 'qwebpage.h',
            'new QWebPage()')
    check_module(target_config, verbose, 'QtXmlPatterns', 'qxmlname.h',
            'new QXmlName()')

    if target_config.qt_version < 0x050000:
        check_module(target_config, verbose, 'phonon', 'phonon/videowidget.h',
                'new Phonon::VideoWidget()')

    if target_config.qt_version < 0x040700:
        check_module(target_config, verbose, 'QtAssistant',
                'qassistantclient.h', 'new QAssistantClient("foo")')

    if target_config.qt_shared:
        check_module(target_config, verbose, 'QtDesigner', 'QExtensionFactory',
                'new QExtensionFactory()')
    else:
        inform("QtDesigner module disabled with static Qt libraries.")

    check_module(target_config, verbose, 'QAxContainer', 'qaxobject.h',
            'new QAxObject()')

    # Qt v4.7 was current when we added support for QtDBus and we didn't bother
    # properly versioning its API.
    if target_config.qt_version >= 0x040700:
        check_module(target_config, verbose, 'QtDBus', 'qdbusconnection.h',
                    'QDBusConnection::systemBus()')

    check_dbus(target_config, verbose)


def generate_makefiles(target_config, verbose, no_timestamp, parts, tracing):
    """ Generate the makefiles to build everything.  target_config is the
    target configuration.  verbose is set if the output is to be displayed.
    no_timestamp is set if the .sip files should exclude the timestamp.  parts
    is the number of parts the generated code should be split into.  tracing is
    set if the generated code should include tracing calls.
    """

    # For the top-level .pro file.
    toplevel_pro = 'PyQt4.pro'
    qpy_src_dir = 'qpy'
    subdirs = [qpy_src_dir]

    # Set the SIP platform, version and feature flags.
    sip_flags = get_sip_flags(target_config)

    # Embed the sip flags.
    inform("Embedding sip flags...")

    qpy_qtcore_src_dir = os.path.join(qpy_src_dir, 'QtCore')
    mk_dir(qpy_qtcore_src_dir)

    in_f = open(source_path(qpy_qtcore_src_dir, 'qpycore_post_init.cpp.in'))
    out_f = open_for_writing(
            os.path.join(qpy_qtcore_src_dir, 'qpycore_post_init.cpp'))

    for line in in_f:
        line = line.replace('@@PYQT_SIP_FLAGS@@', sip_flags)
        out_f.write(line)

    in_f.close()
    out_f.close()

    # Go through the modules.
    qpy_subdirs = []

    for mname in target_config.modules:
        metadata = get_module_metadata(target_config, mname)

        if metadata.qpy_lib != '':
            qpy_subdirs.append(mname)

            inform("Generating the .pro file for the QPy support library for %s..." % mname)

            qpy_mod_src_dir = os.path.join(qpy_src_dir, mname)
            mk_dir(qpy_mod_src_dir)

            sp_qpy_mod_src_dir = source_path(qpy_mod_src_dir)
            need_vpath = (sp_qpy_mod_src_dir != qpy_mod_src_dir)

            pro_lines = []

            pro_add_qt_dependencies(target_config, metadata, pro_lines)

            inc_path = []

            if need_vpath:
                inc_path.append(sp_qpy_mod_src_dir)

            if target_config.consolidate:
                inc_path.append('../../_qt')
            else:
                inc_path.append('../../%s' % mname)

            inc_path.append(target_config.py_inc_dir)

            if target_config.sip_inc_dir != target_config.py_inc_dir:
                inc_path.append(target_config.sip_inc_dir)

            pro_lines.append('INCLUDEPATH = %s' %
                    ' '.join([qmake_quote(i) for i in inc_path]))

            if need_vpath:
                pro_lines.append('VPATH = %s' % qmake_quote(sp_qpy_mod_src_dir))

            pro_lines.append('include(%s.pro)' %
                    os.path.join(sp_qpy_mod_src_dir, metadata.qpy_lib))

            qpy_pro_name = os.path.join(qpy_mod_src_dir,
                    'w_%s.pro' % metadata.qpy_lib)

            out_f = open_for_writing(qpy_pro_name)
            out_f.write('\n'.join(pro_lines))
            out_f.close()

            inform("Generating the Makefile for the QPy support library for %s..." % mname)
            run_qmake(target_config, verbose, qpy_pro_name)

        if mname == 'QtOpenGL':
            generate_OpenGL_extras(target_config, verbose)

        generate_sip_module_code(target_config, verbose, no_timestamp, parts,
                tracing, mname, sip_flags)
        subdirs.append(mname)

    # Generate the .pro file for the qpy libraries.
    inform("Generating the .pro file for the QPy support libraries...")

    qpy_pro_name = os.path.join(qpy_src_dir, 'qpy.pro')

    out_f = open_for_writing(qpy_pro_name)

    out_f.write("""TEMPLATE = subdirs
SUBDIRS = %s
""" % ' '.join(qpy_subdirs))

    out_f.close()

    # Generate the makefiles for the qpy libraries.
    inform("Generating the Makefile for the QPy support libraries...")
    run_qmake(target_config, verbose, qpy_pro_name)

    # Generate the composite module.
    qtmod_sipdir = os.path.join('sip', 'Qt')
    mk_clean_dir(qtmod_sipdir)

    qtmod_sipfile = os.path.join(qtmod_sipdir, 'Qtmod.sip')
    f = open_for_writing(qtmod_sipfile)

    f.write('''%CompositeModule PyQt4.Qt

''')

    for mname in target_config.modules:
        f.write('%%Include %s/%smod.sip\n' % (mname, mname))

    f.close()

    generate_sip_module_code(target_config, verbose, no_timestamp, parts,
            tracing, 'Qt', sip_flags)
    subdirs.append('Qt')

    # Generate the consolidated module if required.
    if target_config.consolidate:
        _qtmod_sipdir = os.path.join('sip', '_qt')
        mk_clean_dir(_qtmod_sipdir)

        _qtmod_sipfile = os.path.join(_qtmod_sipdir, '_qtmod.sip')
        f = open_for_writing(_qtmod_sipfile)

        f.write('''%ConsolidatedModule PyQt4._qt

''')

        for mname in target_config.modules:
            f.write('%%Include %s/%smod.sip\n' % (mname, mname))

        f.close()

        generate_sip_module_code(target_config, verbose, no_timestamp, parts,
                tracing, '_qt', sip_flags)
        subdirs.append('_qt')

    # Generate pylupdate4 and pyrcc4.
    for tool in ('pylupdate', 'pyrcc'):
        generate_application_makefile(target_config, verbose, tool)
        subdirs.append(tool)

    # Generate the pyuic4 wrapper.
    pyuic_wrapper = generate_pyuic4_wrapper(target_config)

    # Generate the Qt Designer plugin.
    if not target_config.no_designer_plugin and 'QtDesigner' in target_config.modules:
        if generate_designer_plugin_makefile(target_config, verbose):
            subdirs.append('designer')

    # Generate the QScintilla API file.
    if target_config.qsci_api:
        inform("Generating the QScintilla API file...")
        f = open_for_writing('PyQt4.api')

        for mname in target_config.modules:
            api = open(mname + '.api')

            for l in api:
                f.write('PyQt4.' + l)

            api.close()
            os.remove(mname + '.api')

        f.close()

    # Generate the Python dbus module.
    if target_config.pydbus_module_dir != '':
        mname = 'dbus'

        mk_dir(mname)
        sp_src_dir = source_path(mname)

        includepath = ' '.join(target_config.dbus_inc_dirs)

        lib_dirs = ['-L' + l for l in target_config.dbus_lib_dirs]
        lib_names = ['-l' + l for l in target_config.dbus_libs]
        libs = ' '.join(lib_dirs + lib_names)

        generate_module_makefile(target_config, verbose, mname,
                includepath=includepath, libs=libs,
                install_path=target_config.pydbus_module_dir,
                src_dir=sp_src_dir)

        subdirs.append(mname)

    # Generate the top-level .pro file.
    inform("Generating the top-level .pro file...")
    out_f = open_for_writing(toplevel_pro)

    out_f.write('''TEMPLATE = subdirs
CONFIG += ordered
SUBDIRS = %s

init_py.files = %s
init_py.path = %s/PyQt4
INSTALLS += init_py
''' % (' '.join(subdirs), source_path('__init__.py'), target_config.module_dir))

    # Install the uic module and the pyuic4 wrapper.
    out_f.write('''
uic_package.files = %s
uic_package.path = %s/PyQt4
INSTALLS += uic_package
''' % (source_path('pyuic', 'uic'), target_config.module_dir))

    out_f.write('''
pyuic4.files = %s
pyuic4.path = %s
INSTALLS += pyuic4
''' % (pyuic_wrapper, target_config.bin_dir))

    # Install the QScintilla .api file.
    if target_config.qsci_api:
        out_f.write('''
qscintilla_api.files = PyQt4.api
qscintilla_api.path = %s/api/python
INSTALLS += qscintilla_api
''' % target_config.qsci_api_dir)

    # Install ElementTree if the version of Python doesn't have it.
    if target_config.py_version < 0x020500:
        out_f.write('''
elementtree.files = %s
elementtree.path = %s/PyQt4
INSTALLS += elementtree
''' % (source_path('elementtree'), target_config.module_dir))

    out_f.close()

    # Make the pyuic4 wrapper executable on platforms that support it.  This
    # means that qmake will try and strip it after installing it resulting in
    # an (ignored) error.  However if we did it after running qmake then (on
    # Linux) the execute bits would be stripped on installation.
    if target_config.py_platform != 'win32':
        inform("Making the %s wrapper executable..." % pyuic_wrapper)

        sbuf = os.stat(pyuic_wrapper)
        mode = sbuf.st_mode
        mode |= (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        os.chmod(pyuic_wrapper, mode)

    # Generate the top-level makefile.
    inform("Generating the top-level Makefile...")
    run_qmake(target_config, verbose, toplevel_pro)


def generate_designer_plugin_makefile(target_config, verbose):
    """ Generate the makefile for the Qt Designer plugin.  target_config is the
    target configuration.  verbose is set if the output is to be displayed.
    Returns True if the makefile could be generated.
    """

    if sys.platform == 'win32':
        link, pysh_lib = get_win32_python_library(target_config)
    else:
        py_major, py_minor = get_py_major_minor(target_config)

        # Use distutils to get the additional configuration.
        from distutils.sysconfig import get_config_vars
        ducfg = get_config_vars()

        config_args = ducfg.get('CONFIG_ARGS', '')

        if target_config.py_platform == 'darwin':
            dynamic_pylib = '--enable-framework' in config_args

            # It's probably a Python bug that the library name doesn't
            # include the ABI information.
            abi = ''
        else:
            dynamic_pylib = '--enable-shared' in config_args
            abi = getattr(sys, 'abiflags', '')

        if not dynamic_pylib:
            inform("The Qt Designer plugin was disabled because the Python library is static.")
            return False

        if glob.glob('%s/lib/libpython%d.%d*' % (ducfg['exec_prefix'], py_major, py_minor)):
            lib_dir_flag = qmake_quote('-L%s/lib' % ducfg['exec_prefix'])
        elif 'MULTIARCH' in ducfg and glob.glob('%s/lib/%s/libpython%d.%d*' % (ducfg['exec_prefix'], ducfg['MULTIARCH'], py_major, py_minor)):
            lib_dir_flag = qmake_quote('-L%s/lib/%s' % (ducfg['exec_prefix'], ducfg['MULTIARCH']))
        elif glob.glob('%s/libpython%d.%d*' % (ducfg['LIBDIR'], py_major, py_minor)):
            lib_dir_flag = qmake_quote('-L%s' % ducfg['LIBDIR'])
        else:
            inform("The Qt Designer plugin was disabled because the Python library couldn't be found.")
            return False

        link = '%s -lpython%d.%d%s' % (lib_dir_flag, py_major, py_minor, abi)

        pysh_lib = ducfg.get('LDLIBRARY', '')

    # Create the qmake project file.
    inform("Generating the Qt Designer plugin .pro file...")

    designer_dir = 'designer'
    sp_designer_dir = source_path(designer_dir)

    fin = open(os.path.join(sp_designer_dir, 'python.pro-in'))
    prj = fin.read()
    fin.close()

    prj = prj.replace('@PYINCDIR@', quote(target_config.py_inc_dir))
    prj = prj.replace('@PYLINK@', link)
    prj = prj.replace('@PYSHLIB@', pysh_lib)
    prj = prj.replace('@QTPLUGINDIR@',
            quote(target_config.designer_plugin_dir))

    pro_name = os.path.join(designer_dir, 'python.pro')

    mk_dir(designer_dir)
    fout = open_for_writing(pro_name)
    fout.write(prj)

    if sp_designer_dir != designer_dir:
        fout.write('''
INCLUDEPATH += %s
VPATH = %s
''' % (qmake_quote(sp_designer_dir), qmake_quote(sp_designer_dir)))

    fout.close()

    # Create the makefile.
    inform("Generating the Qt Designer plugin Makefile...")

    run_qmake(target_config, verbose, pro_name)

    return True


def generate_application_makefile(target_config, verbose, src_dir):
    """ Create the makefile for a QtXml based application.  target_config is
    the target configuration.  verbose is set if the output is to be displayed.
    src_dir is the name of the directory containing the source files.
    """

    mk_dir(src_dir)
    sp_src_dir = source_path(src_dir)

    # The standard naming convention.
    app = src_dir + '4'

    inform("Generating the .pro file for %s..." % app)

    pro_lines = ['TEMPLATE = app', 'QT -= gui', 'QT += xml']
    pro_lines.append(
            'CONFIG += warn_on %s' %
                    ('debug' if target_config.debug else 'release'))

    if target_config.py_platform == 'win32':
        pro_lines.append('CONFIG += console')
    elif target_config.py_platform == 'darwin':
        pro_lines.append('CONFIG -= app_bundle')

    pro_lines.append('target.path = %s' % target_config.bin_dir)
    pro_lines.append('INSTALLS += target')

    if sp_src_dir != src_dir:
        pro_lines.append('INCLUDEPATH += %s' % qmake_quote(sp_src_dir))
        pro_lines.append('VPATH = %s' % qmake_quote(sp_src_dir))

    pro_lines.extend(pro_sources(sp_src_dir))

    pro_name = os.path.join(src_dir, app + '.pro')

    pro = open_for_writing(pro_name)
    pro.write('\n'.join(pro_lines))
    pro.close()

    inform("Generating the Makefile for %s..." % app)
    run_qmake(target_config, verbose, pro_name)


def pro_sources(src_dir):
    """ Return the HEADERS and SOURCES variables for a .pro file by
    introspecting a directory.  src_dir is the name of the directory.
    """

    pro_lines = []

    headers = [os.path.basename(f) for f in glob.glob('%s/*.h' % src_dir)]
    if len(headers) != 0:
        pro_lines.append('HEADERS = %s' % ' '.join(headers))

    c_sources = [os.path.basename(f) for f in glob.glob('%s/*.c' % src_dir)]
    cpp_sources = [os.path.basename(f) for f in glob.glob('%s/*.cpp' % src_dir)]
    pro_lines.append('SOURCES = %s' % ' '.join(c_sources + cpp_sources))

    return pro_lines


def generate_pyuic4_wrapper(target_config):
    """ Create a platform dependent executable wrapper for the pyuic.py script.
    target_config is the target configuration.  Returns the platform specific
    name of the wrapper.
    """

    wrapper = 'pyuic4.bat' if target_config.py_platform == 'win32' else 'pyuic4'

    inform("Generating the %s wrapper..." % wrapper)

    exe = quote(target_config.pyuic_interpreter)
    script = quote(
            os.path.join(target_config.module_dir, 'PyQt4', 'uic', 'pyuic.py'))

    wf = open_for_writing(wrapper)

    if target_config.py_platform == 'win32':
        wf.write('@%s %s %%1 %%2 %%3 %%4 %%5 %%6 %%7 %%8 %%9\n' % (exe, script))
    else:
        wf.write('#!/bin/sh\n')
        wf.write('exec %s %s ${1+"$@"}\n' % (exe, script))

    wf.close()

    return wrapper


def quote(path):
    """ Return a path with quotes added if it contains spaces.  path is the
    path.
    """

    if ' ' in path:
        path = '"%s"' % path

    return path


def qmake_quote(path):
    """ Return a path with quoted for qmake if it contains spaces.  path is the
    path.
    """

    if ' ' in path:
        path = '$$quote(%s)' % path

    return path


def inform_user(target_config, sip_version):
    """ Tell the user the values that are going to be used.  target_config is
    the target configuration.  sip_version is the SIP version string.
    """

    inform("Qt v%s (%s) is being used." % (version_to_string(target_config.qt_version), "Open Source" if target_config.qt_licensee == '' else "Commercial"))
    inform("The qmake executable is %s." % target_config.qmake)

    if target_config.qt_licensee:
        inform("Qt is licensed to %s." % target_config.qt_licensee)


    if target_config.qt_framework:
        inform("Qt is built as a framework.")
    else:
        inform(
                "Qt is built as a %s library." %
                        "shared" if target_config.qt_shared else "static")

    inform("SIP %s is being used." % sip_version)
    inform("The sip executable is %s." % target_config.sip)
    inform("These PyQt4 modules will be built: %s." % ', '.join(target_config.modules))
    inform("The PyQt4 Python package will be installed in %s." % target_config.module_dir)

    if target_config.qt_version >= 0x050000:
        if target_config.no_deprecated:
            inform("PyQt4 is being built without deprecated Qt v4 features.")
        else:
            inform("PyQt4 is being built with deprecated Qt v4 features.")

    if target_config.no_docstrings:
        inform("PyQt4 is being built without generated docstrings.")
    else:
        inform("PyQt4 is being built with generated docstrings.")

    if target_config.prot_is_public:
        inform("PyQt4 is being built with 'protected' redefined as 'public'.")

    if target_config.no_designer_plugin:
        inform("The Designer plugin will not be installed.")
    else:
        inform("The Designer plugin will be installed in %s." %
                target_config.designer_plugin_dir)

    if target_config.qsci_api:
        inform(
                "The QScintilla API file will be installed in %s." %
                        os.path.join(
                                target_config.qsci_api_dir, 'api', 'python'))

    if target_config.pydbus_module_dir:
        inform(
                "The dbus support module will be installed in %s." %
                        target_config.pydbus_module_dir)

    inform("The PyQt4 .sip files will be installed in %s." %
            target_config.sip_dir)

    inform("pyuic4, pyrcc4 and pylupdate4 will be installed in %s." %
            target_config.bin_dir)

    inform("The interpreter used by pyuic4 is %s." %
            target_config.pyuic_interpreter)

    if target_config.vend_enabled:
        inform("PyQt4 will only be usable with signed interpreters.")


def run_qmake(target_config, verbose, pro_name, makefile_name='', fatal=True):
    """ Run qmake against a .pro file.  target_config is the target
    configuration.  verbose is set if the output is to be displayed.  pro_name
    is the name of the .pro file.  makefile_name is the name of the makefile
    to generate (and defaults to Makefile).  fatal is set if a qmake failure is
    considered a fatal error, otherwise False is returned if qmake fails.
    """

    # qmake doesn't behave consistently if it is not run from the directory
    # containing the .pro file - so make sure it is.
    pro_dir, pro_file = os.path.split(pro_name)
    if pro_dir != '':
        cwd = os.getcwd()
        os.chdir(pro_dir)
    else:
        cwd = None

    mf = makefile_name if makefile_name != '' else 'Makefile'

    remove_file(mf)

    args = [quote(target_config.qmake)]

    if target_config.qmake_spec != '':
        args.append('-spec')
        args.append(target_config.qmake_spec)

    if makefile_name != '':
        args.append('-o')
        args.append(makefile_name)

    args.append(pro_file)

    run_command(' '.join(args), verbose)

    if not os.access(mf, os.F_OK):
        if fatal:
            error(
                    "%s failed to create a makefile from %s." %
                            (target_config.qmake, pro_name))

        return False

    # Restore the current directory.
    if cwd is not None:
        os.chdir(cwd)

    return True


def run_make(target_config, verbose, exe, makefile_name):
    """ Run make against a makefile to create an executable.  target_config is
    the target configuration.  verbose is set if the output is to be displayed.
    exe is the platform independent name of the executable that will be
    created.  makefile_name is the name of the makefile.  Returns the platform
    specific name of the executable, or None if an executable wasn't created.
    """

    # Guess the name of make and set the default target and platform specific
    # name of the executable.
    if target_config.py_platform == 'win32':
        if target_config.qmake_spec == 'win32-borland':
            make = 'bmake'
        elif target_config.qmake_spec == 'win32-g++':
            make = 'mingw32-make'
        else:
            make = 'nmake'

        if target_config.debug:
            makefile_target = 'debug'
            platform_exe = os.path.join('debug', exe + '.exe')
        else:
            makefile_target = 'release'
            platform_exe = os.path.join('release', exe + '.exe')
    else:
        make = 'make'
        makefile_target = ''

        if target_config.py_platform == 'darwin':
            platform_exe = os.path.join(exe + '.app', 'Contents', 'MacOS', exe)
        else:
            platform_exe = os.path.join('.', exe)

    remove_file(platform_exe)

    args = [make, '-f', makefile_name]

    if makefile_target != '':
        args.append(makefile_target)

    run_command(' '.join(args), verbose)

    return platform_exe if os.access(platform_exe, os.X_OK) else None


def run_command(cmd, verbose):
    """ Run a command and display the output if requested.  cmd is the command
    to run.  verbose is set if the output is to be displayed.
    """

    if verbose:
        sys.stdout.write(cmd + "\n")

    fout = get_command_output(cmd, and_stderr=True)

    # Read stdout and stderr until there is no more output.
    lout = fout.readline()
    while lout:
        if verbose:
            if sys.hexversion >= 0x03000000:
                sys.stdout.write(str(lout, encoding=sys.stdout.encoding))
            else:
                sys.stdout.write(lout)

        lout = fout.readline()

    fout.close()

    try:
        os.wait()
    except:
        pass


def remove_file(fname):
    """ Remove a file which may or may not exist.  fname is the name of the
    file.
    """

    try:
        os.remove(fname)
    except OSError:
        pass


def generate_OpenGL_extras(target_config, verbose):
    """ Generate the extras needed by the QtOpenGL module (i.e. the .sip file
    defining the correct typedefs for the OpenGL data types.  target_config is
    the target configuration.  verbose is set of the output is to be displayed.
    """

    inform("Determining the OpenGL data types...")

    source = '''#include <QFile>
#include <QTextStream>
#include <qgl.h>

int main(int, char **)
{
    QFile outf("./sip/QtOpenGL/opengl_types.sip");

    if (!outf.open(QIODevice::WriteOnly|QIODevice::Truncate|QIODevice::Text))
        return 1;

    QTextStream out(&outf);

    if (sizeof (long) == sizeof (GLint))
        out << "typedef long GLint;\\n";
    else
        out << "typedef int GLint;\\n";

    if (sizeof (unsigned long) == sizeof (GLuint))
        out << "typedef unsigned long GLuint;\\n";
    else
        out << "typedef unsigned GLuint;\\n";

    if (sizeof (unsigned long) == sizeof (GLenum))
        out << "typedef unsigned long GLenum;\\n";
    else
        out << "typedef unsigned GLenum;\\n";

    if (sizeof (unsigned long) == sizeof (GLbitfield))
        out << "typedef unsigned long GLbitfield;\\n";
    else
        out << "typedef unsigned GLbitfield;\\n";

    out << "typedef float GLfloat;\\n";

    return 0;
}
'''

    cmd = compile_qt_program(target_config, verbose, 'opengl_extras', source,
            'QtOpenGL')
    if cmd is None:
        error("Unable to determine the OpenGL data types.")

    run_command(cmd, verbose)


def check_vendorid(target_config):
    """ See if the VendorID library and include file can be found.
    target_config is the target configuration.
    """

    if target_config.vend_enabled:
        if os.access(os.path.join(target_config.vend_inc_dir, 'vendorid.h'), os.F_OK):
            if glob.glob(os.path.join(target_config.vend_lib_dir, '*vendorid*')):
                inform("The VendorID package was found.")
            else:
                target_config.vend_enabled = False
                inform(
                        "The VendorID library could not be found in %s and so "
                        "signed interpreter checking will be disabled. If the "
                        "VendorID package is installed then use the "
                        "--vendorid-libdir argument to explicitly specify the "
                        "correct directory." % target_config.vend_lib_dir)
        else:
            target_config.vend_enabled = False
            inform(
                    "vendorid.h could not be found in %s and so signed "
                    "interpreter checking will be disabled. If the VendorID "
                    "package is installed then use the --vendorid-incdir "
                    "argument to explicitly specify the correct directory." %
                            target_config.vend_inc_dir)


def get_command_output(cmd, and_stderr=False):
    """ Return a pipe from which a command's output can be read.  cmd is the
    command.  and_stderr is set if the output should include stderr as well as
    stdout.
    """

    try:
        import subprocess
    except ImportError:
        if and_stderr:
            _, sout = os.popen4(cmd)
        else:
            _, sout, _ = os.popen3(cmd)

        return sout

    if and_stderr:
        stderr = subprocess.STDOUT
    else:
        stderr = subprocess.PIPE

    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=stderr)

    return p.stdout


def source_path(*names):
    """ Return the native path for a list of components rooted at the directory
    containing this script.  names is the sequence of component names.
    """

    path = [os.path.dirname(os.path.abspath(__file__))] + list(names)

    return os.path.join(*path)


def check_dbus(target_config, verbose):
    """ See if the DBus support module should be built and update the target
    configuration accordingly.  target_config is the target configuration.
    verbose is set if the output is to be displayed.
    """

    if not os.path.isdir(source_path('dbus')):
        return

    inform("Checking to see if the dbus support module should be built...")

    cmd = 'pkg-config --cflags-only-I --libs dbus-1'

    if verbose:
        sys.stdout.write(cmd + "\n")

    sout = get_command_output(cmd)
    iflags = sout.read().strip()

    if not iflags:
        inform("DBus v1 does not seem to be installed.")
        return

    if sys.hexversion >= 0x03000000:
        iflags = iflags.decode()

    for f in iflags.split():
        if f.startswith('-I'):
            target_config.dbus_inc_dirs.append(f[2:])
        elif f.startswith('-L'):
            target_config.dbus_lib_dirs.append(f[2:])
        elif f.startswith('-l'):
            target_config.dbus_libs.append(f[2:])

    try:
        import dbus.mainloop
    except:
        inform("The Python dbus module doesn't seem to be installed.")
        return

    target_config.pydbus_module_dir = dbus.mainloop.__path__[0]

    # Try and find dbus-python.h.  We don't use pkg-config because it is broken
    # for dbus-python (at least for versions up to and including v0.81.0).
    # Instead we look where DBus itself is installed - which in most cases will
    # be where dbus-python is also installed.
    if target_config.pydbus_inc_dir != '':
        dlist = [target_config.pydbus_inc_dir]
    else:
        dlist = target_config.dbus_inc_dirs

    for d in dlist:
        if os.access(os.path.join(d, 'dbus', 'dbus-python.h'), os.F_OK):
            if d not in target_config.dbus_inc_dirs:
                target_config.dbus_inc_dirs.append(d)

            break
    else:
        inform(
                "dbus/dbus-python.h could not be found and so the DBus "
                "support module will be disabled. If dbus-python v0.80 or "
                "later is installed then use the --dbus argument to "
                "explicitly specify the directory containing "
                "dbus/dbus-python.h.")
        target_config.pydbus_module_dir = ''


def check_module(target_config, verbose, mname, incfile, test):
    """ See if a module can be built and, if so, add it to the target
    configurations list of modules.  target_config is the target configuration.
    verbose is set if the output is to be displayed.  mname is the name of the
    module.  incfile is the name of the include file needed for the test.  test
    is a C++ statement being used for the test.
    """

    # Check the module's main .sip file exists.
    if not os.access(source_path('sip', mname, mname + 'mod.sip'), os.F_OK):
        return

    inform("Checking to see if the %s module should be built..." % mname)

    source = '''#include <%s>

int main(int, char **)
{
    %s;
}
''' % (incfile, test)

    if compile_qt_program(target_config, verbose, 'cfgtest_' + mname, source, mname) is not None:
        target_config.modules.append(mname)


def compile_qt_program(target_config, verbose, name, source, mname):
    """ Compile the source of a Qt program and return the name of the
    executable or None if it couldn't be created.  target_config is the target
    configuration.  verbose is set if the output is to be displayed.  name is
    the root name of the program from which all program-specific file names
    will be derived.  source is the C++ source of the program.  mname is the
    name of the Qt module that the program uses.
    """

    metadata = get_module_metadata(target_config, mname)

    # The derived file names.
    name_pro = name + '.pro'
    name_makefile = name + '.mk'
    name_source = name + '.cpp'

    # Create the .pro file.
    pro_lines = []
    pro_add_qt_dependencies(target_config, metadata, pro_lines)
    pro_lines.append('TARGET = %s' % name)
    pro_lines.append('SOURCES = %s' % name_source)

    f = open_for_writing(name_pro)
    f.write('\n'.join(pro_lines))
    f.close()

    # Create the source file.
    f = open_for_writing(name_source)
    f.write(source)
    f.close()

    if not run_qmake(target_config, verbose, name_pro, name_makefile, fatal=False):
        return None

    return run_make(target_config, verbose, name, name_makefile)


def pro_add_qt_dependencies(target_config, metadata, pro_lines):
    """ Add the Qt dependencies of a module to a .pro file.  target_config is
    the target configuration.  metadata is the module's meta-data.  pro_lines
    is the list of lines making up the .pro file that is updated.
    """

    add = []
    remove = []
    for qt in metadata.qmake_QT:
        if qt.startswith('-'):
            remove.append(qt[1:])
        else:
            add.append(qt)

    if len(remove) != 0:
        pro_lines.append('QT -= %s' % ' '.join(remove))

    if len(add) != 0:
        pro_lines.append('QT += %s' % ' '.join(add))

    if metadata.qmake_CONFIG != '':
        pro_lines.append('CONFIG += %s' % metadata.qmake_CONFIG)

    pro_lines.append(
            'CONFIG += %s' % ('debug' if target_config.debug else 'release'))

    if metadata.qmake_LIBS != '':
        pro_lines.append('LIBS += %s' % metadata.qmake_LIBS)

    pro_lines.extend(target_config.qmake_variables)


def get_sip_flags(target_config):
    """ Return the SIP platform, version and feature flags.  target_config is
    the target configuration.
    """

    sip_flags = []

    # If we don't check for signed interpreters, we exclude the 'VendorID'
    # feature
    if not target_config.vend_enabled:
        sip_flags.append('-x')
        sip_flags.append('VendorID')

    if target_config.qt_version >= 0x050000 and target_config.no_deprecated:
        sip_flags.append('-x')
        sip_flags.append('PyQt_Deprecated_5_0')

    # Handle the platform tag.
    if target_config.py_platform == 'win32':
        plattag = 'WS_WIN'
    elif target_config.py_platform == 'darwin':
        plattag = 'WS_MACX'
    else:
        plattag = 'WS_X11'

    sip_flags.append('-t')
    sip_flags.append(plattag)

    # Handle the Qt version tag.
    verstag = version_to_sip_tag(target_config.qt_version)

    if verstag:
        sip_flags.append('-t')
        sip_flags.append(verstag)

    # Handle any feature flags.
    for xf in target_config.qt_disabled_features:
        sip_flags.append('-x')
        sip_flags.append(xf)

    # Handle the version specific Python features.
    if target_config.py_version < 0x020400:
        sip_flags.append('-x')
        sip_flags.append('Py_DateTime')

    if target_config.py_version < 0x030000:
        sip_flags.append('-x')
        sip_flags.append('Py_v3')

    return ' '.join(sip_flags)


def mk_clean_dir(name):
    """ Create a clean (ie. empty) directory.  name is the name of the
    directory.
    """

    try:
        shutil.rmtree(name)
    except:
        pass

    try:
        os.makedirs(name)
    except:
        error("Unable to create the %s directory." % name)


def mk_dir(name):
    """ Ensure a directory exists, creating it if necessary.  name is the name
    of the directory.
    """

    try:
        os.makedirs(name)
    except:
        pass


def generate_sip_module_code(target_config, verbose, no_timestamp, parts, tracing, mname, sip_flags):
    """ Generate the code for a module.  target_config is the target
    configuration.  verbose is set if the output is to be displayed.
    no_timestamp is set if the .sip files should exclude the timestamp.  parts
    is the number of parts the generated code should be split into.  tracing is
    set if the generated code should include tracing calls.  mname is the name
    of the module to generate the code for.  sip_flags is the string of flags
    to pass to sip.
    """

    inform("Generating the C++ source for the %s module..." % mname)

    mk_clean_dir(mname)

    # Build the SIP command line.
    argv = [quote(target_config.sip), '-w', sip_flags]

    if no_timestamp:
        argv.append('-T')

    if not target_config.no_docstrings:
        argv.append('-o');

    if target_config.prot_is_public:
        argv.append('-P');

    # Work out how SIP is supposed to handle the consolidated module and its
    # components.
    if target_config.consolidate and mname != 'Qt':
        argv.append('-p')
        argv.append('PyQt4._qt')

    if parts != 0:
        argv.append('-j')
        argv.append(str(parts))

    if tracing:
        argv.append('-r')

    if mname not in ('Qt', '_qt'):
        argv.append('-a')
        argv.append(mname + '.api')

    # There is an issue creating QObjects while the GIL is held causing
    # deadlocks in multi-threaded applications.  We don't fully understand this
    # yet so we make sure we avoid the problem by always releasing the GIL.
    argv.append('-g')

    # Pass the absolute pathname so that #line files are absolute.
    argv.append('-c')
    argv.append(os.path.abspath(mname))

    argv.append('-I')
    argv.append('sip')

    sp_sip_dir = source_path('sip')
    if sp_sip_dir != 'sip':
        # SIP assumes POSIX style separators.
        sp_sip_dir = sp_sip_dir.replace(os.pathsep, '/')
        argv.append('-I')
        argv.append(sp_sip_dir)

    # The .sip files for the Qt modules will be in the out-of-tree directory.
    if mname in ('Qt', '_qt'):
        sip_dir = 'sip'
    else:
        sip_dir = sp_sip_dir

    # Add the name of the .sip file.
    argv.append('%s/%s/%smod.sip' % (sip_dir, mname, mname))

    run_command(' '.join(argv), verbose)

    # Check the result.
    if mname == '_qt':
        file_check = 'sip_qtcmodule.cpp'
    elif mname == 'Qt' or target_config.consolidate:
        file_check = 'sip%scmodule.c' % mname
    else:
        file_check = 'sipAPI%s.h' % mname

    if not os.access(os.path.join(mname, file_check), os.F_OK):
        error("Unable to create the C++ code.")

    # Generate the makefile.
    includepath = libs = ''
    if target_config.vend_enabled:
        m = '_qt' if target_config.consolidate else 'QtCore'

        if mname == m:
            includepath = target_config.vend_inc_dir
            libs = '-L%s -lvendorid' % target_config.vend_lib_dir

    generate_module_makefile(target_config, verbose, mname,
            includepath=includepath, libs=libs)


def generate_module_makefile(target_config, verbose, mname, includepath='', libs='', install_path='', src_dir=''):
    """ Generate the makefile for a module.  target_config is the target
    configuration.  verbose is set if the output is to be displayed.  mname is
    the name of the module.  includepath is an optional additional value of
    INCLUDEPATH.  libs is an optional additional value of LIBS.  install_path
    is the optional name of the directory that the module will be installed in.
    src_dir is the optional source directory (by default the sources are
    assumed to be in the module directory).
    """

    inform("Generating the .pro file for the %s module..." % mname)

    if src_dir == '':
        src_dir = mname

    target_name = mname

    if mname != '_qt':
        metadata = get_module_metadata(target_config, mname)

        if metadata.qmake_TARGET != '':
            target_name = metadata.qmake_TARGET

    pro_lines = ['TEMPLATE = lib']

    pro_lines.append('CONFIG += warn_on %s' % ('staticlib' if target_config.static else 'plugin'))

    if mname != '_qt':
        pro_add_qt_dependencies(target_config, metadata, pro_lines)
    else:
        # Merge the component module's details.  We assume core and gui will be
        # needed.
        add = []
        config = ['debug' if target_config.debug else 'release']
        cons_libs = []

        for dep_mname in target_config.modules:
            dep_metadata = get_module_metadata(target_config, dep_mname)
            if dep_metadata.in_consolidated:
                for qt in dep_metadata.qmake_QT:
                    if not qt.startswith('-') and qt not in add:
                        add.append(qt)

                dep_config = dep_metadata.qmake_CONFIG
                if dep_config != '' and dep_config not in config:
                    config.append(dep_config)

                dep_libs = dep_metadata.qmake_LIBS
                if dep_libs != '' and dep_libs not in cons_libs:
                    cons_libs.append(dep_libs)

        if len(add) != 0:
            pro_lines.append('QT += %s' % ' '.join(add))

        pro_lines.append('CONFIG += %s' % ' '.join(config))

        if len(cons_libs) != 0:
            pro_lines.append('LIBS += %s' % ' '.join(cons_libs))

        pro_lines.extend(target_config.qmake_variables)

    if not target_config.static:
        debug_suffix = get_win32_debug_suffix(target_config)
        link, _ = get_win32_python_library(target_config)

        shared = '''
win32 {
    PY_MODULE = %s%s.pyd
    target.files = %s%s.pyd
    LIBS += %s
} else {
    PY_MODULE = %s.so
    target.files = %s.so
}
''' % (target_name, debug_suffix, target_name, debug_suffix, link, target_name, target_name)

        pro_lines.extend(shared.split('\n'))

        # Without the 'no_check_exist' magic the target.files must exist when
        # qmake is run otherwise the install and uninstall targets are not
        # generated.
        pro_lines.append('target.CONFIG = no_check_exist')

    if install_path == '':
        install_path = target_config.module_dir + '/PyQt4'

    pro_lines.append('target.path = %s' % install_path)
    pro_lines.append('INSTALLS += target')

    sip_files = glob.glob(source_path('sip', mname, '*.sip'))
    if len(sip_files) != 0:
        pro_lines.append('sip.path = %s/%s' % (target_config.sip_dir, mname))
        pro_lines.append('sip.files = %s' % ' '.join(sip_files))
        pro_lines.append('INSTALLS += sip')

    if 'g++' in target_config.qmake_spec or 'clang' in target_config.qmake_spec:
        pro_lines.append('QMAKE_CXXFLAGS += -fno-exceptions')

    # This optimisation could apply to other platforms.
    if 'linux' in target_config.qmake_spec and not target_config.static:
        if target_config.py_version >= 0x030000:
            entry_point = 'PyInit_%s' % mname
        else:
            entry_point = 'init%s' % mname

        exp = open_for_writing(os.path.join(mname, target_name + '.exp'))
        exp.write('{ global: %s; local: *; };' % entry_point)
        exp.close()

        pro_lines.append('QMAKE_LFLAGS += -Wl,--version-script=%s.exp' % target_name)

    if target_config.qt_version >= 0x050000 and not target_config.no_deprecated:
        # The name of this macro is very confusing.
        pro_lines.append('DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x040900')

    if target_config.prot_is_public:
        pro_lines.append('DEFINES += SIP_PROTECTED_IS_PUBLIC protected=public')

    pro_lines.append('INCLUDEPATH += %s' % target_config.py_inc_dir)
    if target_config.py_inc_dir != target_config.sip_inc_dir:
        pro_lines.append('INCLUDEPATH += %s' % target_config.sip_inc_dir)

    if mname != '_qt':
        pro_add_qpy(target_config, mname, metadata, pro_lines)
    else:
        for dep_mname in target_config.modules:
            dep_metadata = get_module_metadata(target_config, dep_mname)
            if dep_metadata.in_consolidated:
                pro_add_qpy(target_config, dep_mname, dep_metadata, pro_lines)

    if includepath != '':
        pro_lines.append('INCLUDEPATH += %s' % includepath)

    if libs != '':
        pro_lines.append('LIBS += %s' % libs)

    if not target_config.static:
        shared = '''
win32 {
    QMAKE_POST_LINK = $(COPY_FILE) $(DESTDIR_TARGET) $$PY_MODULE
} else {
    QMAKE_POST_LINK = $(COPY_FILE) $(TARGET) $$PY_MODULE
}
macx {
    QMAKE_LFLAGS += "-undefined dynamic_lookup"
}
'''

        pro_lines.extend(shared.split('\n'))

    pro_lines.append('TARGET = %s' % target_name)

    if src_dir != mname:
        pro_lines.append('INCLUDEPATH += %s' % quote(src_dir))
        pro_lines.append('VPATH = %s' % quote(src_dir))

    pro_lines.extend(pro_sources(src_dir))

    pro_name = os.path.join(mname, mname + '.pro')

    pro = open_for_writing(pro_name)
    pro.write('\n'.join(pro_lines))
    pro.close()

    inform("Generating the Makefile for the %s module..." % target_name)
    run_qmake(target_config, verbose, pro_name)


def pro_add_qpy(target_config, mname, metadata, pro_lines):
    """ Add the qpy dependencies of a module to a .pro file.  target_config is
    the target configuration.  mname is the module's name.  metadata is the
    module's meta-data.  pro_lines is the list of lines making up the .pro file
    that is updated.
    """ 

    if metadata.qpy_lib != '':
        pro_lines.append('INCLUDEPATH += %s' %
                qmake_quote(source_path('qpy', mname)))

        if target_config.py_platform == 'win32':
            dir_suffix = '/' + ('debug' if target_config.debug else 'release')
        else:
            dir_suffix = ''

        pro_lines.append('LIBS += -L../qpy/%s%s -l%s' %
                (mname, dir_suffix, metadata.qpy_lib))


def fix_license(src_lfile, dst_lfile):
    """ Fix the license file, if there is one, so that it conforms to the SIP
    v5 syntax.  src_lfile is the name of the license file.  dst_lfile is the
    name of the fixed license file.
    """

    f = open(src_lfile)
    f5 = open_for_writing(dst_lfile)

    for line in f:
        if line.startswith('%License'):
            anno_start = line.find('/')
            anno_end = line.rfind('/')

            if anno_start < 0 or anno_end < 0 or anno_start == anno_end:
                error("%s has missing annotations." % name)

            annos = line[anno_start + 1:anno_end].split(', ')
            annos5 = [anno[0].lower() + anno[1:] for anno in annos]

            f5.write('%License(')
            f5.write(', '.join(annos5))
            f5.write(')\n')
        else:
            f5.write(line)

    f5.close()
    f.close()


def check_license(target_config, license_confirmed):
    """ Handle the validation of the PyQt4 license.  target_config is the
    target configuration.  license_confirmed is set if the user has already
    accepted the license.
    """

    try:
        import license
        ltype = license.LicenseType
        lname = license.LicenseName

        try:
            lfile = license.LicenseFile
        except AttributeError:
            lfile = None
    except ImportError:
        ltype = None

    if ltype is None:
        ltype = "GPL"
        lname = "GNU General Public License"
        lfile = 'pyqt-gpl.sip'

    inform(
            "This is the %s version of PyQt %s (licensed under the %s) for "
            "Python %s on %s." %
                    (ltype, PYQT_VERSION_STR, lname, sys.version.split()[0],
                            sys.platform))

    # Common checks.
    if target_config.qt_licensee != '' and ltype == 'GPL':
        error(
                "This version of PyQt4 and the commercial version of Qt have "
                "incompatible licenses.")

    # Confirm the license if not already done.
    if not license_confirmed:
        if ltype == "GPL":
            loptions = """
Type '2' to view the GPL v2 license.
Type '3' to view the GPL v3 license.
"""
        else:
            loptions = """
Type 'L' to view the license.
"""

        sys.stdout.write(loptions)
        sys.stdout.write("""Type 'yes' to accept the terms of the license.
Type 'no' to decline the terms of the license.

""")

        while 1:
            sys.stdout.write("Do you accept the terms of the license? ")
            sys.stdout.flush()

            try:
                resp = sys.stdin.readline()
            except KeyboardInterrupt:
                raise SystemExit
            except:
                resp = ""

            resp = resp.strip().lower()

            if resp == "yes":
                break

            if resp == "no":
                sys.exit(0)

            if ltype == "GPL":
                if resp == '2':
                    os.system('more LICENSE.GPL2')
                elif resp == '3':
                    os.system('more LICENSE.GPL3')
            else:
                if resp == 'l':
                    os.system('more LICENSE')

    # Check that the license file exists and fix its syntax.
    sip_dir = 'sip'
    mk_dir(sip_dir)

    sp_sip_dir = source_path(sip_dir)
    src_lfile = os.path.join(sp_sip_dir, lfile)

    if os.access(src_lfile, os.F_OK):
        inform("Found the license file %s." % lfile)
        fix_license(src_lfile, os.path.join(sip_dir, lfile + '5'))
    else:
        error("Please copy the license file %s to %s." % (lfile, sp_sip_dir))


def check_qt(target_config):
    """ Check the Qt installation.  target_config is the target configuration.
    """

    # Starting with v4.7, Qt (when built with MinGW) assumes that stack frames
    # are 16 byte aligned because it uses SSE.  However the Python Windows
    # installers are built with 4 byte aligned stack frames.  We therefore need
    # to tweak the g++ flags to deal with it.
    if target_config.qmake_spec == 'win32-g++' and target_config.qt_version >= 0x040700:
        target_config.qmake_variables.append('QMAKE_CFLAGS += -mstackrealign')
        target_config.qmake_variables.append('QMAKE_CXXFLAGS += -mstackrealign')


def check_sip(target_config):
    """ Check that the version of sip is good enough and return its version.
    target_config is the target configuration.
    """

    if target_config.sip is None:
        error(
                "Make sure you have a working sip on your PATH or use the "
                "--sip argument to explicitly specify a working sip.")

    pipe = os.popen(' '.join([target_config.sip, '-V']))

    for l in pipe:
        version_str = l.strip()
        break
    else:
        error("'%s -V' did not generate any output." % target_config.sip)

    pipe.close()

    if 'snapshot' not in version_str:
        version = version_from_string(version_str)
        if version is None:
            error(
                    "'%s -V' generated unexpected output: '%s'." % (
                            target_config.sip, version_str))

        min_version = version_from_string(SIP_MIN_VERSION)
        if version < min_version:
            error(
                    "This version of PyQt4 requires sip %s or later." %
                            SIP_MIN_VERSION)

    return version_str


def version_from_string(version_str):
    """ Convert a version string of the form m.n or m.n.o to an encoded version
    number (or None if it was an invalid format).  version_str is the version
    string.
    """

    parts = version_str.split('.')
    if not isinstance(parts, list):
        return None

    if len(parts) == 2:
        parts.append('0')

    if len(parts) != 3:
        return None

    version = 0

    for part in parts:
        try:
            v = int(part)
        except ValueError:
            return None

        version = (version << 8) + v

    return version


def open_for_writing(fname):
    """ Return a file opened for writing while handling the most common problem
    of not having write permission on the directory.  fname is the name of the
    file to open.
    """
    try:
        return open(fname, 'w')
    except IOError:
        error(
                "There was an error creating %s.  Make sure you have write "
                "permission on the parent directory." % fname)


def get_win32_python_library(target_config):
    """ Return a tuple of the qmake LIBS flags to link against the Python
    library on Windows, and the name of the DLL itself.  target_config is the
    target configuration.
    """

    lib_dir = qmake_quote('-L%s' % target_config.py_lib_dir)
    py_major, py_minor = get_py_major_minor(target_config)
    debug_suffix = get_win32_debug_suffix(target_config)

    link = '%s -lpython%d%d%s' % (lib_dir, py_major, py_minor, debug_suffix)
    pysh_lib = 'python%d%d%s.dll' % (py_major, py_minor, debug_suffix)

    return link, pysh_lib


def get_win32_debug_suffix(target_config):
    """ Return the debug-dependent suffix appended to the name of Windows
    libraries.  target_config is the target configuration.
    """

    return '_d' if target_config.debug else ''


def get_py_major_minor(target_config):
    """ Return a tuple of the major and minor Python version numbers.
    target_config is the target configuration.
    """

    py_major = target_config.py_version >> 16
    py_minor = (target_config.py_version >> 8) & 0x0ff

    return py_major, py_minor


def get_module_metadata(target_config, mname):
    """ Get the metadata for a module.  target_config is the target
    configuration.  mname is the name of the module.
    """

    metadata = QT4_MODULES if target_config.qt_version < 0x050000 else QT5_MODULES

    return metadata[mname]


def main(argv):
    """ Create the configuration module module.  argv is the list of command
    line arguments.
    """

    # Create the default target configuration.
    target_config = TargetConfiguration()

    # Parse the command line.
    parser = create_optparser(target_config)
    opts, target_config.qmake_variables = parser.parse_args()

    # Query qmake for the basic configuration information.
    target_config.get_qt_configuration(opts)

    # Update the target configuration.
    if opts.config_file is not None:
        target_config.from_configuration_file(opts.config_file)
    else:
        target_config.from_introspection(opts.verbose)

    target_config.override_defaults(opts)

    # Check the licenses are compatible.
    check_license(target_config, opts.license_confirmed)

    # Check SIP is what we need.
    sip_version = check_sip(target_config)

    # Check Qt is what we need.
    check_qt(target_config)

    # Check for the VendorID package.
    check_vendorid(target_config)

    # Check which modules to build if we haven't been told.
    if len(target_config.modules) == 0:
        check_modules(target_config, opts.verbose)

    # Tell the user what's been found.
    inform_user(target_config, sip_version)

    # Generate the makefiles.
    generate_makefiles(target_config, opts.verbose, opts.notimestamp,
            opts.split if opts.concat else 0, opts.tracing)


###############################################################################
# The script starts here.
###############################################################################

if __name__ == '__main__':
    try:
        main(sys.argv)
    except SystemExit:
        raise
    except:
        sys.stderr.write(
"""An internal error occured.  Please report all the output from the program,
including the following traceback, to support@riverbankcomputing.com.
""")
        raise
