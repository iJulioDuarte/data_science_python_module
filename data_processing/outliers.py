import pandas as pd
from scipy import stats

pd.set_option("display.width", None)  # Exibir toda a largura do DataFrame
df = pd.read_csv("clientes.csv")

print(df)

df_basic_filter = df[df["idade"] > 80]

# print("Valores acima de 80 anos: ", df_basic_filter)

z_scores = stats.zscore(df["idade"])
outliers_z = df[z_scores > 3]
print("Outliers usando Z-Score: ", outliers_z)

df_zscore = df[(stats.zscore(df["idade"]) < 3)]

print("DataFrame sem outliers usando Z-Score: ", df_zscore)

Q1 = df["idade"].quantile(0.25)
Q3 = df["idade"].quantile(0.75)
IQR = Q3 - Q1

low_limit = Q1 - 1.5 * IQR
high_limit = Q3 + 1.5 * IQR

print("Limites inferior e superior: ", low_limit, high_limit)

outliers_iqr = df[(df["idade"] >= low_limit) & (df["idade"] <= high_limit)]
print("Outliers usando IQR: ", outliers_iqr)

pd.to_
