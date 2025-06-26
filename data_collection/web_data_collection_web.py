import requests
from bs4 import BeautifulSoup

url = "https://python.org.br/web/"
request = requests.get(url)
extraction = BeautifulSoup(request.text, "html.parser")

# print(extraction.text.strip())  # Exibe o texto extraído da página


def h2_extraction():
    for text_line in extraction.find_all("h2"):
        title = text_line.text.strip()
        print("Título:", title)  # Exibe o título de cada h2 encontrado


def h2_and_p_extraction_counter():  # Exibe a quantidade de títulos e parágrafos encontrados
    h2_counter = 0
    p_counter = 0
    for text_line in extraction.find_all(["h2", "p"]):
        title = text_line.name
        if title == "h2":
            h2_counter += 1
        elif title == "p":
            p_counter += 1
        else:
            continue

    print("Títulos:", h2_counter)  # Exibe o título de cada h2 encontrado
    print("Parágrafos:", p_counter)


def h2_and_p_extraction():  # Exibe os títulos e parágrafos encontrados

    for text_line in extraction.find_all({"h2", "p"}):
        text_tag = text_line.name
        text = text_line.text.strip()
        if text_tag == "h2":
            print("Título:", text)  # Exibe o título de cada h2 encontrado
        elif text_tag == "p":
            print("Parágrafo:", text)
        else:
            continue


def nested_tags_extraction():
    for title in extraction.find_all("h2"):
        print("Título:", title.text.strip())
        for link in title.find_next_siblings(
            "p"
        ):  # Encontra as proximas tags <p> após o <h2>
            for a in link.find_all("a", href=True):
                print("Link:", a.text.strip(), " | URL:", a["href"])


nested_tags_extraction()
