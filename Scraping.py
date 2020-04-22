# coding: utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd

### Alimentar uma variavel com o conteudo de uma pagina
pag = requests.get('https://statusinvest.com.br/acoes/cgas5')

### Status code - tem como resposta se a requição a pagina foi bem sucedida
### content - é o metodo que acessa o conteudo da pagina
if pag.status_code == 200:
   print('Requisição bem sucedida!')
   content = pag.content

### cont - objeto que contém elementos da página
cont = BeautifulSoup(content, 'html.parser')


### objeto que contem os dados que quero obter da página
table = cont.findAll(name='strong')

### exibindo alguns dados da pagina 
table

#### obtendo a tabela de dividendos desta pagina
table = cont.find(name='table')

### transformação a variavel table em uma string, e utilizar metodo do pandas read_html para ler o html da pagina
tabela = str(table)
df = pd.read_html(tabela)[0]

#exibe os dividendos da CGAS5 - COMGAS
df

