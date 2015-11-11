DataCrawler
=========

Crawler sencillo para información publica anotada con microdata y rdfa.

Requerimientos
--------------
Ubuntu 12.04 o mayor.
Python 2.7, virtualenv, python-pip, git.

Instalación y Ejecución
-----------------------
1. Crear un entorno virtual de Python
    
 `$ virtualenv datacrawler`
    
2. Activar el entorno virtual
    
 `$ source path_to_datacrawler_venv/bin/activate`

3. Clonar este repositorio

 `$ git clone https://github.com/SENATICS/DataCrawler.git`
    
4. Instalar el módulo correspondiente:

 `$ cd DataCrawler`
    
 `$ ./install.sh path_to_datacrawler_venv`
 
 `$ python setup.py develop`
 
5. Modificar el archivo settings.py

 Mover el archivo settings-example.py a settings.py y modificar los valores especificados más abajo según las configuraciones locales:

    SPLASH_URL: URL donde se levanta el servidor splash
    
    CATALOG_URL: URL del Catálogo de Datos Nacional
    
    API_KEY: API Key del Catálogo de Datos Nacional
    
 **Ejemplo**
    
    SPLASH_URL: ‘http://localhost:8050/’
    
    CATALOG_URL: ‘http://www.example.com/api/3/action/’
    
    API_KEY: ‘1a2b3456-c7d8-91ef-a234-b567cd891e23’

6. Ejecutar DataCrawler en una terminal:

 `$ python DataCrawler/bin/DataCrawler.py --file=path_to_your_file_with_domains_to_crawl --virtualenv path_to_datacrawler_venv`

Documentación
------------

El manual de usuario en formato PDF, que acompaña el código fuente de esta herramienta, se encuentra en el directorio **doc** de este repositorio.
 
 **Observaciones** 

 **path_to_your_file_with_domains_to_crawl**: ruta absoluta a la ubicación del arhcivo que contiene la lista de los dominios sobre los cuales se realizará el crawling.

 **path_to_datacrawler_venv**: ruta absoluta a la ubicación del entorno virtual donde se instaló el DataCrawler.
