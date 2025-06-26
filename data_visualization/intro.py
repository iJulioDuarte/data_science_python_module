import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("clientes-v3-preparado.csv")

# Histograma
# plt.hist(df["salario"])
# plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df["salario"], bins=100, color="green", alpha=0.8)
plt.title("Histograma do Salário")
plt.xlabel("Salário")
plt.ylabel("Frequência")
plt.xticks(ticks=range(0, int(df["salario"].max()) + 2000, 2000))  #
plt.grid(True)

# Multiplos graficos

plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)  # 2 Linhas, 2 Colunas, Gráfico 1
# Grafico de dispersão
plt.scatter(df["salario"], df["salario"])
plt.title("Gráfico de Dispersão do Salário")
plt.xlabel("Salário")
plt.ylabel("Salário")

plt.subplot(1, 2, 2)  # 1 Linhas, 2 Colunas, Gráfico 2
plt.scatter(df["salario"], df["anos_experiencia"], color="red", alpha=0.6, s=30)
plt.title("Gráfico de Dispersão Salário x Anos de Experiência")
plt.xlabel("Salário")
plt.ylabel("Anos de Experiência")

# Mapa de calor
corr = df[["salario", "anos_experiencia"]].corr()
plt.subplot(2, 2, 3)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Mapa de Calor da Correlação Salário e Idade")

plt.tight_layout()

plt.show()

# Mapa de calor
