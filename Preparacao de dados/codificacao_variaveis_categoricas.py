import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head(10))


# Codificação one-hot para 'estado_civil'
df = pd.concat( [df,pd.get_dummies(df['estado_civil'],prefix='estado_civil')], axis=1)
print('\n',df.head())

# Codificação Ordinal para 'nivel_educacao'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2 , "Ensino Superior": 3 , 'Pós-Graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)
print("\nDataframe após codificação ordinal para 'nivel_educacao':\n",df.head())

# Transformar 'area_atuacao' em categorias codificadas usando o método .cat.codes
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes
print('\nDataFrame após tranformar "area_atuacao" em códigos nnumericos:\n',df.head())

# Label Encoder para 'estado'
# LabelEncoder converte cada valor único em números de 0 a n_classes-1

label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])
print('\nDataFrame após aplicar LabelEncoder em "estado":\n',df.head())






