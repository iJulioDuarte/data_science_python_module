# Agora mostre o título e o preço dos livros da primeira página do site https://books.toscrape.com/, para fazer isso é necessário seguir os passos abaixo:

# Parte 1
# Crie um for para encontrar a tag <h3> dentro da tag <article>
# Extraia os textos da tag <h3> e armazene na variável titulo. Essa variável depois deve ser utilizada para atualizar o valor de livro['Título']
# Crie outro for para encontrar a tag <p class=’’price_color’> com o findall('p', class='price_color'), dentro da tag <h3>
# Extraia os textos da tag <p> e armazene na variável preco. Essa variável depois deve ser utilizada para atualizar o valor de livro['Preço']
# Atente para a nomenclatura correta das variáveis e das chaves do dicionário. Os livros devem ser adicionados na lista catalogo, conforme o código padrão.
# Parte 2
# Calcule a quantidade de livros da primeira página do site https://books.toscrape.com/:

# Você pode utilizar a mesma estrutura de for loop feita na parte 1.
# Armazene a quantidade de livros na variável contar_livros.
# Imprima a variável contar_livros

import pandas as pd
import requests
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

url = "https://books.toscrape.com/"
requisicao = requests.get(url)
requisicao.encoding = "utf-8"

extracao = BeautifulSoup(requisicao.text, "html.parser")

contar_livros = 0
catalogo = []

for artigo in extracao.find_all("article", class_="product_pod"):
    livro = {}
    for titulo in artigo.find_all("h3"):
        titulo = titulo.text.strip()
        livro["Título"] = titulo
        contar_livros += 1

    for preco in artigo.find_all("p", class_="price_color"):
        preco = preco.text.strip()
        print("Preço:", preco)  # Exibe o preço de cada livro encontrado
        livro["Preço"] = preco
    catalogo.append(livro)

print("Total livros:", contar_livros)
