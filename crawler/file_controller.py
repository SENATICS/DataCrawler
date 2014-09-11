__author__ = 'Verena Ojeda'

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
        file =  domain + ".json"
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
        file_response = codecs.open(filename, 'w+', 'utf-8-sig')
        if to_json == True:
            file_response.write(json.dumps(response.json(), indent=2, ensure_ascii=False))
        else:
            file_response.write(json.dumps(response, indent=2, ensure_ascii=False))
        return filename