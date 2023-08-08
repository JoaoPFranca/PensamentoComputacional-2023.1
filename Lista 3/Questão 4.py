# Crie um programa que leia um número N (0 < N < 10) e que imprima uma sequência de números conforme mostrado no exemplo:

# n? 5

# 1
# 22
# 333
# 4444
# 55555

n = int(input("n? ")) #aqui pegamos o número
i = 1 #declarando a variável

while i <= n: #enquanto i for menor ou igual a n
    print(str(i) * i) #vai printando i (como string para poder ser uma repetição ao invés do valor) i vezes
    i += 1 # aqui é para ir alimentando de um em um
