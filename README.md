DOWNLOAD DE ARQUIVOS ANBIMA
============================

Este repositório tem como objetivo compartilhar scripts em Python que permitem ao usuário
a extração das informações e arquivos diários disponibilizados pela ANBIMA:

https://www.anbima.com.br/pt_br/informar/precos-e-indices/precos/precos.htm

https://www.anbima.com.br/pt_br/informar/ima-resultados-diarios.htm

<pre>
- Listagem 238
- IMA-B (Resultados Diários)
- Taxas de Debêntures
- Listagem 550
- Taxas de Títulos Públicos
- REUNE (negociações com debêntures, CRIs, CRAs e CFFs realizadas no mercado secundário)
- Taxas de CRI e CRA
</pre>

<strong>Motivação</strong>

A maioria dos arquivos disponibilizados pela entidade não possuem registro histórico.
Ou seja, existe um limite máximo para a consulta retroativa. Realizando a extração dos
arquivos diariamente, é possível garantir uma fonte histórica fidedigna para consulta
ou manipulação.

ARQUIVOS & INFORMAÇÕES
-----------------------

Toda a execução do código foi segmentada em pequenas funções e individualizadas
em diferentes arquivos ".py". As funções foram centralizadas no arquivo "main.py"
ou via Bash File, fazendo o uso do arquivo "exe_main.sh".

A diferença entre os arquivos, é que o último cria um arquivo ".txt" com os outputs
do código em Python, facilitando a verificação na ocasião de inconsistencias.

INSTALAR AS DEPENDENCIAS NECESSÁRIAS
------------------------------------

Para baixar os arquivos do repositório e instalar as dependencias necessárias,
utilize os comandos a seguir:
	
	$ cd ...local desejado...
	$ git clone https://github.com/hyller0907/ANBIMA_extract.git
	$ cd ANBIMA_extract
	$ pip install -r requirements.txt

Os códigos deste repositorio irão ser atualizados de tempos em tempos, dessa
forma, é importante mante-los atualizados utilizando o comando

	$ git pull
