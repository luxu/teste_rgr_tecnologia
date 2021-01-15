from scrapy import cmdline
import os

os.chdir('rgr')
cmdline.execute("scrapy crawl dados -a filename=websites.txt -o result.json -t json".split())
