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

#line 159 "/home/desa2/PyQt-x11-gpl-4.10.4/sip/QtCore/qobjectdefs.sip"
#include <qobjectdefs.h>
#line 34 "/home/desa2/PyQt-x11-gpl-4.10.4/QtCore/sipQtCoreQGenericArgument.cpp"



/* Cast a pointer to a type somewhere in its superclass hierarchy. */
extern "C" {static void *cast_QGenericArgument(void *, const sipTypeDef *);}
static void *cast_QGenericArgument(void *ptr, const sipTypeDef *targetType)
{
    if (targetType == sipType_QGenericArgument)
        return ptr;

    return NULL;
}


/* Call the instance's destructor. */
extern "C" {static void release_QGenericArgument(void *, int);}
static void release_QGenericArgument(void *sipCppV,int)
{
    Py_BEGIN_ALLOW_THREADS

    delete reinterpret_cast<QGenericArgument *>(sipCppV);

    Py_END_ALLOW_THREADS
}


extern "C" {static void dealloc_QGenericArgument(sipSimpleWrapper *);}
static void dealloc_QGenericArgument(sipSimpleWrapper *sipSelf)
{
    if (sipIsPyOwned(sipSelf))
    {
        release_QGenericArgument(sipGetAddress(sipSelf),0);
    }
}


pyqt4ClassTypeDef sipTypeDef_QtCore_QGenericArgument = {
{
    {
        -1,
        0,
        0,
        SIP_TYPE_CLASS,
        sipNameNr_QGenericArgument,
        {0}
    },
    {
        sipNameNr_QGenericArgument,
        {0, 0, 1},
        0, 0,
        0, 0,
        0, 0,
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    },
    0,
    sipNameNr_PyQt4_QtCore_pyqtWrapperType,
    sipNameNr_sip_simplewrapper,
    0,
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
    dealloc_QGenericArgument,
    0,
    0,
    0,
    release_QGenericArgument,
    cast_QGenericArgument,
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