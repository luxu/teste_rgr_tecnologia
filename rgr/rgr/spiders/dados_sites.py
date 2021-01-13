# -*- coding: utf-8 -*-
from scrapy import Spider
import re
from bs4 import BeautifulSoup as bs
from rgr.items import RgrItem


class DadosSpider(Spider):
    name = 'dados'
    # filename = '../../websites.txt'
    start_urls = [
        'https://www.imobiliariasistema.com.br/'
    ]
    # with open(filename, encoding='utf-8') as _f:
    #     urls = _f.read()
    # for url in urls.split('\n'):
    #     start_urls.append(url)

    def parse(self, response):
        html_to_texto = response.text
        search = ['img', 'src', 'logo']
        pattern = r"(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})"
        src = ''
        lista_telefone = []
        for linha in html_to_texto.split('\n'):
            res = [ele for ele in search if (ele in linha)]
            matchs = re.search(pattern, linha)
            if len(res) == len(search):
                soup = bs(linha, 'html.parser')
                img_ = soup.img
                try:
                    tag = img_.attrs
                    try:
                        src = tag['src']
                        if not src.startswith('http'):
                            src = ''.join((response.url, src))
                    except KeyError:
                        response.url
                except AttributeError:
                    response.url
            if '0800 ' in linha:
                telefone = re.sub('[^0-9]', ' ', linha)
                telefone = telefone.strip()
                lista_telefone.append(telefone)
            if matchs:
                # if 'telep' in linha or 'telef' in linha:
                telefone = re.sub('[^0-9]', ' ', linha)
                telefone = telefone.strip()
                lista_telefone.append(telefone)
        yield RgrItem(
            website=response.url,
            telefone=lista_telefone,
            logo=src
        )
