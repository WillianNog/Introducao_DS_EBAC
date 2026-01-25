import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('ecommerce_preparados.csv')

df.info()
print(df.head(5).to_string())

df.drop(columns=['Unnamed: 0','Review1','Review2','Review3','Título'], axis=1, inplace=True)
print(df.head(5).to_string())


