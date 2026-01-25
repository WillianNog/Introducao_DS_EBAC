import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head(20).to_string())


# Grafico de Barras
plt.figure(figsize=(10,6))
df['nivel_educacao'].value_counts().plot(kind='bar',color='red')
plt.title('Divisão de escolaridade - 1')
plt.xlabel('Nivel educacao')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=(10,6))
plt.bar(x, y, color='green')
plt.title('Divisão de escolaridade - 1')
plt.xlabel('Nivel educacao')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

# Grafico de Pizza
plt.figure(figsize=(10,6))
plt.pie(y, labels=x, autopct='%1.0f%%',startangle=90)
plt.title('Distribuição do nível de educação')
plt.show()

# Gráfico de dispersão
plt.hexbin(df['idade'],df['salario'], gridsize=40 , cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.title('Dispersão de idade e salário')
plt.show()
