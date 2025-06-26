import pandas
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/")
# print(response.text[:600])  # Extrair os primeiros 600 caracteres


soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify()[:1000])

print("Pandas: ")
url_data = pandas.read_html("https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/")
print(url_data[0].head(10))
