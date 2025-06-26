import requests


def send_files():
    path = "C:/Users/julio/Documents/Curso EBAC/produtos_informatica.xlsx"

    req = requests.post(
        "https://upload.gofile.io/uploadFile", files={"file": open(path, "rb")}
    )

    res = req.json()

    print(res)

    url = res["data"]["downloadPage"]
    print("Arquivo enviado. Link para acesso: ", url)


def send_files_with_key():
    path = "C:/Users/julio/Documents/Curso EBAC/produtos_informatica.xlsx"
    key = "your_api_key_here"  # Substitua pela sua chave de API

    req = requests.post(
        f"https://api.gofile.io/uploadFile?key={key}", files={"file": open(path, "rb")}
    )

    res = req.json()

    print(res)

    url = res["data"]["downloadPage"]
    print("Arquivo enviado. Link para acesso: ", url)


def get_files(file_url):
    req = requests.get(file_url)

    if req.status_code == 200:
        with open("downloaded_file.xlsx", "wb") as file:
            file.write(req.content)
        print("Arquivo baixado com sucesso.")
    else:
        print("Erro ao baixar o arquivo:", req.status_code)


get_files("")
