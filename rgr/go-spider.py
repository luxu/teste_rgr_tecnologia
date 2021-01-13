from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from rgr.spiders.dados_sites import DadosSpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(DadosSpider)
process.start()