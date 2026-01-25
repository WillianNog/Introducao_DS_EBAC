import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head(20).to_string())

# Gráfico de dispersão
sns.jointplot(x='idade', y='salario', data=df, kind='scatter', color='blue') # (scatter, hist, hex, kde, reg, resid)
plt.show()

# Gráfico de densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['salario'], fill=True, color='red')
plt.title('Densidade de salário')
plt.xlabel('Salario')
plt.show()

# Gráfico de Pairplot - Dispersão e Histograma
sns.pairplot(df[['idade', 'salario', 'anos_experiencia','nivel_educacao']])
plt.show()


# Gráfico de Regressão
sns.regplot(x='idade', y='salario', data=df, color='blue', scatter_kws={'alpha': 0.3,'color': 'red'})
plt.title('Regressão de salário por idade')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.show()

# Gráfico countplot com hue
sns.countplot(x='estado_civil', hue='nivel_educacao' ,data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade Clientes')
plt.legend(title='Nivel educacao')
plt.show()