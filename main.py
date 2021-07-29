#!/home/hvianna/anaconda3/bin/python

from ima_resultdiario import extract_IMAB
from taxa_cri_cra import extract_TXCRICRA
from listagem_238 import Listagem238
from tx_debentures import extract_TXDEB
from titulos_pub import extract_TP

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
        x = f'O arquivo {file_name} foi movido para a pasta indicada'

    if file_raiz == True:
        os.remove(file_name)
        x = f'A informação {file_name} já existe'

    return x

if __name__ == "__main__":

    '''
    extract_IMAB     = Arquivo IMA-B
    extract_TXCRICRA = Arquivo MTM de CRI e CRA
    Listagem238      = Arquivo com as informações 238
    extract_TXDEB    = Arquivo Taxa de debentures
    extract_TP       = Arquivo "ms" de Titulos Publicos
    '''

    print(f'#########################################################')
    print(f'################ ARQUIVOS ANBIMA ########################')
    print(f'#########################################################')

    try:
        today = date.today()
        form_day = today.strftime("%Y%m%d")
        print(f'Data do Download: {form_day}')

        pwd = os.getcwd()
        dest_00 = r'/home/hvianna/Desktop/ARQUIVOS_ANBIMA'
        file_destination = os.path.join(dest_00, form_day)
        print(f'{file_destination}\n')

        testing02 = os.path.isfile(file_destination)

        if testing02 == False:
            os.mkdir(file_destination)

    except:
        pass

    # Fazendo o Download do arquivo "IMA - Resultados Diários" e salvando na pasta destino
    arquivo_ima = extract_IMAB()
    ima_actual = os.path.join(pwd, arquivo_ima)
    exec_func = mov_files(arquivo_ima, ima_actual, file_destination)
    print(exec_func)

    # Fazendo o Download do arquivo "Taxas de CRI e CRA" e salvando na pasta destino
    arquivo_TXCriCra = extract_TXCRICRA()
    TXCriCra_actual = os.path.join(pwd, arquivo_TXCriCra)
    exec_func = mov_files(arquivo_TXCriCra, TXCriCra_actual, file_destination)
    print(exec_func)

    # Fazendo o Download do arquivo "Listagem 238" e salvando na pasta destino
    arquivo_238 = Listagem238()
    arquivo238_actual = os.path.join(pwd, arquivo_238)
    exec_func = mov_files(arquivo_238, arquivo238_actual, file_destination)
    print(exec_func)

    # Fazendo o Download do arquivo "Taxa Debenture" e salvando na pasta destino
    arquivo_TXDEB = extract_TXDEB()
    arquivo_TXDEB_actual = os.path.join(pwd, arquivo_TXDEB)
    exec_func = mov_files(arquivo_TXDEB, arquivo_TXDEB_actual, file_destination)
    print(exec_func)

    # Fazendo o Download do arquivo "ms" e salvando na pasta destino
    arquivo_ms = extract_TP()
    arquivo_ms_actual = os.path.join(pwd, arquivo_ms)
    exec_func = mov_files(arquivo_ms, arquivo_ms_actual, file_destination)
    print(exec_func)
