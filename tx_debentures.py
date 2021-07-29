#!/home/hvianna/anaconda3/bin/python

'''
BAIXANDO AS INFORMAÇÕS "Taxas de Debêntures" DA ANBIMA
https://www.anbima.com.br/pt_br/informar/taxas-de-debentures.htm
'''

import os
import time
from datetime import date

import requests
from bs4 import BeautifulSoup
from pandas.tseries.offsets import BDay


def extract_TXDEB():
    # Changing timezone
    os.environ['TZ'] = 'America/Sao_Paulo'
    time.tzset()

    # LOG-IN PARAMs
    today = date.today()
    target_day = today - BDay(1)

    data_01 = target_day.strftime("%Y%m%d")
    data_02 = target_day.strftime("%d/%m/%Y")
    mes = data_02.split('/')[1]

    r1 = data_02.split('/')[0]
    r2 = data_02.split('/')[-1]

    mes_i = {
        '01': 'jan',
        '02': 'fev',
        '03': 'mar',
        '04': 'abr',
        '05': 'mai',
        '06': 'jun',
        '07': 'jul',
        '08': 'ago',
        '09': 'set',
        '10': 'out',
        '11': 'nov',
        '12': 'dez'
    }

    key_list = list(mes_i.keys())
    val_list = list(mes_i.values())
    position = key_list.index(mes)

    with requests.Session() as s:
        s.trust_env = False

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }

        form = {
            "Dt_Ref_Ver": str(data_01),
            "Dt_Ref": str(data_02)
        }

        pre_url = 'https://www.anbima.com.br/pt_br/informar/taxas-de-debentures.htm'
        r = s.get(pre_url, headers=headers)

        if r.status_code == 200:
            '''If everything is "OK", make the POST REQUEST'''

            url_tg = 'https://www.anbima.com.br/informacoes/merc-sec-debentures/resultados/mdeb_'
            url_p1 = f'{r1}{val_list[position]}{r2}_di_percentual.asp'

            url_f = f'{url_tg}{url_p1}'
            r = s.post(url_f, data=form, headers=headers)

            # Extracting the complete url with all the parameter
            soup = BeautifulSoup(r.content, 'html5lib')
            x = soup.find_all('a')

            for info in x:
                lk = info.get('href', None)
                if '.xls' in lk:
                    lkf = lk.strip("..")

            my_url = f'https://www.anbima.com.br/informacoes/merc-sec-debentures{lkf}'
            r = s.get(my_url, headers=headers).content

            my_file = f'TXDEB_{data_01}.xls'
            with open(my_file, 'wb') as output:
                output.write(r)

        s.close()
    return my_file
