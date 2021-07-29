#!/home/hvianna/anaconda3/bin/python

"""
BAIXANDO AS INFORMAÇÕS DAS TAXAS CRI DO SITE DA ANBIMA
https://www.anbima.com.br/pt_br/informar/precos-e-indices/precos/precos.htm
"""

import io
import os
import time
from datetime import date

import pandas as pd
import requests

def extract_TXCRICRA():
    # Changing timezone
    os.environ['TZ'] = 'America/Sao_Paulo'
    time.tzset()

    today = date.today()
    file_name_compl = today.strftime("%Y%m%d")

    with requests.Session() as s:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'}

        url = 'https://www.anbima.com.br/pt_br/anbima/TaxasCriCraExport/exportarCSV?filtroTermo=&filtroData='
        r = s.get(url, headers=headers).content

        arquivo = pd.read_csv(io.StringIO(r.decode('ISO-8859-1')), sep=";")

        my_file = f'ANBIMA_TAXAS_CRI-CRA_{file_name_compl}.xlsx'
        sfile = str(my_file)
        arquivo.to_excel(my_file, index=False)

        s.close()
    return my_file
