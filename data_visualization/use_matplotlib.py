import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("clientes-v3-preparado.csv")

# Grafico de barras
plt.figure(figsize=(10, 6))
df["nivel_educacao"].value_counts().plot(kind="bar", color="#90ee70")
plt.title("Distribuição do Nível de Educação")
plt.xlabel("Nível de Educação")
plt.ylabel("Quantidade")
plt.xticks(rotation=0)  # Rotaciona os rótulos do eixo x para melhor legibilidade

x = df["nivel_educacao"].value_counts().index
y = df["nivel_educacao"].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color="#60aa65")
plt.title("Distribuição do Nível de Educação")
plt.xlabel("Nível de Educação")
plt.ylabel("Quantidade")

# Gráfico de pizza
plt.figure(figsize=(10, 6))
plt.pie(
    y,
    labels=x,
    autopct="%1.1f%%",  # Formato de porcentagem (%1.2%% para 2 casas decimais)
    startangle=90,
)
plt.title("Distribuição do Nível de Educação")

# Gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.hexbin(df["idade"], df["salario"], gridsize=40, cmap="Blues")
plt.colorbar(label="Contagem dentro do bin")
plt.xlabel("Idade")
plt.ylabel("Salário")
plt.title("Gráfico de Dispersão: Idade vs Salário")

plt.show()
