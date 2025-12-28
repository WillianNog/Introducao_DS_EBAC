import requests
from bs4 import BeautifulSoup

url ='https://python.org.br/web/'
response = requests.get(url)
extract = BeautifulSoup(response.text, 'html.parser')
conta_subtitulos = 0
conta_paragrafos = 0
#Exibrir Texto

# print(extract.text.strip())

#Filtrar pela TAG
for linha_texto in extract.find_all(['h2','p']):
    if linha_texto.name == 'h2':
        texto = linha_texto.text.strip()
        print(f"Subtitulo:  {texto}\n")
    if linha_texto.name == 'p':
        texto = linha_texto.text.strip()
        print(f"Paragrafo:  {texto}\n")

    if linha_texto.name == 'h2':
        conta_subtitulos += 1
    if linha_texto.name == 'p':
        conta_paragrafos += 1



print(f'Subtitulo h2: {conta_subtitulos}')
print(f'Paragrafo p: {conta_paragrafos}')
