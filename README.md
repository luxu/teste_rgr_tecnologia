# Teste na Rgr Tecnologia

* Instalar o virtualenv
````
pip3 install virtualenv
````
* Crie o ambiente virtual
````
virtualenv .venv
````
* Execute o arquivo ``requirements.txt`` para instalar as libs para o projeto
````
  pip install -r requirements.txt
````
* Execute o comando para pegar os dados e salvar no arquivo JSON
````
  scrapy crawl dados -a filename=<nome-do-arquivo> -o result.json -t json   
````