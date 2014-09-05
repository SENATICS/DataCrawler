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

#line 35 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtGui/qitemselectionmodel.sip"
#include <qitemselectionmodel.h>
#line 34 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQItemSelectionRange.cpp"

#line 31 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qabstractitemmodel.sip"
#include <qabstractitemmodel.h>
#line 38 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQItemSelectionRange.cpp"
#line 33 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qlist.sip"
#include <qlist.h>
#line 41 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQItemSelectionRange.cpp"
#line 127 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qabstractitemmodel.sip"
#include <qabstractitemmodel.h>
#line 44 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQItemSelectionRange.cpp"


PyDoc_STRVAR(doc_QItemSelectionRange_top, "QItemSelectionRange.top() -> int");

extern "C" {static PyObject *meth_QItemSelectionRange_top(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_top(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QItemSelectionRange, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->top();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_top, doc_QItemSelectionRange_top);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_left, "QItemSelectionRange.left() -> int");

extern "C" {static PyObject *meth_QItemSelectionRange_left(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_left(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QItemSelectionRange, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->left();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_left, doc_QItemSelectionRange_left);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_bottom, "QItemSelectionRange.bottom() -> int");

extern "C" {static PyObject *meth_QItemSelectionRange_bottom(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_bottom(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QItemSelectionRange, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->bottom();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_bottom, doc_QItemSelectionRange_bottom);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_right, "QItemSelectionRange.right() -> int");

extern "C" {static PyObject *meth_QItemSelectionRange_right(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_right(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QItemSelectionRange, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->right();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_right, doc_QItemSelectionRange_right);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_width, "QItemSelectionRange.width() -> int");

extern "C" {static PyObject *meth_QItemSelectionRange_width(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_width(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QItemSelectionRange, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->width();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_width, doc_QItemSelectionRange_width);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_height, "QItemSelectionRange.height() -> int");

extern "C" {static PyObject *meth_QItemSelectionRange_height(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_height(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QItemSelectionRange, &sipCpp))
        {
            int sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->height();
            Py_END_ALLOW_THREADS

            return SIPLong_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_height, doc_QItemSelectionRange_height);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_topLeft, "QItemSelectionRange.topLeft() -> QModelIndex");

extern "C" {static PyObject *meth_QItemSelectionRange_topLeft(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_topLeft(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QItemSelectionRange, &sipCpp))
        {
            QModelIndex*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QModelIndex(sipCpp->topLeft());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QModelIndex,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_topLeft, doc_QItemSelectionRange_topLeft);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_bottomRight, "QItemSelectionRange.bottomRight() -> QModelIndex");

extern "C" {static PyObject *meth_QItemSelectionRange_bottomRight(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_bottomRight(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QItemSelectionRange, &sipCpp))
        {
            QModelIndex*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QModelIndex(sipCpp->bottomRight());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QModelIndex,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_bottomRight, doc_QItemSelectionRange_bottomRight);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_parent, "QItemSelectionRange.parent() -> QModelIndex");

extern "C" {static PyObject *meth_QItemSelectionRange_parent(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_parent(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QItemSelectionRange, &sipCpp))
        {
            QModelIndex*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QModelIndex(sipCpp->parent());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QModelIndex,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_parent, doc_QItemSelectionRange_parent);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_model, "QItemSelectionRange.model() -> QAbstractItemModel");

extern "C" {static PyObject *meth_QItemSelectionRange_model(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_model(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QItemSelectionRange, &sipCpp))
        {
            const QAbstractItemModel*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->model();
            Py_END_ALLOW_THREADS

            return sipConvertFromType(const_cast<QAbstractItemModel *>(sipRes),sipType_QAbstractItemModel,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_model, doc_QItemSelectionRange_model);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_contains, "QItemSelectionRange.contains(QModelIndex) -> bool\n"
    "QItemSelectionRange.contains(int, int, QModelIndex) -> bool");

extern "C" {static PyObject *meth_QItemSelectionRange_contains(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_contains(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QModelIndex* a0;
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ9", &sipSelf, sipType_QItemSelectionRange, &sipCpp, sipType_QModelIndex, &a0))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->contains(*a0);
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    {
        int a0;
        int a1;
        const QModelIndex* a2;
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BiiJ9", &sipSelf, sipType_QItemSelectionRange, &sipCpp, &a0, &a1, sipType_QModelIndex, &a2))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->contains(a0,a1,*a2);
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_contains, doc_QItemSelectionRange_contains);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_intersects, "QItemSelectionRange.intersects(QItemSelectionRange) -> bool");

extern "C" {static PyObject *meth_QItemSelectionRange_intersects(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_intersects(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange* a0;
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ9", &sipSelf, sipType_QItemSelectionRange, &sipCpp, sipType_QItemSelectionRange, &a0))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->intersects(*a0);
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_intersects, doc_QItemSelectionRange_intersects);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_intersect, "QItemSelectionRange.intersect(QItemSelectionRange) -> QItemSelectionRange");

extern "C" {static PyObject *meth_QItemSelectionRange_intersect(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_intersect(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange* a0;
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ9", &sipSelf, sipType_QItemSelectionRange, &sipCpp, sipType_QItemSelectionRange, &a0))
        {
            QItemSelectionRange*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QItemSelectionRange(sipCpp->intersect(*a0));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QItemSelectionRange,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_intersect, doc_QItemSelectionRange_intersect);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_isValid, "QItemSelectionRange.isValid() -> bool");

extern "C" {static PyObject *meth_QItemSelectionRange_isValid(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_isValid(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QItemSelectionRange, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->isValid();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_isValid, doc_QItemSelectionRange_isValid);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_indexes, "QItemSelectionRange.indexes() -> list-of-QModelIndex");

extern "C" {static PyObject *meth_QItemSelectionRange_indexes(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_indexes(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QItemSelectionRange, &sipCpp))
        {
            QModelIndexList*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QModelIndexList(sipCpp->indexes());
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QList_0100QModelIndex,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_indexes, doc_QItemSelectionRange_indexes);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_intersected, "QItemSelectionRange.intersected(QItemSelectionRange) -> QItemSelectionRange");

extern "C" {static PyObject *meth_QItemSelectionRange_intersected(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_intersected(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange* a0;
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "BJ9", &sipSelf, sipType_QItemSelectionRange, &sipCpp, sipType_QItemSelectionRange, &a0))
        {
            QItemSelectionRange*sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = new QItemSelectionRange(sipCpp->intersected(*a0));
            Py_END_ALLOW_THREADS

            return sipConvertFromNewType(sipRes,sipType_QItemSelectionRange,NULL);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_intersected, doc_QItemSelectionRange_intersected);

    return NULL;
}


PyDoc_STRVAR(doc_QItemSelectionRange_isEmpty, "QItemSelectionRange.isEmpty() -> bool");

extern "C" {static PyObject *meth_QItemSelectionRange_isEmpty(PyObject *, PyObject *);}
static PyObject *meth_QItemSelectionRange_isEmpty(PyObject *sipSelf, PyObject *sipArgs)
{
    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange *sipCpp;

        if (sipParseArgs(&sipParseErr, sipArgs, "B", &sipSelf, sipType_QItemSelectionRange, &sipCpp))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->isEmpty();
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    /* Raise an exception if the arguments couldn't be parsed. */
    sipNoMethod(sipParseErr, sipName_QItemSelectionRange, sipName_isEmpty, doc_QItemSelectionRange_isEmpty);

    return NULL;
}


extern "C" {static PyObject *slot_QItemSelectionRange___ge__(PyObject *,PyObject *);}
static PyObject *slot_QItemSelectionRange___ge__(PyObject *sipSelf,PyObject *sipArg)
{
    QItemSelectionRange *sipCpp = reinterpret_cast<QItemSelectionRange *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QItemSelectionRange));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange* a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J9", sipType_QItemSelectionRange, &a0))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = !sipCpp->QItemSelectionRange::operator<(*a0);
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtGui,ge_slot,sipType_QItemSelectionRange,sipSelf,sipArg);
}


extern "C" {static PyObject *slot_QItemSelectionRange___lt__(PyObject *,PyObject *);}
static PyObject *slot_QItemSelectionRange___lt__(PyObject *sipSelf,PyObject *sipArg)
{
    QItemSelectionRange *sipCpp = reinterpret_cast<QItemSelectionRange *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QItemSelectionRange));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange* a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J9", sipType_QItemSelectionRange, &a0))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->QItemSelectionRange::operator<(*a0);
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtGui,lt_slot,sipType_QItemSelectionRange,sipSelf,sipArg);
}


extern "C" {static long slot_QItemSelectionRange___hash__(PyObject *);}
static long slot_QItemSelectionRange___hash__(PyObject *sipSelf)
{
    QItemSelectionRange *sipCpp = reinterpret_cast<QItemSelectionRange *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QItemSelectionRange));

    if (!sipCpp)
        return 0;


    {
        {
            long sipRes = 0;

#line 80 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtGui/qitemselectionmodel.sip"
        sipRes = qHash(*sipCpp);
#line 646 "/home/desa2/PyQt-x11-gpl-4.10.4/QtGui/sipQtGuiQItemSelectionRange.cpp"

            return sipRes;
        }
    }

    return 0;
}


extern "C" {static PyObject *slot_QItemSelectionRange___ne__(PyObject *,PyObject *);}
static PyObject *slot_QItemSelectionRange___ne__(PyObject *sipSelf,PyObject *sipArg)
{
    QItemSelectionRange *sipCpp = reinterpret_cast<QItemSelectionRange *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QItemSelectionRange));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange* a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J9", sipType_QItemSelectionRange, &a0))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->QItemSelectionRange::operator!=(*a0);
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtGui,ne_slot,sipType_QItemSelectionRange,sipSelf,sipArg);
}


extern "C" {static PyObject *slot_QItemSelectionRange___eq__(PyObject *,PyObject *);}
static PyObject *slot_QItemSelectionRange___eq__(PyObject *sipSelf,PyObject *sipArg)
{
    QItemSelectionRange *sipCpp = reinterpret_cast<QItemSelectionRange *>(sipGetCppPtr((sipSimpleWrapper *)sipSelf,sipType_QItemSelectionRange));

    if (!sipCpp)
        return 0;

    PyObject *sipParseErr = NULL;

    {
        const QItemSelectionRange* a0;

        if (sipParseArgs(&sipParseErr, sipArg, "1J9", sipType_QItemSelectionRange, &a0))
        {
            bool sipRes;

            Py_BEGIN_ALLOW_THREADS
            sipRes = sipCpp->QItemSelectionRange::operator==(*a0);
            Py_END_ALLOW_THREADS

            return PyBool_FromLong(sipRes);
        }
    }

    Py_XDECREF(sipParseErr);

    if (sipParseErr == Py_None)
        return NULL;

    return sipPySlotExtend(&sipModuleAPI_QtGui,eq_slot,sipType_QItemSelectionRange,sipSelf,sipArg);
}


/* Cast a pointer to a type somewhere in its superclass hierarchy. */
extern "C" {static void *cast_QItemSelectionRange(void *, const sipTypeDef *);}
static void *cast_QItemSelectionRange(void *ptr, const sipTypeDef *targetType)
{
    if (targetType == sipType_QItemSelectionRange)
        return ptr;

    return NULL;
}


/* Call the instance's destructor. */
extern "C" {static void release_QItemSelectionRange(void *, int);}
static void release_QItemSelectionRange(void *sipCppV,int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<QItemSelectionRange *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void assign_QItemSelectionRange(void *, SIP_SSIZE_T, const void *);}
static void assign_QItemSelectionRange(void *sipDst, SIP_SSIZE_T sipDstIdx, const void *sipSrc)
{
    reinterpret_cast<QItemSelectionRange *>(sipDst)[sipDstIdx] = *reinterpret_cast<const QItemSelectionRange *>(sipSrc);
}


extern "C" {static void *array_QItemSelectionRange(SIP_SSIZE_T);}
static void *array_QItemSelectionRange(SIP_SSIZE_T sipNrElem)
{
    return new QItemSelectionRange[sipNrElem];
}


extern "C" {static void *copy_QItemSelectionRange(const void *, SIP_SSIZE_T);}
static void *copy_QItemSelectionRange(const void *sipSrc, SIP_SSIZE_T sipSrcIdx)
{
    return new QItemSelectionRange(reinterpret_cast<const QItemSelectionRange *>(sipSrc)[sipSrcIdx]);
}


extern "C" {static void dealloc_QItemSelectionRange(sipSimpleWrapper *);}
static void dealloc_QItemSelectionRange(sipSimpleWrapper *sipSelf)
{
    if (sipIsPyOwned(sipSelf))
    {
        release_QItemSelectionRange(sipGetAddress(sipSelf),0);
    }
}


extern "C" {static void *init_type_QItemSelectionRange(sipSimpleWrapper *, PyObject *, PyObject *, PyObject **, PyObject **, PyObject **);}
static void *init_type_QItemSelectionRange(sipSimpleWrapper *, PyObject *sipArgs, PyObject *sipKwds, PyObject **sipUnused, PyObject **, PyObject **sipParseErr)
{
    QItemSelectionRange *sipCpp = 0;

    {
        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, ""))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new QItemSelectionRange();
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        const QItemSelectionRange* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J9", sipType_QItemSelectionRange, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new QItemSelectionRange(*a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        const QModelIndex* a0;
        const QModelIndex* a1;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J9J9", sipType_QModelIndex, &a0, sipType_QModelIndex, &a1))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new QItemSelectionRange(*a0,*a1);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    {
        const QModelIndex* a0;

        if (sipParseKwdArgs(sipParseErr, sipArgs, sipKwds, NULL, sipUnused, "J9", sipType_QModelIndex, &a0))
        {
            Py_BEGIN_ALLOW_THREADS
            sipCpp = new QItemSelectionRange(*a0);
            Py_END_ALLOW_THREADS

            return sipCpp;
        }
    }

    return NULL;
}


