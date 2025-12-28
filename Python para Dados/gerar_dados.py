import pandas as pd
import random
from faker import Faker

fake = Faker('pt_BR')

dados_pessoas = []

for _ in range(10):
    nome = fake.name()
    cpf = fake.cpf()
    idade = random.randint(18, 60)
    data = fake.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%Y")
    endereco = fake.address()
    estado = fake.state()
    pais = "Brasil"

    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'data': data,
        'endereco': endereco,
        'estado': estado,
        'pais': pais
    }

    dados_pessoas.append(pessoa)

df_pessoas = pd.DataFrame(dados_pessoas)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

print(df_pessoas) # Usando o display pre configurado ele sempre mostrará a tabela toda quando eu chamar df_pessoas

print(df_pessoas.to_string()) #usando to_string so funcionara no momento chamado


df_pessoas.to_csv('clientes.csv')