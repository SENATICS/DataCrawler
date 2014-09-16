DataCrawler
=========

Simple crawler for public information annotated with microdata.

Setup and run
------------
1. Create a python virtual enviroment
    
 `$ virtualenv datacrawler`
    
2. Activate the virtual enviroment
    
 `$ source path_to_datacrawler/bin/activate`

3. Clone this repository

 `$ git clone https://github.com/DataCrawler.git`
    
4. Install the module:

 `$ cd DataCrawler`
    
 `$ install.sh path_to_datacrawler`
 
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

6. Run DataCrawler in a terminal window:

 `$ python DataCrawler/bin/DataCrawler.py --file=path_to_your_file_with_domains_to_crawl --virtualenv path_to_your_virtual_enviroment`
 
 **Observaciones** 

 **path_to_your_file_with_domains_to_crawl**: ruta absoluta a la ubicación del arhcivo que contiene la lista de los dominios sobre los cuales se realizará el crawling.

 **path_to_your_virtual_enviroment**: ruta absoluta a la ubicación del entorno virtual donde se instaló el DataCrawler.
