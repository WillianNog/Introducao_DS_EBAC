import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

df_corr = df[['salario','idade','anos_experiencia','numero_filhos','nivel_educacao_cod', 'area_atuacao_cod','estado_cod']].corr()
# Heatmap de correlacao
plt.figure(figsize = (12,8))
sns.heatmap(df_corr, annot=True, fmt='.2f',vmin=-1, vmax=1, center=0 , cmap='coolwarm')
plt.title('Mapa de Calor da Correlação entre variáveis')
plt.xticks(rotation = 25)
plt.show()

# Já usei
# Countplot sem hue e com hue
sns.countplot(x='estado_civil' ,data=df,)
plt.title('Distribuição Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.show()

sns.countplot(x='estado_civil', hue='nivel_educacao' ,data=df,)
plt.title('Distribuição Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.legend(title='Nivel educacao')
plt.show()


df_corr = df[['salario','idade','anos_experiencia','numero_filhos','nivel_educacao_cod', 'area_atuacao_cod','estado_cod']].corr()
# Heatmap de correlacao
plt.figure(figsize = (12,8))
plt.subplot(2,2,1)
sns.heatmap(df_corr, annot=True, fmt='.2f',vmin=-1, vmax=1, center=0 , cmap='coolwarm')
plt.title('Mapa de Calor da Correlação entre variáveis')
plt.xticks(rotation = 25)

plt.subplot(2,2,2)
sns.countplot(x='estado_civil' ,data=df,)
plt.title('Distribuição Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')


plt.subplot(2,2,3)
sns.countplot(x='estado_civil', hue='nivel_educacao' ,data=df,)
plt.title('Distribuição Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.legend(title='Nivel educacao')

plt.subplot(2,2,4)
plt.scatter(df['salario'], df['anos_experiencia'], color='#2f6f252d', alpha=0.2, s=20)
plt.title('Dispersão - Salário e Anos de Experiência')
plt.xlabel('Salário')
plt.ylabel('Anos de Experiência')

plt.tight_layout()
plt.savefig('grafico.png')
plt.show()
