# -*- coding: utf-8 -*-
from scrapy import Spider
import re
from bs4 import BeautifulSoup as bs
from rgr.items import RgrItem


class DadosSpider(Spider):
    name = 'dados'

    def __init__(self, filename=None):
        if filename:
            with open(filename) as f:
                self.start_urls = [url.strip() for url in f.readlines()]
        else:
            self.start_urls = [
                'https://www.cialdnb.com/'
            ]

    def parse(self, response):
        html_to_texto = response.text
        search = ['img', 'src', 'logo']
        pattern = r'(\+[0-9]{1,2}\s)?(\(?\d{1,3}\)?\s)(\d{3,4})(-\d{2,4})?(-\d{2})?'
        src = ''
        lista_telefone = []
        for linha in html_to_texto.split('\n'):
            res = [ele for ele in search if (ele in linha)]
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
            matchs = re.search(pattern, linha)
            try:
                phone = matchs.group()
                lista_telefone.append(phone)
            except AttributeError:
                pass
        yield RgrItem(
            website=response.url,
            telefone=lista_telefone,
            logo=src
        )
