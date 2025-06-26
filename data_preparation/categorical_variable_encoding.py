import pandas as pd

pd.set_option("display.width", None)

df = pd.read_csv("clientes-v2-cleaned.csv")

print(df.head())

# Codificação one-hot para "estado_civil"
df = pd.concat([df, pd.get_dummies(df["estado_civil"], prefix="estado_civil")], axis=1)
print("DataFrame após one-hot encoding:", df.head())

# Codificação ordinal para "nivel_educacao"
education_order = {
    "Ensino Fundamental": 1,
    "Ensino Médio": 2,
    "Ensino Superior": 3,
    "Pós-graduação": 4,
}

df["nivel_educacao_ordinal"] = df["nivel_educacao"].map(education_order)

print("DataFrame após codificação ordinal:", df.head())
