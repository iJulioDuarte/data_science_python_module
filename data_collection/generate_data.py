import random

import pandas as pd
from faker import Faker

faker = Faker("pt_BR")

personal_data = []

for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 70)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime(
        "%d/%m/%Y"
    )
    endereco = faker.address()
    estado = faker.state()
    pais = faker.country()

    person = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "data_nascimento": data,
        "endereco": endereco,
        "estado": estado,
        "pais": pais,
    }

    personal_data.append(person)

df_people = pd.DataFrame(personal_data)
print("DataFrame de pessoas:\n", df_people)

pd.set_option("display.max_columns", None)  # Exibe todas as colunas
pd.set_option("display.max_rows", None)  # Exibe todas as linhas
pd.set_option("display.max_colwidth", None)  # Exibe o conteúdo completo das colunas
pd.set_option("display.width", None)  # Ajusta a largura da exibição

df_people.to_csv("people_data.csv", index=False)
read_df_people = pd.read_csv("people_data.csv")
