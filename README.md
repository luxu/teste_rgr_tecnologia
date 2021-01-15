# Test 

* Install Lib virtualenv
````
pip3 install virtualenv
````
* Create the virtual environment
````
virtualenv .venv
````
* Execute o arquivo ``requirements.txt`` para instalar as libs para o projeto
````
  pip install -r requirements.txt
````
* Execute o comando para pegar os dados e salvar no arquivo JSON
````
  scrapy crawl dados -a filename=websites.txt -o result.json -t json   
````