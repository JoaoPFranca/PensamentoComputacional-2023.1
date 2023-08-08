# Crie uma função que receba um número inteiro N como entrada e retorne a soma de todos os múltiplos de 3 ou 5 menores que N. Se um número for múltiplo de ambos 3 e 5, conte-o apenas uma vez na soma.

# Exemplos:

# Entrada: N = 10 Saída: 23.

# Entrada: N = 20 Saída: 78.

n = int(input("N = "))
j = 0

for i in range (n):
  if (i % 3 == 0) or (i % 5 == 0):
    j += i
    
print(f"{j}.")

