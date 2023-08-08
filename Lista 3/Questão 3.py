# faça um programa que leia dois números n1 e n2, onde 1 <= n1 <= n2 <= 10, e que imprima a tabuada dos números entre n1 e n2, conforme exemplo.

# Exemplo (os ... é uma abreviação, mas deve ser completado)

  
# Digite n1: 2
# Digite n2: 4
# =-=-=-= Tabuada de 2 =-=-=-=
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 9 = 18
# 2 x 10 = 20
# =-=-=-= Tabuada de 3 =-=-=-=
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 9 = 27
# 3 x 10 = 30
# =-=-=-= Tabuada de 4 =-=-=-=
# 4 x 1 = 4
# 4 x 2 = 8
# ...
# 4 x 9 = 36
# 4 x 10 = 40

n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))

for numero in range(n1, n2 + 1):
    print(f"=-=-=-= Tabuada de {numero}=-=-=-=")
    for i in range(1, 10 + 1):
        print(f"{numero} x {i} = {numero * i}")
  
