# Escreva um programa que peça ao usuário um número inteiro N e depois um conjunto de N números. O programa deverá armazenar todos os números lidos numa lista, e então imprimir todos os números, classificando se cada número é primo ou não, no caso se não ser primo o programa também deve imprimir a lista de divisores do número.
# Para verificar se um número é primo ou não, escreva uma função que recebe um número inteiro como parâmetro e retorna à sua lista de divisores. Use o retorno da função para imprimir a saída do programa no formato abaixo:

# Exemplo 1

# Qual o valor de N? 5
# Digite os valores:
# 2
# 5
# 25
# 10
# 9
# A classificação é:
# 2 é primo
# 5 é primo
# 25 não é primo, os divisores são: [1, 5, 25]
# 10 não primo, os divisores são: [1, 2, 5, 10]
# 9 não é primo, os divisores são: [1, 3, 9]


def lista_divisores(numero):
  divisores = []
  for i in range(1, numero + 1):
    if numero % i == 0:
      divisores.append(i)
  return divisores


def classificar_numeros():
  N = int(input("Qual o valor de N? "))
  print("Digite os valores:")
  numeros = []
  for j in range(N):
    numero = int(input())
    numeros.append(numero)

  print("A classificação é:")
  for numero in numeros:
    divisores = lista_divisores(numero)
    if len(divisores) == 2:
      print(numero, "é primo")
    else:
      print(numero, "não é primo, os divisores são:", divisores)


classificar_numeros()
