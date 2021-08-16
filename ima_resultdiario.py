#!/home/hvianna/anaconda3/bin/python

'''
BAIXANDO AS INFORMAÇÕS DO IMA-B NO SITE DA ANBIMA
https://www.anbima.com.br/pt_br/informar/precos-e-indices/precos/precos.htm
'''

import requests
from yesterday import show_yday

def extract_IMAB(user_day):

    form_day = user_day.strftime("%d/%m/%Y")
    file_day = user_day.strftime("%Y%m%d")
    form2 = user_day.strftime("%d%m%Y")

    with requests.Session() as s:

        s.trust_env = False

        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'}

        form1 = {
                "Tipo":"",
                "DataRef":"",
                "Pai":"ima",
                "escolha":"1",
                "Idioma":"PT",
                "saida":"xls",
                "indice":"ima-b",
                "consulta":"Ambos",
                "Dt_Ref_Ver":file_day,
                "Dt_Ref":form_day,
                }

        pre_url = "https://www.anbima.com.br/informacoes/ima/ima-carteira.asp"
        r = s.post(pre_url, data=form1, headers=headers)

        form2 = {
            "Tipo":"1",
            "Indice":"ima-b",
            "DataRef":form2,
            "Pai":"ima_carteira",
            "Consulta":"Ambos",
            "Info1":"true",
            "Info2":"",
            "Info3":"true",
            "Info4":"true",
            "Info5":"true",
            "Info6":"true",
            "Info7":"true",
            "Info8":"true",
            "Info9":"true",
            "Info10":"",
            "Info11":"true",
            "Info12":"true",
            "Info13":"true",
            "Info14":"true",
            "Info15":"true",
            "Info16":"true",
            "Info17":"true",
            "Info18":"true",
            "Info19":"true",
            "Info20":"true",
            "Info21":"",
            "Info22":"true",
            "Info23":"true",
            "Info24":"true",
            "Info25":"true",
            "Info26":"true",
            "Info27":"true",
            "Info28":"true",
            "Info29":"true",
            "Info30":"true",
            "Info31":"true",
            "Info32":"true",
            "Info33":"true",
            "Info34":"true",
            "Info35":"true",
            "Info36":"true",
            "Info37":"true",
            "Info38":"true",
            "Info39":"true",
        }

        url = "https://www.anbima.com.br/informacoes/ima/ima-carteira.asp"
        r = s.post(url, data=form2, headers=headers)

        file = f'IMA_{file_day}.html'
        sfile = str(file)
        with open(file, 'w') as file:
            file.write(r.text)

        s.close()
    return sfile
