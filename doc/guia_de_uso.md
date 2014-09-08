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

 `$ install.sh path_to_your_virtualenv_site_packages`

Ejecución y uso
---------------

1. Activar el entorno virtual:

 `$ source path_to_datacrawler/bin/`

2. Crear el archivo con la lista de dominios sobre los cuales se realizará el crawling. La lista debe contener los diferentes dominios, separados por saltos de línea. Ejemplo:

 Nombre del archivo: domains.txt
 
 Contenido:

 mec.gov.py

 datos.gov.py

3. Ingresar al directorio DataCrawler/bin y ejecutar el siguiente comando en una terminal:

 `$ python DataCrawler/bin/DataCrawler.py --file=path_to_your_file_with_domains_to_crawl`

Para el ejemplo de más arriba el comando sería el siguiente:

 `$ python DataCrawler/bin/DataCrawler.py --file=domains.txt`

**Observación**: el archivo con la lista de dominos no necesiar estar necesariamente dentro del directorio del DataCrawler, por lo cual siempre se debe especificar la ruta absoluta del archivo.

Resultados
----------

Para cada dominio de la lista se retornan dos archivos. Un archivo `domain.json` que contiene los datos extraídos a partir de las anotaciones microdata. Y un archivo `domain_data.json` que contiene la conversión del archivo `domain.json` correspondiente al formato POD (Project Open Data).