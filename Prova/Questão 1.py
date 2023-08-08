# Escreva um programa que calcule e exiba o Máximo Divisor Comum (MDC) de dois números inteiros inseridos pelo usuário.

# Digite o primeiro número inteiro: 24

# Digite o segundo número inteiro: 36

# O Máximo Divisor Comum (MDC) de 24 e 36 é: 12

# Digite o primeiro número inteiro: 48

# Digite o segundo número inteiro: 18

# O Máximo Divisor Comum (MDC) de 48 e 18 é: 6


n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

divisores_n1 = []
for i in range(1, n1 + 1):
    if n1 % i == 0:
        divisores_n1.append(i)

divisores_n2 = []
for j in range(1, n2 + 1):
    if n2 % j == 0:
        divisores_n2.append(j)

divisores_comuns = [divisor for divisor in divisores_n1 if divisor in divisores_n2]

print(f"O Máximo Divisor Comum (MDC) de {n1} e {n2} é: {max(divisores_comuns)}")