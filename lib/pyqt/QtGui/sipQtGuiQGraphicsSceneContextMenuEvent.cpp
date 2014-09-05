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

#line 110 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtGui/qgraphicssceneevent.sip"
#include <qgraphicssceneevent.h>
#line 34 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQGraphicsSceneContextMenuEvent.cpp"

#line 35 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qnamespace.sip"
#include <qnamespace.h>
#line 38 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQGraphicsSceneContextMenuEvent.cpp"
#line 35 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qpoint.sip"
#include <qpoint.h>
#line 41 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQGraphicsSceneContextMenuEvent.cpp"
#line 119 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qpoint.sip"
#include <qpoint.h>
#line 44 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQGraphicsSceneContextMenuEvent.cpp"
#line 35 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtGui/qwidget.sip"
#include <qwidget.h>
#line 47 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQGraphicsSceneContextMenuEvent.cpp"
#line 31 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qcoreevent.sip"
#include <qcoreevent.h>
#line 50 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQGraphicsSceneContextMenuEvent.cpp"


PyDoc_STRVAR(doc_QGraphicsSceneContextMenuEvent_pos, "QGraphicsSceneContextMenuEvent.pos() -> QPointF");

extern "C" {static PyObject *meth_QGraphicsSceneContextMenuEvent_pos(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsSceneContextMenuEvent_pos(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QGraphicsSceneContextMenuEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QGraphicsSceneContextMenuEvent, &sipCpp))
        {
            QPointF*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QPointF(sipCpp->pos());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QPointF,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsSceneContextMenuEvent, sipName_pos, doc_QGraphicsSceneContextMenuEvent_pos);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsSceneContextMenuEvent_scenePos, "QGraphicsSceneContextMenuEvent.scenePos() -> QPointF");

extern "C" {static PyObject *meth_QGraphicsSceneContextMenuEvent_scenePos(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsSceneContextMenuEvent_scenePos(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QGraphicsSceneContextMenuEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QGraphicsSceneContextMenuEvent, &sipCpp))
        {
            QPointF*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QPointF(sipCpp->scenePos());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QPointF,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsSceneContextMenuEvent, sipName_scenePos, doc_QGraphicsSceneContextMenuEvent_scenePos);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsSceneContextMenuEvent_screenPos, "QGraphicsSceneContextMenuEvent.screenPos() -> QPoint");

extern "C" {static PyObject *meth_QGraphicsSceneContextMenuEvent_screenPos(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsSceneContextMenuEvent_screenPos(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QGraphicsSceneContextMenuEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QGraphicsSceneContextMenuEvent, &sipCpp))
        {
            QPoint*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QPoint(sipCpp->screenPos());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QPoint,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsSceneContextMenuEvent, sipName_screenPos, doc_QGraphicsSceneContextMenuEvent_screenPos);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsSceneContextMenuEvent_modifiers, "QGraphicsSceneContextMenuEvent.modifiers() -> Qt.KeyboardModifiers");

extern "C" {static PyObject *meth_QGraphicsSceneContextMenuEvent_modifiers(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsSceneContextMenuEvent_modifiers(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QGraphicsSceneContextMenuEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QGraphicsSceneContextMenuEvent, &sipCpp))
        {
            Qt::KeyboardModifiers*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new Qt::KeyboardModifiers(sipCpp->modifiers());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_Qt_KeyboardModifiers,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsSceneContextMenuEvent, sipName_modifiers, doc_QGraphicsSceneContextMenuEvent_modifiers);

    return NULL;
}


PyDoc_STRVAR(doc_QGraphicsSceneContextMenuEvent_reason, "QGraphicsSceneContextMenuEvent.reason() -> QGraphicsSceneContextMenuEvent.Reason");

extern "C" {static PyObject *meth_QGraphicsSceneContextMenuEvent_reason(PyObject *, PyObject *);}
static PyObject *meth_QGraphicsSceneContextMenuEvent_reason(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QGraphicsSceneContextMenuEvent *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QGraphicsSceneContextMenuEvent, &sipCpp))
        {
            QGraphicsSceneContextMenuEvent::Reason sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->reason();
            Py_END_ALLOW_THREADS

            return sipConvertFromEnum(sipRes,sipType_QGraphicsSceneContextMenuEvent_Reason);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QGraphicsSceneContextMenuEvent, sipName_reason, doc_QGraphicsSceneContextMenuEvent_reason);

    return NULL;
}


