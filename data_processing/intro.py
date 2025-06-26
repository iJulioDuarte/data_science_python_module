import pandas as pd

df = pd.read_csv("clientes.csv")

print(df.head().to_string())  # Exibe as primeiras linhas do DataFrame
print(df.tail().to_string())  # Exibe as últimas linhas do DataFrame

print("Qtd: ", df.shape)  # Exibe a quantidade de linhas e colunas do DataFrame

print("Types:\n", df.dtypes)  # Exibe os tipos de dados de cada coluna

print(
    "Null values:\n", df.isnull().sum()
)  # Exibe a quantidade de valores nulos em cada coluna

df["Marca"] = df["Marca"].str.upp
