/*
 * Interface wrapper code.
 *
 * Generated by SIP 4.16.2 on Wed Sep  3 09:36:19 2014
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

#include "sipAPIQtGui.h"

#line 33 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtGui/qinputcontextfactory.sip"
#include <qinputcontextfactory.h>
#line 34 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQInputContextFactory.cpp"

#line 36 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qstring.sip"
#include <qstring.h>
#line 38 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQInputContextFactory.cpp"
#line 36 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qstringlist.sip"
#include <qstringlist.h>
#line 41 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQInputContextFactory.cpp"
#line 33 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtGui/qinputcontext.sip"
#include <qinputcontext.h>
#line 44 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQInputContextFactory.cpp"
#line 34 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qobject.sip"
#include <qobject.h>
#line 47 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQInputContextFactory.cpp"


PyDoc_STRVAR(doc_QInputContextFactory_keys, "QInputContextFactory.keys() -> QStringList");

extern "C" {static PyObject *meth_QInputContextFactory_keys(PyObject *, PyObject *);}
static PyObject *meth_QInputContextFactory_keys(PyObject *, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        if (sipParseArgs(&sipParseErr, sipArgs, ""))
        {
            QStringList*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QStringList(QInputContextFactory::keys());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QStringList,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QInputContextFactory, sipName_keys, doc_QInputContextFactory_keys);

    return NULL;
}


PyDoc_STRVAR(doc_QInputContextFactory_create, "QInputContextFactory.create(QString, QObject) -> QInputContext");

extern "C" {static PyObject *meth_QInputContextFactory_create(PyObject *, PyObject *);}
static PyObject *meth_QInputContextFactory_create(PyObject *, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QString* a0;
        int a0State = 0;
        QObject* a1;
        sipWrapper *sipOwner = 0;

        if (sipParseArgs(&sipParseErr, sipArgs, "J1JH", sipType_QString,&a0, &a0State, sipType_QObject, &a1, &sipOwner))
        {
            QInputContext*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = QInputContextFactory::create(*a0,a1);
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<QString *>(a0),sipType_QString,a0State);

            return sipConvertFromNewType(sipRes,sipType_QInputContext,(PyObject *)sipOwner);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QInputContextFactory, sipName_create, doc_QInputContextFactory_create);

    return NULL;
}


PyDoc_STRVAR(doc_QInputContextFactory_languages, "QInputContextFactory.languages(QString) -> QStringList");

extern "C" {static PyObject *meth_QInputContextFactory_languages(PyObject *, PyObject *);}
static PyObject *meth_QInputContextFactory_languages(PyObject *, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QString* a0;
        int a0State = 0;

        if (sipParseArgs(&sipParseErr, sipArgs, "J1", sipType_QString,&a0, &a0State))
        {
            QStringList*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QStringList(QInputContextFactory::languages(*a0));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<QString *>(a0),sipType_QString,a0State);

            return sipConvertFromNewType(sipRes,sipType_QStringList,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QInputContextFactory, sipName_languages, doc_QInputContextFactory_languages);

    return NULL;
}


PyDoc_STRVAR(doc_QInputContextFactory_displayName, "QInputContextFactory.displayName(QString) -> QString");

extern "C" {static PyObject *meth_QInputContextFactory_displayName(PyObject *, PyObject *);}
static PyObject *meth_QInputContextFactory_displayName(PyObject *, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QString* a0;
        int a0State = 0;

        if (sipParseArgs(&sipParseErr, sipArgs, "J1", sipType_QString,&a0, &a0State))
        {
            QString*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QString(QInputContextFactory::displayName(*a0));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<QString *>(a0),sipType_QString,a0State);

            return sipConvertFromNewType(sipRes,sipType_QString,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QInputContextFactory, sipName_displayName, doc_QInputContextFactory_displayName);

    return NULL;
}


PyDoc_STRVAR(doc_QInputContextFactory_description, "QInputContextFactory.description(QString) -> QString");

extern "C" {static PyObject *meth_QInputContextFactory_description(PyObject *, PyObject *);}
static PyObject *meth_QInputContextFactory_description(PyObject *, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QString* a0;
        int a0State = 0;

        if (sipParseArgs(&sipParseErr, sipArgs, "J1", sipType_QString,&a0, &a0State))
        {
            QString*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QString(QInputContextFactory::description(*a0));
            Py_END_ALLOW_THREADS
            sipReleaseType(const_cast<QString *>(a0),sipType_QString,a0State);

            return sipConvertFromNewType(sipRes,sipType_QString,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QInputContextFactory, sipName_description, doc_QInputContextFactory_description);

    return NULL;
}


/* Cast a pointer to a type somewhere in its superclass hierarchy. */
extern "C" {static void *cast_QInputContextFactory(void *, const sipTypeDef *);}
static void *cast_QInputContextFactory(void *ptr, const sipTypeDef *targetType)
{
    if (targetType == sipType_QInputContextFactory)
        return ptr;

    return NULL;
}


