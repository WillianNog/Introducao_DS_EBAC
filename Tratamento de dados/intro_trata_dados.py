import pandas as pd

df = pd.read_csv('clientes.csv')


# Head mostra as 5 primeiras lihhas e tail as ultimas. to_string é para deixar a tabela mais visivel
print(df.head().to_string())
print(df.tail().to_string())


# Verificar qtd de linhas e colunas
print('\nQTD: ', df.shape)

# Verificar tipos de dados
print('\nTipo: \n', df.dtypes)

# Checa valores nulos
print('\nValores nulos:\n', df.isnull().sum())
