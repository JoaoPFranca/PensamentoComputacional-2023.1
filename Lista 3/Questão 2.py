# Um número inteiro positivo,n, é dito triangular se, e somente se, ele é o resultado do produto de três números inteiros positivos e consecutivos. Escreva um algoritmo que leia um número inteiro positivo, n, e escreva como saída “é triangular” se n for triangular e “não é triangular”, caso contrário.

# n? 24

# Saída: é triangular

# n? 25

# Saída: não é triangular

n = int(input("n? "))

for i in range(1, n): # num raio de 1 até n
    if i * (i + 1) * (i + 2) == n: #se i e seus dois consecutivos forem igual a N, eles recebem a condição "is_triangular" como true.
        is_triangular = True
        break
    

if is_triangular:
    print("é triangular")
else:
    print("não é triangular")