import pandas as pd

list_names = ["Ana", "Marcos", "Carlos"]
print("Lista de nomes:", list_names)
print("Primeiro nome:", list_names[0])

print(" ")

dicionary_data = {"nome": "Ana", "idade": 30, "cidade": "São Paulo"}
print("Dicionário de dados:", dicionary_data)
print("Atributo do dicionário:", dicionary_data.get("nome"))

print(" ")

data = [
    {"nome": "Ana", "idade": 30, "cidade": "São Paulo"},
    {"nome": "Marcos", "idade": 25, "cidade": "Rio de Janeiro"},
    {"nome": "Carlos", "idade": 28, "cidade": "Belo Horizonte"},
]

df = pd.DataFrame(data)
print("DataFrame:", df)

print("Primeira linha do DataFrame:\n", df.iloc[0])

df["salario"] = [3000, 2500, 2800]
print("DataFrame com nova coluna 'salario':\n", df)

df.drop(columns=["salario"], inplace=True)
print("DataFrame após remover a coluna 'salario':\n", df)

filter_age = df["idade"] > 27
print("DataFrame filtrado por idade  27:\n", df[filter_age])

df.to_csv("dados.csv", index=False)

read_df = pd.read_csv("dados.csv")
print("DataFrame lido do arquivo CSV:\n", read_df)
