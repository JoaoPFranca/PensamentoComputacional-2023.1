# Escreva um programa que pede ao usuário um número de dias e converte esse número em semanas e dias. Observe que existem muitos casos específicos a serem tratados, uma vez que faz diferença dizer "dia" ou "dias", bem como "semana" ou "semanas", por exemplo:

# Se o usuário digitar 0, o programa deve exibir: 0 dias equivale à nenhum dia.
# Se o usuário digitar 7, o programa deve exibir: 7 dias equivalem à 1 semana!
# Se o usuário digitar 8, o programa deve exibir: 8 dias equivalem à 1 semana e 1 dia!
# Se o usuário digitar 30, o programa deve exibir: 30 dias equivalem à 4 semanas e 2 dias!

# Digite um número: 30

# Saída:

# 30 dias equivalem à 4 semanas e 2 dias!

num = int(input("Digite um número: "))

semanas = int(num / 7)
dias = num % 7

if (num == 0):
  print("0 dias equivale à nenhum dia.") #0 dias

elif (num == 1):
  print("1 dia equivale à 1 dia!") #1 dia

elif (num < 7):
  print(f"{num} dias equivalem à {num} dias!") #menos de uma semana (apenas dias)

elif (num == 7):
  print("7 dias equivalem à 1 semana!") #apenas uma semana

elif (num == 8):
  print("8 dias equivalem à 1 semana e 1 dia!") #tudo no singular

elif (dias == 0 and num != 7):
  print(f"{num} dias equivalem à {semanas} semanas!") #se o resto for 0 e for diferente de uma semanA

elif (num > 7 and dias != 0 and dias != 1):
  print(f"{num} equivalem à {semanas} semanas e {dias} dias!") #Aqui tratamos: O singular de semanas em "num > 7", o resto da divisão ser 0 e 1 (pra evitar o plural em 1)

elif (num > 7 and dias == 1):
  print(f"{num} equivalem à {semanas} semanas e {dias} dia!") #Aqui eu trato apenas o plural em 1 dia
