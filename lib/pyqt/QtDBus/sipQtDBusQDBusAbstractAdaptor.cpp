/*
 * Interface wrapper code.
 *
 * Generated by SIP 4.16.2 on Wed Sep  3 09:36:23 2014
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

#include "sipAPIQtDBus.h"

#line 33 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtDBus/qdbusabstractadaptor.sip"
#include <qdbusabstractadaptor.h>
#line 34 "/home/desa2/PyQt-x11-gpl-4.10.4/QtDBus/sipQtDBusQDBusAbstractAdaptor.cpp"

#line 34 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qobject.sip"
#include <qobject.h>
#line 38 "/home/desa2/PyQt-x11-gpl-4.10.4/QtDBus/sipQtDBusQDBusAbstractAdaptor.cpp"
#line 31 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 41 "/home/desa2/PyQt-x11-gpl-4.10.4/QtDBus/sipQtDBusQDBusAbstractAdaptor.cpp"
#line 355 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 44 "/home/desa2/PyQt-x11-gpl-4.10.4/QtDBus/sipQtDBusQDBusAbstractAdaptor.cpp"
#line 338 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 47 "/home/desa2/PyQt-x11-gpl-4.10.4/QtDBus/sipQtDBusQDBusAbstractAdaptor.cpp"
#line 274 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qvariant.sip"
#include <qvariant.h>
#line 50 "/home/desa2/PyQt-x11-gpl-4.10.4/QtDBus/sipQtDBusQDBusAbstractAdaptor.cpp"
#line 33 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qlist.sip"
#include <qlist.h>
#line 53 "/home/desa2/PyQt-x11-gpl-4.10.4/QtDBus/sipQtDBusQDBusAbstractAdaptor.cpp"
#line 37 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qbytearray.sip"
#include <qbytearray.h>
#line 56 "/home/desa2/PyQt-x11-gpl-4.10.4/QtDBus/sipQtDBusQDBusAbstractAdaptor.cpp"
#line 35 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qnamespace.sip"
#include <qnamespace.h>
#line 59 "/home/desa2/PyQt-x11-gpl-4.10.4/QtDBus/sipQtDBusQDBusAbstractAdaptor.cpp"
#line 120 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qlist.sip"
#include <qlist.h>
#line 62 "/home/desa2/PyQt-x11-gpl-4.10.4/QtDBus/sipQtDBusQDBusAbstractAdaptor.cpp"
#line 31 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qthread.sip"
#include <qthread.h>
#line 65 "/home/desa2/PyQt-x11-gpl-4.10.4/QtDBus/sipQtDBusQDBusAbstractAdaptor.cpp"
#line 36 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qstring.sip"
#include <qstring.h>
#line 68 "/home/desa2/PyQt-x11-gpl-4.10.4/QtDBus/sipQtDBusQDBusAbstractAdaptor.cpp"
#line 35 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qregexp.sip"
#include <qregexp.h>
#line 71 "/home/desa2/PyQt-x11-gpl-4.10.4/QtDBus/sipQtDBusQDBusAbstractAdaptor.cpp"
#line 31 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qobjectdefs.sip"
#include <qobjectdefs.h>
#line 74 "/home/desa2/PyQt-x11-gpl-4.10.4/QtDBus/sipQtDBusQDBusAbstractAdaptor.cpp"


class sipQDBusAbstractAdaptor : public QDBusAbstractAdaptor
{
public:
    sipQDBusAbstractAdaptor(QObject*);
    virtual ~sipQDBusAbstractAdaptor();

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
    sipQDBusAbstractAdaptor(const sipQDBusAbstractAdaptor &);
    sipQDBusAbstractAdaptor &operator = (const sipQDBusAbstractAdaptor &);

    char sipPyMethods[7];
};

sipQDBusAbstractAdaptor::sipQDBusAbstractAdaptor(QObject*a0): QDBusAbstractAdaptor(a0), sipPySelf(0)
{
    memset(sipPyMethods, 0, sizeof (sipPyMethods));
}

sipQDBusAbstractAdaptor::~sipQDBusAbstractAdaptor()
{
    sipCommonDtor(sipPySelf);
}

const QMetaObject *sipQDBusAbstractAdaptor::metaObject() const
{
    return sip_QtDBus_qt_metaobject(sipPySelf,sipType_QDBusAbstractAdaptor);
}

int sipQDBusAbstractAdaptor::qt_metacall(QMetaObject::Call _c,int _id,void **_a)
{
    _id = QDBusAbstractAdaptor::qt_metacall(_c,_id,_a);

    if (_id >= 0)
        _id = sip_QtDBus_qt_metacall(sipPySelf,sipType_QDBusAbstractAdaptor,_c,_id,_a);

    return _id;
}

void *sipQDBusAbstractAdaptor::qt_metacast(const char *_clname)
{
    return (sip_QtDBus_qt_metacast(sipPySelf, sipType_QDBusAbstractAdaptor, _clname)) ? this : QDBusAbstractAdaptor::qt_metacast(_clname);
}

void sipQDBusAbstractAdaptor::disconnectNotify(const char*a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[0],sipPySelf,NULL,sipName_disconnectNotify);

    if (!sipMeth)
    {
        QDBusAbstractAdaptor::disconnectNotify(a0);
        return;
    }

    typedef void (*sipVH_QtCore_24)(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const char*);

    ((sipVH_QtCore_24)(sipModuleAPI_QtDBus_QtCore->em_virthandlers[24]))(sipGILState, 0, sipPySelf, sipMeth, a0);
}

void sipQDBusAbstractAdaptor::connectNotify(const char*a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[1],sipPySelf,NULL,sipName_connectNotify);

    if (!sipMeth)
    {
        QDBusAbstractAdaptor::connectNotify(a0);
        return;
    }

    typedef void (*sipVH_QtCore_24)(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, const char*);

    ((sipVH_QtCore_24)(sipModuleAPI_QtDBus_QtCore->em_virthandlers[24]))(sipGILState, 0, sipPySelf, sipMeth, a0);
}

void sipQDBusAbstractAdaptor::customEvent(QEvent*a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[2],sipPySelf,NULL,sipName_customEvent);

    if (!sipMeth)
    {
        QDBusAbstractAdaptor::customEvent(a0);
        return;
    }

    typedef void (*sipVH_QtCore_17)(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, QEvent*);

    ((sipVH_QtCore_17)(sipModuleAPI_QtDBus_QtCore->em_virthandlers[17]))(sipGILState, 0, sipPySelf, sipMeth, a0);
}

void sipQDBusAbstractAdaptor::childEvent(QChildEvent*a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[3],sipPySelf,NULL,sipName_childEvent);

    if (!sipMeth)
    {
        QDBusAbstractAdaptor::childEvent(a0);
        return;
    }

    typedef void (*sipVH_QtCore_25)(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, QChildEvent*);

    ((sipVH_QtCore_25)(sipModuleAPI_QtDBus_QtCore->em_virthandlers[25]))(sipGILState, 0, sipPySelf, sipMeth, a0);
}

void sipQDBusAbstractAdaptor::timerEvent(QTimerEvent*a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[4],sipPySelf,NULL,sipName_timerEvent);

    if (!sipMeth)
    {
        QDBusAbstractAdaptor::timerEvent(a0);
        return;
    }

    typedef void (*sipVH_QtCore_9)(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, QTimerEvent*);

    ((sipVH_QtCore_9)(sipModuleAPI_QtDBus_QtCore->em_virthandlers[9]))(sipGILState, 0, sipPySelf, sipMeth, a0);
}

bool sipQDBusAbstractAdaptor::eventFilter(QObject*a0,QEvent*a1)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[5],sipPySelf,NULL,sipName_eventFilter);

    if (!sipMeth)
        return QDBusAbstractAdaptor::eventFilter(a0,a1);

    typedef bool (*sipVH_QtCore_18)(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, QObject*,QEvent*);

    return ((sipVH_QtCore_18)(sipModuleAPI_QtDBus_QtCore->em_virthandlers[18]))(sipGILState, 0, sipPySelf, sipMeth, a0, a1);
}

bool sipQDBusAbstractAdaptor::event(QEvent*a0)
{
    sip_gilstate_t sipGILState;
    PyObject *sipMeth;

    sipMeth = sipIsPyMethod(&sipGILState,&sipPyMethods[6],sipPySelf,NULL,sipName_event);

    if (!sipMeth)
        return QDBusAbstractAdaptor::event(a0);

    typedef bool (*sipVH_QtCore_5)(sip_gilstate_t, sipVirtErrorHandlerFunc, sipSimpleWrapper *, PyObject *, QEvent*);

    return ((sipVH_QtCore_5)(sipModuleAPI_QtDBus_QtCore->em_virthandlers[5]))(sipGILState, 0, sipPySelf, sipMeth, a0);
}


PyDoc_STRVAR(doc_QDBusAbstractAdaptor_setAutoRelaySignals, "QDBusAbstractAdaptor.setAutoRelaySignals(bool)");

extern "C" {static PyObject *meth_QDBusAbstractAdaptor_setAutoRelaySignals(PyObject *, PyObject *);}
static PyObject *meth_QDBusAbstractAdaptor_setAutoRelaySignals(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        bool a0;
        QDBusAbstractAdaptor *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "pb", &sipSelf, sipType_QDBusAbstractAdaptor, &sipCpp, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp->setAutoRelaySignals(a0);
            Py_END_ALLOW_THREADS

            Py_INCREF(Py_None);
            return Py_None;
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QDBusAbstractAdaptor, sipName_setAutoRelaySignals, doc_QDBusAbstractAdaptor_setAutoRelaySignals);

    return NULL;
}


PyDoc_STRVAR(doc_QDBusAbstractAdaptor_autoRelaySignals, "QDBusAbstractAdaptor.autoRelaySignals() -> bool");

extern "C" {static PyObject *meth_QDBusAbstractAdaptor_autoRelaySignals(PyObject *, PyObject *);}
static PyObject *meth_QDBusAbstractAdaptor_autoRelaySignals(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QDBusAbstractAdaptor *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "p", &sipSelf, sipType_QDBusAbstractAdaptor, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->autoRelaySignals();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QDBusAbstractAdaptor, sipName_autoRelaySignals, doc_QDBusAbstractAdaptor_autoRelaySignals);

    return NULL;
}


/* Cast a pointer to a type somewhere in its superclass hierarchy. */
extern "C" {static void *cast_QDBusAbstractAdaptor(void *, const sipTypeDef *);}
static void *cast_QDBusAbstractAdaptor(void *ptr, const sipTypeDef *targetType)
{
    void *res;

    if (targetType == sipType_QDBusAbstractAdaptor)
        return ptr;

    if ((res = ((const sipClassTypeDef *)sipType_QObject)->ctd_cast((QObject *)(QDBusAbstractAdaptor *)ptr,targetType)) != NULL)
        return res;

    return NULL;
}


