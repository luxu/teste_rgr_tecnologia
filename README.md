# Test 

* Install Lib virtualenv
````
pip3 install virtualenv
````
* Create the virtual environment
````
virtualenv .venv
````
* Run the `` requirements.txt`` file to install the libs for the project
````
  pip install -r requirements.txt
````
* Run the command to get the data and save it in the JSON file
````
  scrapy crawl dados -a filename=websites.txt -o result.json -t json   
````
