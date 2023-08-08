# Escreva um programa que peça ao usuário dois números inteiros n1 e n2 (n2 > n1) e imprima quantos números primos existem no intervalo [n1, n2], incluindo esses dois números. Lembre-se que um número é primo se ele é divisível apenas por 1 e por ele mesmo.

# n1? 2

# n2? 10

# Existem 4 numeros primos entre 2 e 10

n1 = int(input("n1? "))
n2 = int(input("n2? "))

if n1 > n2:
  n1, n2 = n2, n1 #trocar posições se n1 for maior que n2

contador = 0

for i in range(n1, n2 + 1): #no raio de n1 e n2 + 1
    if i > 1: #se o número for maior que um
        is_prime = True #setando a condição "is_prime"
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            contador += 1

print(f"Existem {contador} numeros primos entre {n1} e {n2}")