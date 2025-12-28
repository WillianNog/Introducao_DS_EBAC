import pandas as pd

# Função para calcular o cubo de um numero

def eleva_cubo(x):
    return x ** 3 # O arterisco duas vezes significa elevado


# Expressao lambda é escrever a mesma função porem em 1 linha
# Expressao lambda pra calcular o cubo de um numero

eleva_cubo_lambda = lambda x : x ** 3

print(eleva_cubo(2))
print(eleva_cubo_lambda(2))

df = pd.DataFrame({'numeros' : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]})
df['cubo_funcao'] = df['numeros'].apply(eleva_cubo)
df['cubo_lambda'] = df['numeros'].apply(lambda x: x ** 3)

print(df)