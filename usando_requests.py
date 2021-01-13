import re
from datetime import datetime
from requests import get
from time import sleep
from bs4 import BeautifulSoup as bs

def getTelephone(urls):
    for url in urls.split('\n'):
        try:
            html = get(url)
            html_to_texto = html.content.decode('utf-8')
            pattern = '(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})'
            for linha in html_to_texto.split('\n'):
                matchs = re.search(pattern, linha)
                if '0800 ' in linha:
                    linha = re.sub('[^0-9]', ' ', linha)
                    print(f'URL..:{html.url}\n{linha.strip()}\n{"-" * 100}')
                if matchs:
                    if 'telep' in linha or 'telef' in linha:
                        linha = re.sub('[^0-9]', ' ', linha)
                        print(f'URL..:{html.url}\n{linha.strip()}\n{"-" * 100}')
        except Exception as err:
            print(url)
        # break

def getLinkLogo(urls):
    for url in urls.split('\n'):
        html = get(url)
        html_to_texto = html.content.decode('utf-8')
        search = ['img', 'src', 'logo']
        for linha in html_to_texto.split('\n'):
            res = [ele for ele in search if (ele in linha)]
            if len(res) == len(search):
                soup = bs(linha, 'html.parser')
                img_ = soup.img
                tag = img_.attrs
                src = tag['src']
                if not src.startswith('http'):
                    src = ''.join((html.url[:-1], src))
                print(f"{linha}\n{src}\n{'-'*100}")

if __name__ == '__main__':
    filename = 'websites.txt'
    with open(filename, encoding='utf-8') as _f:
        urls = _f.read()
    start_time = datetime.now()
    getTelephone(urls)
    # getLinkLogo(urls)
    end_time = datetime.now()
    time_start = ':'.join((str(start_time.hour), str(start_time.minute), str(start_time.second)))
    time_end = ':'.join((str(end_time.hour), str(end_time.minute), str(end_time.second)))
    print(f'START..:{start_time}\nEND..:{end_time}\nAVERAGE..: {time_start}-{time_end}')
