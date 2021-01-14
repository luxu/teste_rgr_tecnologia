# -*- coding: utf-8 -*-
from scrapy import Spider
import re
from bs4 import BeautifulSoup as bs
from rgr.items import RgrItem
import os

class DadosSpider(Spider):
    name = 'dados'


    def __init__(self, filename=None):
        if filename:
            with open(filename) as f:
                self.start_urls = [url.strip() for url in f.readlines()]
        else:
            self.start_urls = [
                'https://www.caixa.gov.br/atendimento/Paginas/default.aspx'
            ]

    def parse(self, response):
        html_to_texto = response.text
        search = ['img', 'src', 'logo']
        pattern = r"(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})"
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
            pattern_0800 = ''
            if '0800- ' in linha:
                telefone = re.sub('[^0-9]', ' ', linha)
                telefone = telefone.strip()
                lista_telefone.append(telefone)
            else:
                matchs = re.search(pattern, linha)
                try:
                    phone = matchs.group()
                    lista_telefone.append(phone)
                except AttributeError:
                    pass
            # if len(phone) > 0:
                # if 'telep' in linha or 'telef' in linha:
                # telefone = re.sub('[^0-9]', ' ', linha)
                # telefone = telefone.strip()
                # lista_telefone.append(telefone)
        yield RgrItem(
            website=response.url,
            telefone=lista_telefone,
            logo=src
        )
