# -*- coding: utf-8 -*-
#
# @author	Rodrigo Parra
# @copyright	2014 Governance and Democracy Program USAID-CEAMSO
# @license 	http://www.gnu.org/licenses/gpl-2.0.html
#
# USAID-CEAMSO
# Copyright (C) 2014 Governance and Democracy Program
# http://ceamso.org.py/es/proyectos/20-programa-de-democracia-y-gobernabilidad
#
#----------------------------------------------------------------------------
# This file is part of the Governance and Democracy Program USAID-CEAMSO,
# is distributed as free software in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License version 2 as published by the
# Free Software Foundation, accessible from <http://www.gnu.org/licenses/> or write
# to Free Software Foundation (FSF) Inc., 51 Franklin St, Fifth Floor, Boston,
# MA 02111-1301, USA.
#---------------------------------------------------------------------------
# Este archivo es parte del Programa de Democracia y Gobernabilidad USAID-CEAMSO,
# es distribuido como software libre con la esperanza que sea de utilidad,
# pero sin NINGUNA GARANTÍA; sin garantía alguna implícita de ADECUACION a cualquier
# MERCADO o APLICACION EN PARTICULAR. Usted puede redistribuirlo y/o modificarlo
# bajo los términos de la GNU Lesser General Public Licence versión 2 de la Free
# Software Foundation, accesible en <http://www.gnu.org/licenses/> o escriba a la
# Free Software Foundation (FSF) Inc., 51 Franklin St, Fifth Floor, Boston,
# MA 02111-1301, USA.
#
__author__ = 'Rodrigo Parra'

import codecs
import os
import time

try:
    import json
except ImportError:
    import simplejson as json


class FileController:
    def clean_tmp_files(self):
        """
        Elimina los archivos temporales utilizados por el spider.
        """
        if os.path.exists("aux.html"):
            os.remove("aux.html")
        if os.path.exists("splash.html"):
            os.remove("splash.html")


    def clean_item_tmp_file(self, domain):
        """
        Elimina los archivos temporales utilizados por el spider.
        """
        file = domain + ".json"
        if os.path.exists(file):
            os.remove(file)


    def save_existing_data_json(self, response, domain, to_json):
        """
        Guarda un data.json nuevo y/o existente.
        """
        principal = "results_" + time.strftime("%d_%m_%y")
        if not os.path.exists(principal):
            os.makedirs(principal)
        subprincipal = principal + "/" + domain
        if not os.path.exists(subprincipal):
            os.makedirs(subprincipal)
        filename = subprincipal + "/" + "data.json"
        # file_response = codecs.open(filename, 'w+', 'utf-8-sig')
        file_response = open(filename, 'w+')
        if to_json == True:
            file_response.write(json.dumps(response.json(), indent=2, ensure_ascii=False))
            file_response.close()
        else:
            file_response.write(json.dumps(response, indent=2, ensure_ascii=False))
            file_response.close()
        return filename