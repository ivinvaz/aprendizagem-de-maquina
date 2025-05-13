from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

import sklearn
import seaborn as sns
import pandas as pd
import numpy as np

df = sns.load_dataset('titanic')

df.dropna(inplace=True)
y = df["survived"]
df.drop(columns=["survived"], inplace=True)

#limpando os dados
try:
  df.drop(columns=["pclass"], inplace=True)
  df.drop(columns=["deck"], inplace=True)
  df.drop(columns=["embarked"], inplace=True)
  df.drop(columns=["alive"], inplace=True)
  df.drop(columns=["who"], inplace=True)
  df.drop(columns=["adult_male"], inplace=True)
  df.drop(columns=["embark_town"], inplace=True)
  df.drop(columns=["alone"], inplace=True)
  df.drop(columns=["passengerId"], inplace=True)
  df.drop(columns=["pclass"], inplace=True)
  df.drop(columns=["fare"], inplace=True)
  df.drop(columns=["fare"], inplace=True)
  df.drop(columns=["embark_town"], inplace=True)
  df.drop(columns=["who"], inplace=True)
  df.drop(columns=["parch"], inplace=True)
except:
  pass
df["age"].fillna(df["age"].mean(),inplace=True)

meuLabelEncoder = LabelEncoder()
df["sex"] = meuLabelEncoder.fit_transform(df["sex"])
df["class"] = meuLabelEncoder.fit_transform(df["class"])
dados = df.values

#Recebendo dados
classs = input("Classe do ticket(1,2,3): ")
sex = input("Gênero do tripulante(homem:0, mulher:1): ")
if sex == "male":
  sex = 0
else:
  sex = 1
age = input("Idade do tripulante: ")
sibsp = input("Número de parentes abordo(esposa/maridos, familiares): ")
parch = input("Número de familiares(filhos): ")
fare = input("Taxa paga: ")

#Criando modelo de testes
X = df.values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

modelo = RandomForestClassifier()

'''
modelo.fit(X_test, y_test)
previsoes = modelo.predict(X_test)
print(f"Acurácia: {sklearn.metrics.accuracy_score(y_test, previsoes)}")
'''

modelo.fit(X, y)

#Testando
novo_passageiro = np.array([[sex, age, sibsp, parch, fare, classs]])
x = modelo.predict(novo_passageiro)
if x == 1:
  x = "sobreviveu"
else:
  x = "não sobreviveu"
print(f"O passageiro {x}.")