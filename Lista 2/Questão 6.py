# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o
# resultado da operação solicitada.

# Digite o Primeiro número: 10
# Digite o Segundo número: 15
# Digite a operação a realizar [+,-,* ou /]: %

# Saída:
# Operação inválida!

a = int(input("Digite o Primeiro número: "))
b = int(input("Digite o Segundo número: "))

operacao = input("Digite a operação a realizar [+,-,* ou /]: ")

if operacao == "+": #usei as " " pq o input padrão é uma string
  print(f"A soma de {a} + {b} é: {a+b}")

elif operacao == "-": #o elif é uma estrutura condicional que funciona como um intermediário entre if e else
  print(f"A subtracao de {a} - {b} é: {a-b}")

elif operacao == "*":
  print(f"O produto de {a} * {b} é: {a*b}")

elif operacao == "/":
  print(f"A divisão de {a} / {b} é: {a/b}")

else:
  print("Operação inválida!")
