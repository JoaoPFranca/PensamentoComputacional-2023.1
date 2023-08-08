# Desenvolva um programa que solicite ao usuário um número inteiro positivo e exiba a sequência de Collatz para esse número. A sequência é gerada da seguinte forma: se o número é par, divida-o por 2; se o número é ímpar, multiplique-o por 3 e adicione 1. Repita esse processo até que o número seja igual a 1.

# Exemplos:

# Digite um número inteiro positivo: 6 Sequência de Collatz para 6: 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# Digite um número inteiro positivo: 13 Sequência de Collatz para 13: 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

n = int(input("Digite um número inteiro positivo: "))

  
if n > 0:
  collatz = [n]
  while n != 1:
      if n % 2 == 0: 
          n //= 2
      else: 
          n = n * 3 + 1
      collatz.append(n)

  print(f"Sequência de Collatz pra {collatz[0]}: {' -> '.join(map(str, collatz))}", end="")

else:
  print("O número deve ser inteiro positivo.")
