# Monte uma tabela-verdade com os valores de A AND B e A OR B por meio de um programa. Para isso, seu programa deve receber o valor booleano para as variáveis A e B e então imprimir na tela os valores respectivos para cada operação (AND e OR), como no exemplo.

# Dica: Associe os valores de 0 para False e 1 para True por meio de uma condicional.

# OBS.: Valores diferentes de 0 e 1 devem ser considerados inválidos.

# Valor lógico de A eh: 1
# Valor lógico de B eh: 0

# A AND B eh: False
# A OR B eh: True

a = int(input("Valor lógico de A eh: "))
b = int(input("Valor lógico de B eh: "))

if a not in (0, 1) or b not in (0, 1): # Se A ou B não estiverem no conjunto [0, 1], printa a mensagem de erro
  print("Coloque apenas 0 ou 1.")

else:
  e = a and b  # Faz o AND
  ou = a or b  # Faz o OR

  print(f"A AND B é: {bool(e)}")
  print(f"A OR B é: {bool(ou)}")