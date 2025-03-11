import pandas as pd 
try:
  with open("dados.csv", "r") as arquivo:
    conteudo = pd.read_csv("dados.csv")
    lista_dados = conteudo.values.tolist()
    arquivo.close()
except FileNotFoundError:
  with open("dados.csv", "w") as arquivo:
    arquivo.write("Nome,Idade\nAna,25\nBruno,30\nCarla,22\nDaniel,28\nEduardo,35")
    arquivo.close()
  with open("dados.csv", "r") as arquivo:
    conteudo = pd.read_csv("dados.csv")
    lista_dados = conteudo.values.tolist()
    arquivo.close()
nome = input("Digite o nome a ser pesquisado: ")
maior_idade = max(lista_dados)
maior_idade = maior_idade[1]
for nome1,idade in lista_dados:
  if nome1 == nome:
    if idade >= maior_idade:
      print(f"{nome1} tem {idade} anos, é a pessoa mais velha da lista.")
      break
    else:
      print(f"{nome1} tem {idade} anos, não é a pessoa mais velha da lista.")
      break
  else:
    print("Nome não encontrado.")
    break