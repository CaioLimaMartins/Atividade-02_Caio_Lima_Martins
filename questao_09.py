#Questão 09
import pandas as pd

df = pd.read_csv("Caminho do arquivo csv")
coluna = df["coluna_selecionada"]
filtro = df[df["coluna_selecionada"] > 50]
print(filtro)