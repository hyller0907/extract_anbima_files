#!/home/hvianna/anaconda3/bin/python

'''
BAIXANDO AS INFORMAÇÕS DA LISTAGEM 238 NO SITE DA ANBIMA
https://www.anbima.com.br/pt_br/informar/listagem-238.htm
'''
import requests

def Listagem238(user_day):
    form_day = user_day.strftime("%Y%m%d")

    with requests.Session() as s:
        s.trust_env = False

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        }

        pre_url = 'https://www.anbima.com.br/informacoes/res-238/resultados'
        url = f'{pre_url}/{form_day}_238.asp'
        r = s.get(url, headers=headers)

        if r.status_code == 200:
            # Extracting all in excel file
            pre_excel = 'https://www.anbima.com.br/informacoes/res-238/arqs'
            excel_get = f'{pre_excel}/{form_day}_238.tex'

            r = s.get(excel_get, headers = headers).content

            file = f'listagem_238_{form_day}.csv'
            with open(file, 'wb') as output:
                output.write(r)

        s.close()
    return file