/* Call the instance's destructor. */
extern "C" {static void release_QDBusAbstractAdaptor(void *, int);}
static void release_QDBusAbstractAdaptor(void *sipCppV,int)
{
    QDBusAbstractAdaptor *sipCpp = reinterpret_cast<QDBusAbstractAdaptor *>(sipCppV);

    Py_BEGIN_ALLOW_THREADS

    if (QThread::currentThread() == sipCpp->thread())
        delete sipCpp;
    else
        sipCpp->deleteLater();

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_QDBusAbstractAdaptor(sipSimpleWrapper *);}
static void dealloc_QDBusAbstractAdaptor(sipSimpleWrapper *sipSelf)
{
    if (sipIsDerived(sipSelf))
        reinterpret_cast<sipQDBusAbstractAdaptor *>(sipGetAddress(sipSelf))->sipPySelf = NULL;

    if (sipIsPyOwned(sipSelf))
    {
        release_QDBusAbstractAdaptor(sipGetAddress(sipSelf),sipSelf->flags);
    }
}


extern "C" {static void *init_type_QDBusAbstractAdaptor(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QDBusAbstractAdaptor(sipSimpleWrapper *sipSelf, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **sipOwner, PyObject **sipParseErr)
{
    sipQDBusAbstractAdaptor *sipCpp = 0;

    {
        QObject* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "JH", sipType_QObject, &a0, sipOwner))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new sipQDBusAbstractAdaptor(a0);
            Py_END_ALLOW_THREADS

            sipCpp->sipPySelf = sipSelf;

            return sipCpp;
        }
    }

    return NULL;
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_QDBusAbstractAdaptor[] = {{141, 0, 1}};


