import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("clientes-v3-preparado.csv")

# Gráfico de Dispersão com Seaborn
sns.jointplot(x="idade", y="salario", data=df, kind="scatter")

# Gráfico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df["salario"], fill=True, color="#863e9c", label="Salário")
plt.title("Densidade do Salário")
plt.xlabel("Salário")

# Gráfico de pairplot
sns.pairplot(df[["idade", "salario", "anos_experiencia", "nivel_educacao"]])

# Gráfico de regressão
plt.figure(figsize=(10, 6))
sns.regplot(
    x="idade",
    y="salario",
    data=df,
    color="#278f65",
    scatter_kws={"alpha": 0.5, "color": "#34c290"},
)
plt.title("Regressão: Idade vs Salário")
plt.xlabel("Idade")
plt.ylabel("Salário")

# Gráfico countplot com hue
plt.figure(figsize=(10, 6))
sns.countplot(x="estado_civil", hue="nivel_educacao", data=df, palette="pastel")
plt.title("Contagem por Estado Civil e Nível de Educação")
plt.xlabel("Estado Civil")
plt.ylabel("Contagem")
plt.legend(title="Nível de Educação")

plt.show()
