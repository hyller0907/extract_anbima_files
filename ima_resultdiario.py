#!/home/hvianna/anaconda3/bin/python

'''
BAIXANDO AS INFORMAÇÕS DO IMA-B NO SITE DA ANBIMA
https://www.anbima.com.br/pt_br/informar/precos-e-indices/precos/precos.htm
'''

import requests


def extract_IMAB(user_day):

    form_day = user_day.strftime("%d/%m/%Y")
    file_day = user_day.strftime("%Y%m%d")


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

        url = 'https://www.anbima.com.br/informacoes/ima/ima-carteira-down.asp'
        r = s.post(url, data=form, headers=headers)

        file = f'IMA_{file_day}.html'
        sfile = str(file)
        with open(file, 'w') as file:
            file.write(r.text)

        s.close()
    return sfile
