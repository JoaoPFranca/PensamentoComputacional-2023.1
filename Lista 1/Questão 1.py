# Escreva um programa que pede ao usuário 2 números decimais (float) A e B, e imprime o resultado das operações de adição, subtração, divisão, divisão inteira e resto entre A e B. No caso de operações entre números inteiros, como resto e divisão inteira, converta os números em inteiro antes de realizar as operações.

#Digite o número A: 3.5
# Digite o número B: 4
# 3.5 + 4 = 7.5
# 3.5 - 4 = -0.5
# 3.5 / 4 = 0.875
# 3 // 4 = 0
# 3 % 4 = 3

a = float(input("Digite o número A: "))  #Se o tipo de dado não for String, deve-se colocar o tipo antes do input.
b = float(input("Digite o número B: "))

soma = a + b
subtracao = a - b
div = a / b
divInt = int(a) / int(b)
resto = int(a) % int(b)

print(f"{a} + {b} = {soma}")  #As chaves representam a variável possa ser representada no meio de uma frase entre aspas
print(f"{a} - {b} = {subtracao}")  #O "f" transforma o que está entre aspas numa String
print(f"{a} / {b} = {div}")
print(f"{int(a)} // {int(b)} = {divInt}")
print(f"{int(a)} % {int(b)} = {resto}")