static PyMethodDef methods_QDBusAbstractAdaptor[] = {
    {SIP_MLNAME_CAST(sipName_autoRelaySignals), meth_QDBusAbstractAdaptor_autoRelaySignals, METH_VARARGS, SIP_MLDOC_CAST(doc_QDBusAbstractAdaptor_autoRelaySignals)},
    {SIP_MLNAME_CAST(sipName_setAutoRelaySignals), meth_QDBusAbstractAdaptor_setAutoRelaySignals, METH_VARARGS, SIP_MLDOC_CAST(doc_QDBusAbstractAdaptor_setAutoRelaySignals)}
};

PyDoc_STRVAR(doc_QDBusAbstractAdaptor, "\1QDBusAbstractAdaptor(QObject)");


pyqt4ClassTypeDef sipTypeDef_QtDBus_QDBusAbstractAdaptor = {
{
    {
        -1,
        0,
        0,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_QDBusAbstractAdaptor,
        {0}
    },
    {
        sipNameNr_QDBusAbstractAdaptor,
        {0, 0, 1},
        2, methods_QDBusAbstractAdaptor,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QDBusAbstractAdaptor,
    -1,
    -1,
    supers_QDBusAbstractAdaptor,
    0,
    init_type_QDBusAbstractAdaptor,
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
    dealloc_QDBusAbstractAdaptor,
    0,
    0,
    0,
    release_QDBusAbstractAdaptor,
    cast_QDBusAbstractAdaptor,
    0,
    0,
    0,
    0,
    0,
    0
},
    &QDBusAbstractAdaptor::staticMetaObject,
    0,
    0
};