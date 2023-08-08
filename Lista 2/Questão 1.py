# Escreva um programa que lê do usuário 3 números e imprime quem é o maior, quem é o menor e quem é o do 'meio'. Veja que existem diferentes casos a considerar: (1) três números iguais, (2) três números diferentes, (3) dois números iguais. Para cada um dos casos seu programa deve imprimir a saída de acordo com os exemplos que seguem:

# n1? 12
# n2? 10
# n3? 25
# maior: 25
# menor: 10
# meio: 12

# n1? 1
# n2? 1
# n3? 1
# todos são iguais a 1

# n1? 11
# n2? 11
# n3? 25
# maior: 25
# menores: 11
# não há elementos do meio

a = int(input("n1? "))
b = int(input("n2? "))
c = int(input("n3? "))

numeros = [a, b, c] #fiz uma lista para poder usar max e min
maior = max(numeros)
menor = min(numeros)

if (a != maior) or (a != menor): # se A não for o maior ou o menor, A é o do meio
  meio = a
elif (b != menor) or (b != maior): # se B não for o maior ou o menor, B é o do meio
  meio = b

else:
  meio = c #se nem A nem B forem meio, o meio é C.

if (a != b) and (a != c) and (b != c): #Se forem todos diferentes
  print(f"maior: {maior}")
  print(f"menor: {menor}")
  print(f"meio: {meio}")

if (a == b == c): #Se forem todos iguais
  print(f"todos são iguais a {a}")

if (a == b != c) or (a == c != b) or (b == c != a): #Se tiverem dois iguais e um diferente
  print(f"maior: {maior}")
  print(f"menores: {menor}")
  print("não há elementos do meio")