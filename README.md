DataCrawler
Simple Crawler for Paraguay public information.

Setup and run

1. Install the dependencies. If you are using Ubuntu it is as simple as running:

    sudo apt-get install libffi-dev

2. Also, maybe you have to install or update some extra dependencies, like this:

    sudo apt-get install libxslt1-dev libxslt1.1 libxml2-dev libxml2 libssl-dev

3. And, if you don't have python-dev installed run:

    sudo apt-get install python-dev

4. Clone this repository

    //direccion del repositorio, ejemplo:
    git clone https://github.com/datacrawler.git

5. Install the module with setuptools:

    cd DataCrawler
    python setup.py develop

6. Run DataCrawler in a terminal window:

    python DataCrawler/bin/test.py

TODO (Arreglar esta parte)
1. Add microdata-to-json library
    
    Copy the directory in your workspace and run: 
  
        python setup.py develop
        
2. Add rdfa-to-microdata serializer

    Copy microdata.py file in plugins/serializer of rdflib library

