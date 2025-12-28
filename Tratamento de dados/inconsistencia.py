import pandas as pd
import numpy as np

pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

df = pd.read_csv('clientes_remove_outliers.csv')

print(df.head())

# Mascarar dados pessoais
df['cpf_mascara'] = df['cpf'].apply(lambda cpf:f'{cpf[:3]}.***.***--{cpf[-2:]}')
print(f'\nComo ficcou os dados mascarados: \n{df['cpf_mascara'].head(2)}')

# Corrigir data
df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d', errors='coerce')

data_atual = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data']<=data_atual, pd.to_datetime('1900-01-01'))
df['idade_ajustada'] = data_atual.year - df['data'].dt.year
df['idade_ajustada'] -= ((data_atual.month < df['data_atualizada'].dt.month) | ((data_atual.month == df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int))

print('Idade maiores que 100\n', df[df['idade_ajustada']>100].head(4))
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan
print('Idade ajustada\n', df[df['idade_ajustada'].isna()].head(2))

# Corrigir campos com multiplas informações
df['endereco_curto'] = df['endereco'].apply( lambda x: x.split('\n')[0].strip())
df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n'))>1 else 'Bairro Desconhecido')
df['estado_sigla'] = df['endereco'].apply(lambda x: x.split('/')[-1].strip().upper() if len(x.split('\n')) >1  else 'Estado Desconhecido')

print('Endereço Formatado \n', df[['endereco_curto', 'bairro' , 'estado_sigla']])

# Tratamento de Endereço
df['endereco_curto'] = df['endereco_curto'].apply(lambda x: "Endereço invalido" if len(x) > 40 or len(x) < 5 else x )

# Corrigir dados erroneos
df['cpf'] = df['cpf'].apply(lambda x: x if len(x) == 14 else "CPF invalido")

ufs = [
    'AC', 'AL', 'AP', 'AM',
    'BA', 'CE', 'DF', 'ES',
    'GO', 'MA', 'MT', 'MS',
    'MG', 'PA', 'PB', 'PR',
    'PE', 'PI', 'RJ', 'RN',
    'RS', 'RO', 'RR', 'SC',
    'SP', 'SE', 'TO'
]

df['estado_sigla'] = df['estado_sigla'].apply(lambda x: x if x in ufs else 'UF Desconhecido')
print('Estados\n', df[df['estado_sigla']=='UF Desconhecido']['estado_sigla'].head(2))
print(df.loc[[81,84]])

print("Dados tratados: \n", df.head(3))

df['cpf'] = df['cpf_mascara']
df['idade'] = df['idade_ajustada']
df['endereco'] = df['endereco_curto']
df['estado'] = df['estado_sigla']
df_salvar = df[['nome','cpf','idade','data','endereco','bairro','estado']]

df_salvar.to_csv('clientes_tratados.csv', index=False)

print('Novo DataFrame: \n', pd.read_csv('clientes_tratados.csv'))