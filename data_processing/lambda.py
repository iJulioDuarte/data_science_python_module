import pandas as pd


def eleva_cubo(x):
    return x**3


eleva_cubo_lambda = lambda x: x**3  # noqa: E731

print(eleva_cubo(2))  # Exibe o resultado da função eleva_cubo
print(eleva_cubo_lambda(2))  # Exibe o resultado da função lambda eleva_cubo_lambda

df = pd.DataFrame({"numeros": [1, 2, 3, 4, 5, 10]})

df["cubo_funcao"] = df["numeros"].apply(eleva_cubo)
df["cubo_lambda"] = df["numeros"].apply(lambda x: x**3)

print(df)  # Exibe o DataFrame com as colunas originais e as novas colunas com os cubos
