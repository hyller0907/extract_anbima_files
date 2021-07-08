#!/home/hvianna/anaconda3/bin/python

'''
BAIXANDO AS INFORMAÇÕS DO IMA-B NO SITE DA ANBIMA
https://www.anbima.com.br/pt_br/informar/precos-e-indices/precos/precos.htm
'''

import os
import time
from datetime import date

import requests
from pandas.tseries.offsets import BDay


def extract_IMAB():
    # Changing timezone
    os.environ['TZ'] = 'America/Sao_Paulo'
    time.tzset()

    # LOG-IN PARAMs
    today = date.today()
    target_day = today - BDay(1)
    form_day = target_day.strftime("%d/%m/%Y")

    with requests.Session() as s:
        s.trust_env = False

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }

        form = {"Titulo_2": "ima-b",
                "Consulta_2": "Ambos",
                "Idioma": "PT",
                "Dt_Ref": form_day,
                "DataIni": form_day,
                "DataFim": form_day,
                "Indice": "ima-b",
                "Consulta": "Ambos",
                "saida": "xls"}

        pre_url = 'https://www.anbima.com.br/informacoes/ima/ima-carteira.asp'
        r = s.get(pre_url, headers=headers)

        # Finding the authentication needed to gain access to Pegasus Module
        url = 'https://www.anbima.com.br/informacoes/ima/ima-carteira-down.asp'
        r = s.post(url, data=form, headers=headers)

        file = f'IMA_{target_day.strftime("%Y%m%d")}.html'
        sfile = str(file)
        with open(file, 'w') as file:
            file.write(r.text)

    s.close()

    print(f'Arquivo {sfile} baixado com sucesso.')
    return sfile
