import requests
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

url = "https://books.toscrape.com/"
requisicao = requests.get(url)

# variável exigida pelo teste
extracao = BeautifulSoup(requisicao.text, "html.parser")

# ÚNICO print esperado pelo teste
print(extracao.prettify()[:2000])





url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []

for artigo in extracao.find_all('article', class_='product_pod'):
    livro = {}
    for tit in artigo.find_all(['h3', 'article']):
        titulo = tit.text
        livro['Título'] = titulo
    for p in artigo.find_all('p', class_='price_color'):
        preco = p.text
        livro['Preço'] = preco
    catalogo.append(livro)
    contar_livros+=1


print('Total livros:', contar_livros)