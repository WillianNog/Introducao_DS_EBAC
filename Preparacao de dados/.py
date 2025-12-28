import pandas as pd

df = pd.read_csv('clientes-v2.csv')

print(df.head().to_string())
print(df.tail().to_string())

df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print('Verificação inicial: ')
print(df.info())

print('Dados nulos: \n' , df.isnull().sum())
print('Dados nulos %: \n' , df.isnull().mean() * 100)

# Remover todas as linha que tenham valores nulos
print('\nLinhas Totais' , df.shape[0])
print('Excluindo linhas com Nulos...')
df.dropna(inplace=True)

# Confirmar exclusao
print('Linhas Totais' , df.shape[0] )
print("QTD de linhas com nulos: " , df.isnull().sum().sum())

print('Analise de dados duplicados: ',df.duplicated().sum())
print('Analise de dados unicos: \n',df.nunique())
print('Estatísticas dos dados: \n', df.describe().to_string())


df = df[['idade' , 'data' , 'estado' , 'salario' , 'nivel_educacao' , 'numero_filhos' , 'estado_civil' , 'area_atuacao' ]]
print(df.head().to_string())
df.to_csv('clientes-v2-tratados.csv' , index=False)
