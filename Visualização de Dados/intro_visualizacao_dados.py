import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Histograma
plt.hist(df['salario'])
# plt.show()


# Histograma Parametros
plt.figure(figsize = (10,6))
plt.hist(df[['salario']], bins = 90, color = 'purple', alpha = 0.5)
plt.title('Histograma - Distribuição de salários')
plt.xlabel('Salário')
plt.xticks(ticks=range(0,int(df['salario'].max())+2000,2000))
plt.ylabel('Frequência (Quantidade de registros)')
plt.grid(True)
# plt.show()


# Multiplos Graficos
plt.figure(figsize = (10,6))
plt.subplot(2,2,1)

# Gráfico da dispersão 1
plt.scatter(df['salario'], df['salario'])
plt.title('Dispersão - Salário e salário')
plt.xlabel('Salário')
plt.ylabel('Salário')


# Gráfico da dispersão 2
plt.subplot(2,2,2)
plt.scatter(df['salario'], df['anos_experiencia'], color='#2f6f252d', alpha=0.2, s=20)
plt.title('Dispersão - Salário e Anos de Experiência')
plt.xlabel('Salário')
plt.ylabel('Anos de Experiência')

# Mapa de calor 3
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2,2,3)
sns.heatmap(corr, annot = True , cmap = 'coolwarm')
plt.title('Correlation Heatmap entre idade e Salário')

plt.subplot(2,2,4)
sns.heatmap(corr, annot = True , cmap = 'coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlation Heatmap entre idade e Salário')

plt.tight_layout()
plt.show()