/* Cast a pointer to a type somewhere in its superclass hierarchy. */
extern "C" {static void *cast_QGraphicsSceneContextMenuEvent(void *, const sipTypeDef *);}
static void *cast_QGraphicsSceneContextMenuEvent(void *ptr, const sipTypeDef *targetType)
{
    void *res;

    if (targetType == sipType_QGraphicsSceneContextMenuEvent)
        return ptr;

    if ((res = ((const sipClassTypeDef *)sipType_QGraphicsSceneEvent)->ctd_cast((QGraphicsSceneEvent *)(QGraphicsSceneContextMenuEvent *)ptr,targetType)) != NULL)
        return res;

    return NULL;
}


/* Call the instance's destructor. */
extern "C" {static void release_QGraphicsSceneContextMenuEvent(void *, int);}
static void release_QGraphicsSceneContextMenuEvent(void *sipCppV,int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<QGraphicsSceneContextMenuEvent *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_QGraphicsSceneContextMenuEvent(sipSimpleWrapper *);}
static void dealloc_QGraphicsSceneContextMenuEvent(sipSimpleWrapper *sipSelf)
{
    if (sipIsPyOwned(sipSelf))
    {
        release_QGraphicsSceneContextMenuEvent(sipGetAddress(sipSelf),0);
    }
}


/* Define this type's super-types. */
static sipEncodedTypeDef supers_QGraphicsSceneContextMenuEvent[] = {{200, 255, 1}};


static PyMethodDef methods_QGraphicsSceneContextMenuEvent[] = {
    {SIP_MLNAME_CAST(sipName_modifiers), meth_QGraphicsSceneContextMenuEvent_modifiers, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsSceneContextMenuEvent_modifiers)},
    {SIP_MLNAME_CAST(sipName_pos), meth_QGraphicsSceneContextMenuEvent_pos, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsSceneContextMenuEvent_pos)},
    {SIP_MLNAME_CAST(sipName_reason), meth_QGraphicsSceneContextMenuEvent_reason, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsSceneContextMenuEvent_reason)},
    {SIP_MLNAME_CAST(sipName_scenePos), meth_QGraphicsSceneContextMenuEvent_scenePos, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsSceneContextMenuEvent_scenePos)},
    {SIP_MLNAME_CAST(sipName_screenPos), meth_QGraphicsSceneContextMenuEvent_screenPos, METH_VARARGS, SIP_MLDOC_CAST(doc_QGraphicsSceneContextMenuEvent_screenPos)}
};

static sipEnumMemberDef enummembers_QGraphicsSceneContextMenuEvent[] = {
    {sipName_Keyboard, static_cast<int>(QGraphicsSceneContextMenuEvent::Keyboard), 198},
    {sipName_Mouse, static_cast<int>(QGraphicsSceneContextMenuEvent::Mouse), 198},
    {sipName_Other, static_cast<int>(QGraphicsSceneContextMenuEvent::Other), 198},
};


pyqt4ClassTypeDef sipTypeDef_QtGui_QGraphicsSceneContextMenuEvent = {
{
    {
        -1,
        0,
        0,
        SIP_TYPE_SCC|SIP_TYPE_CLASS,
        sipNameNr_QGraphicsSceneContextMenuEvent,
        {0}
    },
    {
        sipNameNr_QGraphicsSceneContextMenuEvent,
        {0, 0, 1},
        5, methods_QGraphicsSceneContextMenuEvent,
        3, enummembers_QGraphicsSceneContextMenuEvent,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    0,
    -1,
    -1,
    supers_QGraphicsSceneContextMenuEvent,
    0,
    0,
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
    dealloc_QGraphicsSceneContextMenuEvent,
    0,
    0,
    0,
    release_QGraphicsSceneContextMenuEvent,
    cast_QGraphicsSceneContextMenuEvent,
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