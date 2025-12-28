import pandas as pd

df = pd.read_csv('clientes.csv')
pd.set_option('display.width', None)
print(df.head())

# Remover daddos
df.drop('pais', axis=1, inplace=True)   # Coluna
df.drop(2, axis=0, inplace=True)    # Linha

# Normalizar campos de texto
df['nome'] = df['nome'].str.title() # Converte primeira letra de cada palavra para maiúsculo
df['endereco'] = df['endereco'].str.lower() # Converte coluna para maiúsculo
df['estado'] = df['estado'].str.upper() # Converte coluna para minúsculo

# Converter tipos de dados
df['idade'] = df['idade'].astype(int)

print('\n\n' ,df.head())

# Tratar valores nulos (ausentes)
# df_fillna = df.fillna(0) # Subistitui nulos por 0
# df_dropna = df.dropna() # Remove registros com valores nulos (linha toda)
# df_dropna4 = df.dropna(thresh=4) # Remove registros com valores nulos apenas se na linha tiver pelo menos 4 valores nao nulos
#
# print("Valores nulos:\n" ,df.isnull().sum())
# print("Qtd de registros nulos com fillna: " , df_fillna.isnull().sum().sum()) # .sum 2 vezes seguidas é para somar tudo
# print("Qtd de registros nulos com dropna: " , df_dropna.isnull().sum().sum())
# print("Qtd de registros nulos com dropna4: " , df_dropna4.isnull().sum().sum())


# Tratamento do DF atual
df = df.dropna(subset=['cpf']) #Remover linhas onde CPF é Nulo
print("QTD registros nulos, mas com CPF presente: " , df.isnull().sum().sum())

df.fillna({'estado':'Desconhecido'},inplace=True)
#Outra maneira
df['endereco'] = df['endereco'].fillna('Endereço nao informado')
#outra meneira
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean()) # subistitui idade nula pela média das idades

# Tratar formato de dados
print(df.dtypes['data'])
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')
print(df.dtypes['data_corrigida'])

# Tratar dados duplicados
print('Qtd de registros atual: ', df.shape[0])
df.drop_duplicates() # Sem inplace nao altera o df original (cria um novo df)
df.drop_duplicates(subset=['cpf'], inplace=True)
print('qtd registro sem duplicatas de CPF: ', len(df)) # len mostra quantidade de linha igual o .shape[0]

print('Dados Limpos: ', df.head())


# Salvar DataFrame
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome','idade','cpf','data','endereco','estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print('Novo dataframe: \n', pd.read_csv('clientes_limpeza.csv'))