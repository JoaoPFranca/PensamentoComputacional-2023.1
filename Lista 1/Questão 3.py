#Escreva um programa que recebe do usuário dois textos, A e B, e imprime os resultados das operações tamanho(A) - tamanho(B), A + B, A contém B, B contém A, primeira letra de A, primeira letra de B, última letra de A, última letra de B.

# Digite o texto A: testando
# Digite o texto B: test
# tamanho(A) - tamanho(B) = 4
# A + B = testandotest
# A contém B = True
# B contém A = False
# Primeira letra de A = t
# Primeira letra de B = t
# Última letra de A = o
# Última letra de B = t

a = input("Digite o texto A: ")
b = input("Digite o texto B: ")

tamanhoA = len(a) #lenght(tamanho) de a
tamanhoB = len(b) #lenght(tamanho) de b

subtracaoTamanhos = tamanhoA - tamanhoB #o lenght conta o número de caracteres

somaString = a + b #aqui não estamos usando os lenghts. aqui é uma concatenação

aContemB = False #Importante: Antes de usar uma variável, temos que declarar
if b in a:
  aContemB = True

bContemA = False #Então se fosse um int, seria bContemA = 0, se fosse uma string era bContemA = null... etc
if a in b:
  bContemA = True

primeiraLetraA = a[0] #NO PYTHON A CONTAGEM COMEÇA NO ZERO
primeiraLetraB = b[0]

ultimaLetraA = a[-1] #Não existe -0, então se usa o -1 pra pegar a última letra
ultimaLetraB = b[-1]

print(f"tamanho(A) - tamanho(B) = {subtracaoTamanhos}")
print(f"A + B = {somaString}")
print(f"A contém B =  {aContemB}")
print(f"B contém A =  {bContemA}")
print(f"Primeira letra de A = {primeiraLetraA}")
print(f"Primeira letra de B = {primeiraLetraB}")
print(f"Última letra de A = {ultimaLetraA}")
print(f"Última letra de B = {ultimaLetraB}")
