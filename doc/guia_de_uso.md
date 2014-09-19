Manual de uso - DataCrawler
=========================

Instalación
-----------

1. Crear un entorno virtual:

 `$ virtualenv datacrawler`

2. Activar el entorno virtual:

 `$ source path_to_datacrawler/bin/activate`

3. Clonar el repositorio:

 `$ git clone https://github.com/DataCrawler.git`

4. Instalar el módulo:

 `$ cd DataCrawler`

 `$ ./install.sh path_to_datacrawler`
 
 `$ python setup.py develop`
 

Ejecución y uso
---------------

1. Activar el entorno virtual:

 `$ source path_to_datacrawler/bin/activate`
 
2. Modificar el archivo settings.py

 Mover el archivo settings-example.py a settings.py y modificar los valores especificados más abajo según las configuraciones locales:

    SPLASH_URL: URL donde se levanta el servidor splash
    
    CATALOG_URL: URL del Catálogo de Datos Nacional
    
    API_KEY: API Key del Catálogo de Datos Nacional
    
 **Ejemplo**
    
    SPLASH_URL: ‘http://localhost:8050/’
    
    CATALOG_URL: ‘http://www.example.com/api/3/action/’
    
    API_KEY: ‘1a2b3456-c7d8-91ef-a234-b567cd891e23’

3. Crear el archivo con la lista de dominios sobre los cuales se realizará el crawling. La lista debe contener los diferentes dominios, separados por saltos de línea. Ejemplo:

 **Ejemplo**
 
 Nombre del archivo: domains.txt
 
 Contenido:

 mec.gov.py

 datos.gov.py
 
4. Ingresar al directorio DataCrawler/bin y ejecutar el siguiente comando en una terminal:

 `$ python DataCrawler/bin/DataCrawler.py --file=path_to_your_file_with_domains_to_crawl --virtualenv path_to_your_virtual_enviroment`

**Observaciones** 

**path_to_your_file_with_domains_to_crawl**: ruta absoluta a la ubicación del arhcivo que contiene la lista de los dominios sobre los cuales se realizará el crawling.

**path_to_your_virtual_enviroment**: ruta absoluta a la ubicación del entorno virtual donde se instaló el DataCrawler.

Resultados
----------

Para cada dominio de la búsqueda se crea un directorio con el nombre del dominio, el cual contiene dentro un archivo data.json estandarizado según el formato propuesto por Project Open Data. Luego, por cada uno de los archivos generados se realiza el proceso de conversión para transferirlos al Catálogo de Datos Nacional. Por cada dataset encontrado dentro del archivo data.json, la herramienta por línea de comandos pregunta si se desea o no crear/actualizar el dataset en el Catálogo de Datos Nacional.