/* Call the instance's destructor. */
extern "C" {static void release_QInputContextFactory(void *, int);}
static void release_QInputContextFactory(void *sipCppV,int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<QInputContextFactory *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void assign_QInputContextFactory(void *, SIP_SSIZE_T, const void *);}
static void assign_QInputContextFactory(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast<QInputContextFactory *>(sipDst)[sipDstIdx] = *reinterpret_cast<const QInputContextFactory *>(sipSrc);
}


extern "C" {static void *array_QInputContextFactory(SIP_SSIZE_T);}
static void *array_QInputContextFactory(SIP_SSIZE_T sipNrElem)
{
    return new QInputContextFactory[sipNrElem];
}


extern "C" {static void *copy_QInputContextFactory(const void *, SIP_SSIZE_T);}
static void *copy_QInputContextFactory(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new QInputContextFactory(reinterpret_cast<const QInputContextFactory *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_QInputContextFactory(sipSimpleWrapper *);}
static void dealloc_QInputContextFactory(sipSimpleWrapper *sipSelf)
{
    if (sipIsPyOwned(sipSelf))
    {
        release_QInputContextFactory(sipGetAddress(sipSelf),0);
    }
}


extern "C" {static void *init_type_QInputContextFactory(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QInputContextFactory(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    QInputContextFactory *sipCpp = 0;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, ""))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new QInputContextFactory();
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        const QInputContextFactory* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J9", sipType_QInputContextFactory, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new QInputContextFactory(*a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    return NULL;
}


static PyMethodDef methods_QInputContextFactory[] = {
    {SIP_MLNAME_CAST(sipName_create), meth_QInputContextFactory_create, METH_VARARGS, SIP_MLDOC_CAST(doc_QInputContextFactory_create)},
    {SIP_MLNAME_CAST(sipName_description), meth_QInputContextFactory_description, METH_VARARGS, SIP_MLDOC_CAST(doc_QInputContextFactory_description)},
    {SIP_MLNAME_CAST(sipName_displayName), meth_QInputContextFactory_displayName, METH_VARARGS, SIP_MLDOC_CAST(doc_QInputContextFactory_displayName)},
    {SIP_MLNAME_CAST(sipName_keys), meth_QInputContextFactory_keys, METH_VARARGS, SIP_MLDOC_CAST(doc_QInputContextFactory_keys)},
    {SIP_MLNAME_CAST(sipName_languages), meth_QInputContextFactory_languages, METH_VARARGS, SIP_MLDOC_CAST(doc_QInputContextFactory_languages)}
};

PyDoc_STRVAR(doc_QInputContextFactory, "\1QInputContextFactory()\n"
    "QInputContextFactory(QInputContextFactory)");


pyqt4ClassTypeDef sipTypeDef_QtGui_QInputContextFactory = {
{
    {
        -1,
        0,
        0,
        SIP_TYPE_CLASS,
        sipNameNr_QInputContextFactory,
        {0}
    },
    {
        sipNameNr_QInputContextFactory,
        {0, 0, 1},
        5, methods_QInputContextFactory,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QInputContextFactory,
    sipNameNr_PyQt4_QtCore_pyqtWrapperType,
    sipNameNr_sip_simplewrapper,
    0,
    0,
    init_type_QInputContextFactory,
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
    dealloc_QInputContextFactory,
    assign_QInputContextFactory,
    array_QInputContextFactory,
    copy_QInputContextFactory,
    release_QInputContextFactory,
    cast_QInputContextFactory,
    0,
    0,
    0,
    0,
    0,
    0
},
    0,
    0,
    0
};