import numpy as np
import pandas as pd
from scipy import stats

pd.set_option('display.width', None)
df = pd.read_csv('clientes-v2-tratados.csv')

# Transformação logarítmica
df['salario_log'] = np.log1p(df['salario']) # log1p serve para evitar problemas com valores 0
print('Transformação logaritmica em salario:\n',df.head())

df['salario_boxcox'], _ = stats.boxcox(df['salario']+1)
print('Transformação Box-Cox em salario:\n',df.head(10))

estado_freq = (df['estado'].value_counts() / len(df))*100
df['estado_freq'] = df['estado'].map(estado_freq)

print('\nPorcentagem de desconto em cada linha\n',
      df[['estado','estado_freq']].drop_duplicates().head(15))

# Interações
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']
print('\nInteração de filhos com idade:\n', df[['nivel_educacao','estado','interacao_idade_filhos']].head(15))


