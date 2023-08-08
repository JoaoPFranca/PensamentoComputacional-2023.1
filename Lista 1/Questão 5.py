# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

# 1 - o produto do dobro do primeiro com metade do segundo .
# 2 - a soma do triplo do primeiro com o terceiro.
# 3 - o terceiro elevado ao cubo.

# Primeiro Número (inteiro): 2
# Segundo Número (inteiro): 4
# Terceiro Número (real): 2.5

# Saída

# o produto do dobro do primeiro com metade do segundo é: 8
# A soma do triplo do primeiro com o terceiro é: 8.5
# o terceiro elevado ao cubo é: 15.625

a = int(input("Primeiro Número (inteiro):"))
b = int(input("Segundo Número (inteiro):"))
c = float(input("Terceiro Número (real):"))  #O float aceita casas decimais

primeiraCondicao = (a * 2) * (b / 2)
segundaCondicao = (a * 3) + c
terceiraCondicao = (c * c * c)

print(
  f"o produto do dobro do primeiro com metade do segundo é: {primeiraCondicao}"
)
print(f"A soma do triplo do primeiro com o terceiro é: {segundaCondicao}")
print(f"o terceiro elevado ao cubo é: {terceiraCondicao}")

#Para aceitar um número ilimitado de casas decimais, preferi por não formatar as condições
