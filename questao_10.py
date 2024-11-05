#Questão 10
import pandas as pd

df = pd.read_csv("Caminho do arquivo csv")
print(df.isna())
print(df.isna( ),sum())

df['coluna_exemplo'].fillna(df['coluna_exemplo'].mean(), inplace=True)