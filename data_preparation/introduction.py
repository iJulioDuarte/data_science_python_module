import pandas as pd

df = pd.read_csv("clientes-v2.csv")

print(df.head().to_string())
print(df.tail().to_string())
df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y", errors="coerce")

print("Verificação inicial de dados:")
print(df.info())

print("Verificação de valores nulos: ", df.isnull().sum())
print("% de valores nulos: ", df.isnull().mean() * 100)


df.dropna(inplace=True)


print("Verificação de valores nulos após remoção: ", df.isnull().sum().sum())

print("Verificação de duplicatas: ", df.duplicated().sum())

print("Análise de dados únicos:", df.nunique())

print("Estatística dos dados: ", df.describe())

df = df[
    [
        "idade",
        "data",
        "estado",
        "salario",
        "nivel_educacao",
        "numero_filhos",
        "estado_civil",
        "area_atuacao",
    ]
]
print("DataFrame após seleção de colunas: \n", df.head().to_string())

df.to_csv("clientes-v2-cleaned.csv", index=False)

df["Preço"] = df.apply(x=lambda x: , axis=1)
