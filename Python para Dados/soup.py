import requests
from bs4 import BeautifulSoup
import pandas as pd


print('Request: ')
url = "https://stooq.com/q/d/?s=%5Ebvp&i=d"
response = requests.get(url)
print(response.text[:300])


print('BeautifulSoup: ')
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify()[:400])


print("Pandas: ")
url_dados = pd.read_html(url)
print(url_dados[0].head(10))


