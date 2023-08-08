# Desenvolva uma função que receba um número inteiro positivo como entrada e determine se ele é um número narcisista. Um número narcisista é aquele cuja soma dos dígitos elevados à sua própria quantidade de dígitos resulta no próprio número.

# Entrada: 153

# Saída: É um número narcisista.

# Entrada: 9474

# Saída: É um número narcisista.

# Entrada: 123

# Saída: Não é um número narcisista.

n = int(input(""))

if n < 0:
  print("O programa só aceita números inteiros e positivos.")

else:
  nComoString = str(n)
  tamanhoN = len(nComoString)
  calculo = sum(int(cadaDigito)**tamanhoN for cadaDigito in nComoString)

  if calculo == n:
    print("É um número narcisista.")
  else:
    print("Não é um número narcisista.")


