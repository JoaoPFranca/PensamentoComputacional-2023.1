# A ordem lexicográfica é a ordem das palavras usada em um dicionário, por exemplo, o verbo "ser" vem antes da palavra "seres", na ordem lexicográfica. Embora possa parecer que tem algo a ver com o tamanho da palavra, a palavra "testando" viria antes da palavra "testes" na ordem lexicográfica.

# Na linguagem python, podemos testar se uma plavra vem antes da outra de acordo com a ordem lexicográfica usando os operadores ">" ou "<". Dessa forma sejam as palavras A e B, se A < B, a vem antes de B; de forma análoga, se A > B, B vem antes de A. Obs: para comparações da ordem lexicográfica, considere os textos todos minúsculos!

# Assim escreva um programa que lê três textos do usuário e os imprime na ordem lexicográfica de acordo com os exemplos abaixo:

# Texto 1? casa
# Texto 2? testes
# Texto 3? testando
# Seguem os textos em ordem:
# 1o. casa
# 2o. testando
# 3o. testes]

a = input("Texto 1? ").lower()  #minúsculo
b = input("Texto 2? ").lower()
c = input("Texto 3? ").lower()
print("Seguem os textos em ordem:")

if a < b < c:  #ordenação de cada caso
  print(f"1o. {a}")
  print(f"2o. {b}")
  print(f"3o. {c}")

elif a < c < b:
  print(f"1o. {a}")
  print(f"2o. {c}")
  print(f"3o. {b}")

elif b < a < c:
  print(f"1o. {b}")
  print(f"2o. {a}")
  print(f"3o. {c}")

elif b < c < a:
  print(f"1o. {b}")
  print(f"2o. {c}")
  print(f"3o. {a}")

elif c < a < b:
  print(f"1o. {c}")
  print(f"2o. {a}")
  print(f"3o. {b}")

else:  #se for c < b < a
  print(f"1o. {c} ")
  print(f"2o. {b} ")
  print(f"3o. {a} ")
