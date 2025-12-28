import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] > 100]

print('Filtro básico: \n', df_filtro_basico[['nome', 'idade']])

# Identificar Outliers com Z-score
z_score = stats.zscore(df['idade'])
outliers_z = df[z_score >= 3]
print('\nOutliers pelo Z-Score: \n', outliers_z)

df_zscore = df[(stats.zscore(df['idade']) < 3)]

# Identificar outliers com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print('\nLimites IQR: ', limite_baixo,' e ', limite_alto)

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print('\nOutliers IQR: ', outliers_iqr)


# Filtrar outliers com IQR
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

# Filtro manual
limite_baixo = 1
limite_alto = 100
df = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

# Filtrar enderecos invalidos
df['endereco'] = df['endereco'].apply(lambda x: 'Endereço inválido' if len(x.split('\n')) < 3 else x)
print('\nQtd de enderecos invalidos: ', (df['endereco']=='Endereço inválido').sum(),'\n' )

# Trata campos de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome invalido' if isinstance(x,str) and len(x)>50 else x)

print('\nQtd de nomes invalidos: ', (df['nome']=='Nome invalido').sum(),'\n' )

print('Dados Tratados \n' ,df)

# Salvando em csv

df.to_csv('clientes_remove_outliers.csv', index=False)