#OBS, não estava conseguindo importar a função do arquivo Funcoes de jeito nenhum.

def fazer_str_com_conteudo():
  while True:
    try:
      frase = input("Frase: ")
      if frase == "":
        raise ValueError
      else:
         break
    except ValueError:
      print("A frase não pode ser nula, tente novamente.")
  return frase

#1 

frase = fazer_str_com_conteudo()
lista_palavras = frase.split()
lista_frase = list(frase)

#2

caracteres_totais = [len(palavras) for palavras in lista_palavras]
caracteres_totais = sum(caracteres_totais)

quantas_palavras = len(lista_palavras)

maior_palavra = ""
for palavras in lista_palavras:
    if len(palavras) > len(maior_palavra):
        maior_palavra = palavras

#3

frase_ao_contrario = lista_frase[::-1]
frase_ao_contrario = " ".join(frase_ao_contrario)


frase_contraria = lista_palavras[::-1]
frase_contraria = " ".join(frase_contraria)

frase_maiuscula = frase.upper()

frase_tupla = tuple(lista_palavras)

#4

print(f"-Número de caracteres da frase: {caracteres_totais}\n-Número de palavras: {quantas_palavras}\n-A palavra com maior comprimento: {maior_palavra}\n-A frase invertida por caracteres: {frase_ao_contrario}\n-A frase invertida por palavras:{frase_contraria}\n-A frase em maiúsculas: {frase_maiuscula}\n-A tupla formada pelas palavras da frase: {frase_tupla}")
