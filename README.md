# Scraps for website information 

* Install Lib ``venv``
````
apt-get update
apt-get install libpython3-dev
apt-get install python3-venv
````
* Entry in folder
````
cd teste_rgr_tecnologia
````
* Create the virtual environment
````
python3 -m venv .venv
````
* Access the virtual environment
````
source .venv/bin/activate
````
* Run the `` requirements.txt`` file to install the libs for the project
````
  pip install -r requirements.txt
````
* Access folder ``rgr``
````
cd rgr
````
* Run the command to get the data and save it in the JSON file
````
  scrapy crawl dados -a filename=websites.txt -o result.json -t json   
````

## Docker

Build image
``
docker build -t mycrawler .
``

Generate Data
``
docker run mycrawler
``

Important! It generates the file called result.json inside the rgr folder. 

## That´s all Folks