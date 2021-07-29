#!/home/hvianna/anaconda3/bin/python

from ima_resultdiario import extract_IMAB
from taxa_cri_cra import extract_TXCRICRA
from listagem_238 import Listagem238

import shutil
import os

import time
from datetime import date

'''
Your script you just need to make your script executable.
Something like chmod a+x [your-script].py should make it
executable and then you can just call ./[your-script.py]
in shell.
'''

def mov_files(file_name, actual, destination):

    file_raiz = os.path.isfile(os.path.join(destination, file_name))

    if file_raiz == False:
        shutil.move(actual, destination)
        os.remove(file_name)
        x = 'O arquivo foi movido para a pasta indicada'

    else:
        os.remove(file_name)
        x = 'A informação já existe'

    return print(x)

if __name__ == "__main__":

    '''
    extract_IMAB = Arquivo IMA-B
    extract_TXCRICRA = Arquivo MTM de CRI e CRA
    Listagem238 = Arquivo com as informações 238



    '''


    try:
        today = date.today()
        form_day = today.strftime("%Y%m%d")

        pwd = os.getcwd()
        dest_00 = r'/home/hvianna/Desktop/ARQUIVOS_ANBIMA'
        file_destination = os.path.join(dest_00, form_day)

        try:
            testing02 = os.path.isfile(file_destination)

            if testing02 == False:
                os.mkdir(file_destination)

        except:
            pass

        # Fazendo o Download do arquivo "IMA - Resultados Diários" e salvando na pasta destino
        arquivo_ima = extract_IMAB()
        ima_actual = os.path.join(pwd, arquivo_ima)
        mov_files(arquivo_ima, ima_actual, file_destination)

        # Fazendo o Download do arquivo "Taxas de CRI e CRA" e salvando na pasta destino
        arquivo_TXCriCra = extract_TXCRICRA()
        TXCriCra_actual = os.path.join(pwd, arquivo_TXCriCra)
        mov_files(arquivo_TXCriCra, TXCriCra_actual, file_destination)

        # Fazendo o Download do arquivo "Listagem 238" e salvando na pasta destino
        arquivo_238 = Listagem238()
        arquivo238_actual = os.path.join(pwd, arquivo_238)
        mov_files(arquivo_238, arquivo238_actual, file_destination)

    except:
        pass
