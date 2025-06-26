import pandas as pd
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

df = pd.read_csv("clientes-v2-cleaned.csv")

print(df.head())

df = df[["idade", "salario"]]

# Padronização - MinMaxScaler
scaler = MinMaxScaler()
df["idadeMinMax"] = scaler.fit_transform(df[["idade"]])
df["salarioMinMax"] = scaler.fit_transform(df[["salario"]])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df["idadeMinMax_mm"] = min_max_scaler.fit_transform(df[["idade"]])
df["salarioMinMax_mm"] = min_max_scaler.fit_transform(df[["salario"]])

print(df.head())

# Padronização - StandardScaler
scaler = StandardScaler()
df["idadeStandard"] = scaler.fit_transform(df[["idade"]])
df["salarioStandard"] = scaler.fit_transform(df[["salario"]])

# Padronização - RobustScaler
scaler = RobustScaler()
df["idadeRobust"] = scaler.fit_transform(df[["idade"]])
df["salarioRobust"] = scaler.fit_transform(df[["salario"]])

print(df.head(15))

print("MinMaxScaler (De 0 a 1):")
print(
    "Idade - Min {:.4f}, Max {:.4f}, Mean {:.4f}, Std {:.4f}".format(
        df["idadeMinMax"].min(),
        df["idadeMinMax"].max(),
        df["idadeMinMax"].mean(),
        df["idadeMinMax"].std(),
    )
)
print(
    "Salário - Min {:.4f}, Max {:.4f}, Mean {:.4f}, Std {:.4f}".format(
        df["salarioMinMax"].min(),
        df["salarioMinMax"].max(),
        df["salarioMinMax"].mean(),
        df["salarioMinMax"].std(),
    )
)
