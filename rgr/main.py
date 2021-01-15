from scrapy import cmdline

cmdline.execute("scrapy crawl dados -a filename=websites.txt -o result.json -t json".split())
