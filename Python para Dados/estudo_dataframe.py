# Estudo Dataframe

import pandas as pd



# Lista é uma coleção ordenada de elementos que podem ser de qualquer tipo
lista_nomes = ['Ana', 'Marcos', 'Carlos']
print('\n\n\nLista de nomes: \n', lista_nomes)
print('Primeiro Elemento na Lista: \n', lista_nomes[0])



# Dicionário é uma estrutura composta de pares chave-valor
dicionario_pessoa = {
    'nome': 'Ana',
    'idade': 39,
    'cidade': 'São Paulo',}

print('Dicionário de uma pessoa, \n', dicionario_pessoa)
print('Pessoa cujo nome é: ', dicionario_pessoa['nome'], ' e idade: ', dicionario_pessoa['idade'])
# ou com atributo get
print('Com GET -> Pessoa cujo nome é: ', dicionario_pessoa.get('nome'), ' e idade: ', dicionario_pessoa.get('idade'))



# Lista de Dicionários é uma estrutura de dados que combina listas e dicionários.
dados = [
    {'nome': 'Ana', 'idade': 24, 'cidade': 'São Paulo'},
    {'nome': 'Marcos', 'idade': 40, 'cidade': 'Campinas'},
    {'nome': 'Willian', 'idade': 25, 'cidade': 'Mairiporã'},
]
print('\n\n\n',dados)
print(dados[1])
print(dados[1]['nome'], dados[2]['idade'])


# DataFrame: uma estrutura de dados bidimensional, ou seja, uma tabela (linhas e colunas)

df = pd.DataFrame(dados)
print('\n\nDataFrame \n', df)

# Selecionar coluna
print('\n\nNomes \n', df['nome'])

# Selecionar várias colunas (uso duas chaves para selecionar mais de uma de uma vez)
print('\n\nNome, Idade e Cidade \n', df[['nome','idade','cidade']])

# Selecionar linha
print('\n\nPrimeira linha: \n', df.iloc[0]) # Uso iloc para definir a linha que quero trazer as info

# Adicionar uma nova coluna
df['salario'] = [4100, 16000, 5200]
print('\n',df)

# Adicionar um novo registro
df.loc[len(df)] = {
    'nome': 'Joao',
    'idade': 45,
    'cidade': 'Atibaia',
    'salario': 4600
}
print('\n\n\nDataframe atualizado: \n', df)

# Remover uma coluna
df.drop('salario', axis=1, inplace=True) # axis=1 é para coluna e axis=0 para linha

# Filtrando pessoas com mais de 28 anos
filtro_idade = df[df['idade'] >= 28]
print('\n\n\nFiltro de idade \n', filtro_idade)

# Salvando em CSV

df.to_csv('dados.csv', index=False)


# Lendo arquivo CSV em DataFrame

df_lido = pd.read_csv('dados.csv')
print('\n Leitura do CSV \n',df_lido)