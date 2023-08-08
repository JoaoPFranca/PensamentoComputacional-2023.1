# Desenvolva uma função que receba uma string e uma substring como entrada e determine se a substring está presente na string.

# Exemplos:

# Entrada

# string = "Olá, mundo!"

# substring = "mundo"

# Saída:

# A substring está presente na string.

# Entrada:

# string = "O céu está azul hoje"

# substring = "nublado"


a = input("string = ")
b = input("substring = ")

if b in a:
  print("A substring está presente na string.")

