# Crie um programa que lê um valor numérico N e que em seguida lê N números. Armazene esses números em uma lista. Em seguida, leia do usuário 3 números inteiros (OP, A e B). O primeiro número (OP) representa uma operação matemática (0 é soma, 1 é multiplicação) que deve ser realizada em cima dos dois números cujas posições (1 a N) na lista são A e B. O programa deve então apresentar a operação e seu resultado.

# Exemplo 1

# Qual o N? 5
# Digite os valores:
# 10
# 20
# 30
# 40
# 50
# Qual a op? 1
# Qual o A? 2
# Qual o B? 4
# 20 * 40 = 800

n = int(input("Qual o N? "))

print("Digite os valores:")
valores = [] #lista de valores
for i in range(n): # até n
    numero = int(input())
    valores.append(numero) #adiciona um número ao final da lista

op = int(input("Qual a op? "))
a = int(input("Qual o A? ")) - 1 #o -1 é uma correção de posição, já que o python começa do 0.
b = int(input("Qual o B? ")) - 1 #exemplo: se eu botar "3" aqui, vai ser o 4º elemento da lista



if op == 0:
  print(f"{valores[a]} + {valores[b]} = {valores[a] + valores[b]}") #valores [a] é basicamente a posição "a" da lista valores

elif op == 1:
  print(f"{valores[a]} * {valores[b]} = {valores[a] * valores[b]}")

else:
  print("Operação inválida! 0 = Adição, 1 = Multiplicação")