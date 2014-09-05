/*
 * Interface wrapper code.
 *
 * Generated by SIP 4.16.2 on Wed Sep  3 09:36:12 2014
 *
 * Copyright (c) 2014 Riverbank Computing Limited <info@riverbankcomputing.com>
 * 
 * This file is part of PyQt.
 * 
 * This file may be used under the terms of the GNU General Public
 * License versions 2.0 or 3.0 as published by the Free Software
 * Foundation and appearing in the files LICENSE.GPL2 and LICENSE.GPL3
 * included in the packaging of this file.  Alternatively you may (at
 * your option) use any later version of the GNU General Public
 * License if such license has been publicly approved by Riverbank
 * Computing Limited (or its successors, if any) and the KDE Free Qt
 * Foundation. In addition, as a special exception, Riverbank gives you
 * certain additional rights. These rights are described in the Riverbank
 * GPL Exception version 1.1, which can be found in the file
 * GPL_EXCEPTION.txt in this package.
 * 
 * If you are unsure which license is appropriate for your use, please
 * contact the sales department at sales@riverbankcomputing.com.
 * 
 * This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
 * WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
 */

#include "sipAPIQtCore.h"

#line 31 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qsocketnotifier.sip"
#include <qsocketnotifier.h>
#line 34 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQSocketNotifier.cpp"

#line 34 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qobject.sip"
#include <qobject.h>
#line 38 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQSocketNotifier.cpp"
#line 31 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 41 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQSocketNotifier.cpp"
#line 355 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 44 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQSocketNotifier.cpp"
#line 338 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 47 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQSocketNotifier.cpp"
#line 274 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qvariant.sip"
#include <qvariant.h>
#line 50 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQSocketNotifier.cpp"
#line 33 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qlist.sip"
#include <qlist.h>
#line 53 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQSocketNotifier.cpp"
#line 37 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qbytearray.sip"
#include <qbytearray.h>
#line 56 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQSocketNotifier.cpp"
#line 35 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qnamespace.sip"
#include <qnamespace.h>
#line 59 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQSocketNotifier.cpp"
#line 120 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qlist.sip"
#include <qlist.h>
#line 62 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQSocketNotifier.cpp"
#line 31 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qthread.sip"
#include <qthread.h>
#line 65 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQSocketNotifier.cpp"
#line 36 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qstring.sip"
#include <qstring.h>
#line 68 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQSocketNotifier.cpp"
#line 35 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qregexp.sip"
#include <qregexp.h>
#line 71 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQSocketNotifier.cpp"
#line 31 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qobjectdefs.sip"
#include <qobjectdefs.h>
#line 74 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQSocketNotifier.cpp"


class sipQSocketNotifier : public QSocketNotifier
{
public:
    sipQSocketNotifier(int,QSocketNotifier::Type,QObject*);
    virtual ~sipQSocketNotifier();

    int qt_metacall(QMetaObject::Call,int,void **);
    void *qt_metacast(const char *);
    const QMetaObject *metaObject() const;

    /*
     * There is a protected method for every virtual method visible from
     * this class.
     */
protected:
    void disconnectNotify(const char*);
    void connectNotify(const char*);
    void customEvent(QEvent*);
    void childEvent(QChildEvent*);
    void timerEvent(QTimerEvent*);
    bool eventFilter(QObject*,QEvent*);
    bool event(QEvent*);

public:
    sipSimpleWrapper *sipPySelf;

private:
    sipQSocketNotifier(const sipQSocketNotifier &);
    sipQSocketNotifier &operator = (const sipQSocketNotifier &);

    char sipPyMethods[7];
};

sipQSocketNotifier::sipQSocketNotifier(int a0,QSocketNotifier::Type a1,QObject*a2): QSocketNotifier(a0,a1,a2), sipPySelf(0)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipQSocketNotifier::~sipQSocketNotifier()
{
    sipCommonDtor(sipPySelf);
}

const QMetaObject *sipQSocketNotifier::metaObject() const
{
    return sip_QtCore_qt_metaobject(sipPySelf,sipType_QSocketNotifier);
}

int sipQSocketNotifier::qt_metacall(QMetaObject::Call _c,int _id,void **_a)
{
    _id = QSocketNotifier::qt_metacall(_c,_id,_a);

    if (_id >= 0)
        _id = sip_QtCore_qt_metacall(sipPySelf,sipType_QSocketNotifier,_c,_id,_a);

    return _id;
}

void *sipQSocketNotifier::qt_metacast(const char *_clname)
{
    return (sip_QtCore_qt_metacast(sipPySelf, sipType_QSocketNotifier, _clname)) ? this : QSocketNotifier::qt_metacast(_clname);
}

void sipQSocketNotifier::disconnectNotify(const char*a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[0],sipPySelf,NULL,sipName_disconnectNotify);

    if (!sipMeth)
    {
        QSocketNotifier::disconnectNotify(a0);
        return;
    }

    extern void sipVH_QtCore_24(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const char*);

    sipVH_QtCore_24(sipGILState, 0, sipPySelf, sipMeth, a0);
}