/* Define this type's Python slots. */
static sipPySlotDef slots_QItemSelectionRange[] = {
    {(void *)slot_QItemSelectionRange___ge__, ge_slot},
    {(void *)slot_QItemSelectionRange___lt__, lt_slot},
    {(void *)slot_QItemSelectionRange___hash__, hash_slot},
    {(void *)slot_QItemSelectionRange___ne__, ne_slot},
    {(void *)slot_QItemSelectionRange___eq__, eq_slot},
    {0, (sipPySlotType)0}
};


static PyMethodDef methods_QItemSelectionRange[] = {
    {SIP_MLNAME_CAST(sipName_bottom), meth_QItemSelectionRange_bottom, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_bottom)},
    {SIP_MLNAME_CAST(sipName_bottomRight), meth_QItemSelectionRange_bottomRight, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_bottomRight)},
    {SIP_MLNAME_CAST(sipName_contains), meth_QItemSelectionRange_contains, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_contains)},
    {SIP_MLNAME_CAST(sipName_height), meth_QItemSelectionRange_height, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_height)},
    {SIP_MLNAME_CAST(sipName_indexes), meth_QItemSelectionRange_indexes, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_indexes)},
    {SIP_MLNAME_CAST(sipName_intersect), meth_QItemSelectionRange_intersect, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_intersect)},
    {SIP_MLNAME_CAST(sipName_intersected), meth_QItemSelectionRange_intersected, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_intersected)},
    {SIP_MLNAME_CAST(sipName_intersects), meth_QItemSelectionRange_intersects, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_intersects)},
    {SIP_MLNAME_CAST(sipName_isEmpty), meth_QItemSelectionRange_isEmpty, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_isEmpty)},
    {SIP_MLNAME_CAST(sipName_isValid), meth_QItemSelectionRange_isValid, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_isValid)},
    {SIP_MLNAME_CAST(sipName_left), meth_QItemSelectionRange_left, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_left)},
    {SIP_MLNAME_CAST(sipName_model), meth_QItemSelectionRange_model, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_model)},
    {SIP_MLNAME_CAST(sipName_parent), meth_QItemSelectionRange_parent, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_parent)},
    {SIP_MLNAME_CAST(sipName_right), meth_QItemSelectionRange_right, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_right)},
    {SIP_MLNAME_CAST(sipName_top), meth_QItemSelectionRange_top, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_top)},
    {SIP_MLNAME_CAST(sipName_topLeft), meth_QItemSelectionRange_topLeft, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_topLeft)},
    {SIP_MLNAME_CAST(sipName_width), meth_QItemSelectionRange_width, METH_VARARGS, SIP_MLDOC_CAST(doc_QItemSelectionRange_width)}
};

PyDoc_STRVAR(doc_QItemSelectionRange, "\1QItemSelectionRange()\n"
    "QItemSelectionRange(QItemSelectionRange)\n"
    "QItemSelectionRange(QModelIndex, QModelIndex)\n"
    "QItemSelectionRange(QModelIndex)");


pyqt4ClassTypeDef sipTypeDef_QtGui_QItemSelectionRange = {
{
    {
        -1,
        0,
        0,
        SIP_TYPE_CLASS,
        sipNameNr_QItemSelectionRange,
        {0}
    },
    {
        sipNameNr_QItemSelectionRange,
        {0, 0, 1},
        17, methods_QItemSelectionRange,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    doc_QItemSelectionRange,
    sipNameNr_PyQt4_QtCore_pyqtWrapperType,
    sipNameNr_sip_simplewrapper,
    0,
    slots_QItemSelectionRange,
    init_type_QItemSelectionRange,
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
    dealloc_QItemSelectionRange,
    assign_QItemSelectionRange,
    array_QItemSelectionRange,
    copy_QItemSelectionRange,
    release_QItemSelectionRange,
    cast_QItemSelectionRange,
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