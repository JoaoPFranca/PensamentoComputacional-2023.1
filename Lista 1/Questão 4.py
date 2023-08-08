# Escreva um programa que recebe dois textos do usuário e imprime o valor das expressões de acordo com os exemplos:

# 1 - Texto A dividido em duas Partes: primeira_metade_texto(A) e segunda_metade_texto(A)
# 2 - Texto B dividido em duas Partes: primeira_metade_texto(B) e segunda_metade_texto(B)
# 3 - primeira_metade_texto(A) + segunda_metade_texto(B)
# 4 - segunda_metade_texto(A) + primeira_metade_texto(B)
# 5 - primeira_letra_texto(A) + segunda_letra_texto(B) + ultima_letra_texto(A) + ultima_letra_texto(B)

# Digite o texto A: uma_palavra_A
# Digite o texto B: outro_texto_B
# Texto A dividido em duas Partes: uma_pa e lavra_A
# Texto B dividido em duas Partes: outro_ e texto_B
# uma_pa + texto_B = uma_patexto_B
# lavra_A + outro_ = lavra_Aoutro_
# u + u + A + B = uuAB


a = input("Digite o texto A: ")
b = input("Digite o texto B: ")

tamanhoA = len(a) #tamanho de A
meioDeA = tamanhoA // 2 #aqui a gente tenta pegar o meio de A. 
primeiraMetadeA = a[:meioDeA] #para usar essa posição aqui
segundaMetadeA = a[meioDeA:]#os dois pontos antes dizem que é ANTES do número correspondente ao meio. os dois pontos depois, indicam que é DEPOIS dele.

tamanhoB = len(b)
meioDeB = tamanhoB // 2
primeiraMetadeB = b[:meioDeB]
segundaMetadeB = b[meioDeB:]

primeiraLetraA = a[0] #primeira posição
segundaLetraB = b[1] #segunda posição (O PYTHON COMEÇA NO ZERO)
ultimaLetraA = a[-1] #última posição
ultimaLetraB = b[-1]

print(f"Texto A dividido em duas Partes: {primeiraMetadeA} e {segundaMetadeA}")
print(f"Texto B dividido em duas Partes: {primeiraMetadeB} e {segundaMetadeB}")
print(f"{primeiraMetadeA} + texto_B = {primeiraMetadeA + 'texto_B'}") #detalhe para o uso das aspas simples
print(f"{segundaMetadeA} + {primeiraMetadeB} = {segundaMetadeA + primeiraMetadeB}")
print(f"{primeiraLetraA} + {segundaLetraB} + {ultimaLetraA} + {ultimaLetraB} = {primeiraLetraA + segundaLetraB + ultimaLetraA + ultimaLetraB}")