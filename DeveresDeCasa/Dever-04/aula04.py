from random import randint
import pandas as pd

lista = ["maçã", "banana","laranja","uva","maçã","melão","mamão","banana"]
lista = set(lista)

arquivo = open("DeveresDeCasa\Dever-04\data\minhas_frutas.txt", "w")
arquivo.write("Fruta,Quantidade\n")
for frutas in lista:
      arquivo.write(f"{frutas},{randint(1,100)}\n")

arquivo = open("DeveresDeCasa\Dever-04\data\minhas_frutas.txt", "r")
dados = pd.read_csv(arquivo)
dados = pd.DataFrame(dados)
print(dados)