void sipQSocketNotifier::connectNotify(const char*a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[1],sipPySelf,NULL,sipName_connectNotify);

    if (!sipMeth)
    {
        QSocketNotifier::connectNotify(a0);
        return;
    }

    extern void sipVH_QtCore_24(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const char*);

    sipVH_QtCore_24(sipGILState, 0, sipPySelf, sipMeth, a0);
}

void sipQSocketNotifier::customEvent(QEvent*a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[2],sipPySelf,NULL,sipName_customEvent);

    if (!sipMeth)
    {
        QSocketNotifier::customEvent(a0);
        return;
    }

    extern void sipVH_QtCore_17(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, QEvent*);

    sipVH_QtCore_17(sipGILState, 0, sipPySelf, sipMeth, a0);
}

void sipQSocketNotifier::childEvent(QChildEvent*a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[3],sipPySelf,NULL,sipName_childEvent);

    if (!sipMeth)
    {
        QSocketNotifier::childEvent(a0);
        return;
    }

    extern void sipVH_QtCore_25(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, QChildEvent*);

    sipVH_QtCore_25(sipGILState, 0, sipPySelf, sipMeth, a0);
}

void sipQSocketNotifier::timerEvent(QTimerEvent*a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[4],sipPySelf,NULL,sipName_timerEvent);

    if (!sipMeth)
    {
        QSocketNotifier::timerEvent(a0);
        return;
    }

    extern void sipVH_QtCore_9(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, QTimerEvent*);

    sipVH_QtCore_9(sipGILState, 0, sipPySelf, sipMeth, a0);
}

bool sipQSocketNotifier::eventFilter(QObject*a0,QEvent*a1)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[5],sipPySelf,NULL,sipName_eventFilter);

    if (!sipMeth)
        return QSocketNotifier::eventFilter(a0,a1);

    extern bool sipVH_QtCore_18(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, QObject*,QEvent*);

    return sipVH_QtCore_18(sipGILState, 0, sipPySelf, sipMeth, a0, a1);
}

bool sipQSocketNotifier::event(QEvent*a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[6],sipPySelf,NULL,sipName_event);

    if (!sipMeth)
        return QSocketNotifier::event(a0);

    extern bool sipVH_QtCore_5(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, QEvent*);

    return sipVH_QtCore_5(sipGILState, 0, sipPySelf, sipMeth, a0);
}


PyDoc_STRVAR(doc_QSocketNotifier_socket, "QSocketNotifier.socket() -> int");

extern "C" {static PyObject *meth_QSocketNotifier_socket(PyObject *, PyObject *);}
static PyObject *meth_QSocketNotifier_socket(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QSocketNotifier *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QSocketNotifier, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->socket();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QSocketNotifier, sipName_socket, doc_QSocketNotifier_socket);

    return NULL;
}


PyDoc_STRVAR(doc_QSocketNotifier_type, "QSocketNotifier.type() -> QSocketNotifier.Type");

extern "C" {static PyObject *meth_QSocketNotifier_type(PyObject *, PyObject *);}
static PyObject *meth_QSocketNotifier_type(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QSocketNotifier *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QSocketNotifier, &sipCpp))
        {
            QSocketNotifier::Type sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->type();
            Py_END_ALLOW_THREADS

            return sipConvertFromEnum(sipRes,sipType_QSocketNotifier_Type);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QSocketNotifier, sipName_type, doc_QSocketNotifier_type);

    return NULL;
}


PyDoc_STRVAR(doc_QSocketNotifier_isEnabled, "QSocketNotifier.isEnabled() -> bool");

extern "C" {static PyObject *meth_QSocketNotifier_isEnabled(PyObject *, PyObject *);}
static PyObject *meth_QSocketNotifier_isEnabled(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QSocketNotifier *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QSocketNotifier, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->isEnabled();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QSocketNotifier, sipName_isEnabled, doc_QSocketNotifier_isEnabled);

    return NULL;
}


PyDoc_STRVAR(doc_QSocketNotifier_setEnabled, "QSocketNotifier.setEnabled(bool)");

extern "C" {static PyObject *meth_QSocketNotifier_setEnabled(PyObject *, PyObject *);}
static PyObject *meth_QSocketNotifier_setEnabled(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        bool a0;
        QSocketNotifier *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "Bb", &sipSelf, sipType_QSocketNotifier, &sipCpp, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->setEnabled(a0);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QSocketNotifier, sipName_setEnabled, doc_QSocketNotifier_setEnabled);

    return NULL;
}


PyDoc_STRVAR(doc_QSocketNotifier_event, "QSocketNotifier.event(QEvent) -> bool");

extern "C" {static PyObject *meth_QSocketNotifier_event(PyObject *, PyObject *);}
static PyObject *meth_QSocketNotifier_event(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;
    bool sipSelfWasArg = (!sipSelf || sipIsDerived((sipSimpleWrapper *)sipSelf));

    {
        QEvent* a0;
        QSocketNotifier *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "pJ8", &sipSelf, sipType_QSocketNotifier, &sipCpp, sipType_QEvent, &a0))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = (sipSelfWasArg ? sipCpp->QSocketNotifier::event(a0) : sipCpp->event(a0));
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QSocketNotifier, sipName_event, doc_QSocketNotifier_event);

    return NULL;
}


