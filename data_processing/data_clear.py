import pandas as pd

df = pd.read_csv("clientes.csv")
pd.set_option("display.width", None)


# df.drop("país", axis=1, inplace=True)
df.drop(2, axis=0, inplace=True)


df["nome"] = df["nome"].str.title()
df["endereco"] = df["endereco"].str.lower()
df["estado"] = df["estado"].str.upper()

df["idade"] = df["idade"].astype(int)

# Tratar valores nulos
print("Valores nulos: ", df.isnull().sum())
df_fillna = df.fillna(0)
df_dropna = df.dropna()
df_dropna4 = df.dropna(thresh=4)
df = df.dropna(subset=["cpf"])

# Exibir valores nulos tratados
print("Valores nulos tratados com fillna: ", df_fillna.isnull().sum().sum())
print("Valores nulos tratados com dropna: ", df_dropna.isnull().sum().sum())
print("Valores nulos tratados com dropna (thresh=4): ", df_dropna4.isnull().sum())
