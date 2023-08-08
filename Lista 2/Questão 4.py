# Escreva um programa que pede ao usuário um texto e dois números inteiros i1 e i2. Após lidas as entradas o programa faz as seguintes verificações:

# Se i1 > i2 troque os valores de i1 e i2
# Se i1 ou i2 forem maiores ou iguais ao tamanho do texto lido, finalize o programa avisando ao usuário que os valores tem que ser menores do que o tamanho do texto.
# Após feitas as verificações, o programa deverá imprimir partes do texto conforme as especificações abaixo:

# Parte 1: equivale à parte do texto que vai da primeira letra até o índice i1
# Parte 2: equivale à parte do texto que vai da primeira letra até o índice i2
# Parte 3: equivale à parte do texto que vai da letra de índice i1 letra até o índice i2
# Parte 4: equivale à parte do texto que vai da letra de índice i1 até o final do texto
# Parte 5: equivale à parte do texto que vai da letra de índice i2 até o final do texto


# texto? teste_texto
# i1? 1
# i2? 5
# Partes
# Parte 1: t
# Parte 2: teste
# Parte 3: este
# Parte 4: este_texto
# Parte 5: _texto


txt = input("texto? ")
tamanhotxt = len(txt)
i1 = int(input("i1? "))
i2 = int(input("i2? "))

if i1 < tamanhotxt and i2 < tamanhotxt:
  if i1 > i2: #A troca
    i1novo = i2
    i2novo = i1
  
    parte1 = txt[:i1novo]
    parte2 = txt[:i2novo]
    parte3 = txt[i1novo:i2novo]
    parte4 = txt[i1novo:]
    parte5 = txt[i2novo:]
  
  else: #Sem precisar trocar
    parte1 = txt[:i1]
    parte2 = txt[:i2]
    parte3 = txt[i1:i2]
    parte4 = txt[i1:]
    parte5 = txt[i2:]

  print("Partes")
  print(f"Parte 1: {parte1}")
  print(f"Parte 2: {parte2}")
  print(f"Parte 3: {parte3}")
  print(f"Parte 4: {parte4}")
  print(f"Parte 5: {parte5}")

else:
  print("Os valores tem que ser menores do que o tamanho do texto.")