/* Cast a pointer to a type somewhere in its superclass hierarchy. */
extern "C" {static void *cast_QSocketNotifier(void *, const sipTypeDef *);}
static void *cast_QSocketNotifier(void *ptr, const sipTypeDef *targetType)
{
    void *res;

    if (targetType == sipType_QSocketNotifier)
        return ptr;

    if ((res = ((const sipClassTypeDef *)sipType_QObject)->ctd_cast((QObject *)(QSocketNotifier *)ptr,targetType)) != NULL)
        return res;

    return NULL;
}


/* Call the instance's destructor. */
extern "C" {static void release_QSocketNotifier(void *, int);}
static void release_QSocketNotifier(void *sipCppV,int)
{
    QSocketNotifier *sipCpp = reinterpret_cast<QSocketNotifier *>(sipCppV);

    Py_BEGIN_ALLOW_THREADS

    if (QThread::currentThread() == sipCpp->thread())
        delete sipCpp;
    else
        sipCpp->deleteLater();

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_QSocketNotifier(sipSimpleWrapper *);}
static void dealloc_QSocketNotifier(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerived(sipSelf))
        reinterpret_cast<sipQSocketNotifier *>(sipGetAddress(sipSelf))->sipPySelf = NULL;

    if (sipIsPyOwned(sipSelf))
    {
        release_QSocketNotifier(sipGetAddress(sipSelf),sipSelf->flags);
    }
}


extern "C" {static void *init_type_QSocketNotifier(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QSocketNotifier(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **sipOwner, PyObject **sipParseErr)
{
    sipQSocketNotifier *sipCpp = 0;

    {
        int a0;
        QSocketNotifier::Type a1;
        QObject* a2 = 0;

        static const char *sipKwdList[] = {
            NULL,
            NULL,
            sipName_parent,
        };

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, sipKwdList, sipUnused, "iE|JH", &a0, sipType_QSocketNotifier_Type, &a1, sipType_QObject, &a2, sipOwner))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipQSocketNotifier(a0,a1,a2);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return NULL;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_QSocketNotifier[] = {{141, 255, 1}};


static PyMethodDef methods_QSocketNotifier[] = {
    {SIP_MLNAME_CAST(sipName_event), meth_QSocketNotifier_event, METH_VARARGS, SIP_MLDOC_CAST(doc_QSocketNotifier_event)},
    {SIP_MLNAME_CAST(sipName_isEnabled), meth_QSocketNotifier_isEnabled, METH_VARARGS, SIP_MLDOC_CAST(doc_QSocketNotifier_isEnabled)},
    {SIP_MLNAME_CAST(sipName_setEnabled), meth_QSocketNotifier_setEnabled, METH_VARARGS, SIP_MLDOC_CAST(doc_QSocketNotifier_setEnabled)},
    {SIP_MLNAME_CAST(sipName_socket), meth_QSocketNotifier_socket, METH_VARARGS, SIP_MLDOC_CAST(doc_QSocketNotifier_socket)},
    {SIP_MLNAME_CAST(sipName_type), meth_QSocketNotifier_type, METH_VARARGS, SIP_MLDOC_CAST(doc_QSocketNotifier_type)}
};

static sipEnumMemberDef enummembers_QSocketNotifier[] = {
    {sipName_Exception, static_cast<int>(QSocketNotifier::Exception), 188},
    {sipName_Read, static_cast<int>(QSocketNotifier::Read), 188},
    {sipName_Write, static_cast<int>(QSocketNotifier::Write), 188},
};


/* Define this type's signals. */
static const pyqt4QtSignal signals_QSocketNotifier[] = {
    {"activated(int)", "\1QSocketNotifier.activated[int]", 0, 0},
    {0, 0, 0, 0}
};

PyDoc_STRVAR(doc_QSocketNotifier, "\1QSocketNotifier(int, QSocketNotifier.Type, QObject parent=None)");


pyqt4ClassTypeDef sipTypeDef_QtCore_QSocketNotifier = {
{
    {
        -1,
        0,
        0,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_QSocketNotifier,
        {0}
    },
    {
        sipNameNr_QSocketNotifier,
        {0, 0, 1},
        5, methods_QSocketNotifier,
        3, enummembers_QSocketNotifier,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QSocketNotifier,
    -1,
    -1,
    supers_QSocketNotifier,
    0,
    init_type_QSocketNotifier,
    0,
    0,
#if PY_MAJOR_VERSION >= 3
    0,
    0,
#else
    0,
    0,
    0,
    0,
#endif
    dealloc_QSocketNotifier,
    0,
    0,
    0,
    release_QSocketNotifier,
    cast_QSocketNotifier,
    0,
    0,
    0,
    0,
    0,
    0
},
    &QSocketNotifier::staticMetaObject,
    0,
    signals_QSocketNotifier,
};