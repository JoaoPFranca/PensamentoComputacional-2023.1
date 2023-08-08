# Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. A cada jogo, seu auxiliar anota quantas tentativas de saques, bloqueios e ataques cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e ataques tiveram sucesso (resultaram em pontos). Seu programa deve mostrar qual o percentual de saques, bloqueios e ataques do time todo tiveram sucesso.

# Formato de entrada
# A primeira entrada é o número de jogadores N (N >= 1). Em seguida, para cada jogador, deve-se se ler uma linha com as seguintes informações: nome do jogador, os valores S, B e A, representam a quantidade de tentativas de saques, bloqueios e ataques; os valores S1, B1 e A1, representando o número de saques, bloqueios e ataques deste jogador que tiveram sucesso.

# Formato de saída
# A saída deve mostrar o percentual total de saques, bloqueios e ataques do time todo que resultaram em pontos, conforme mostrado no exemplo.

# Quantidade de jogadores? 3
# Digite os dados para cada jogador:
# Renan 10 20 12 1 10 9
# Jonas 8 7 1 2 7 0
# Edson 3 3 3 1 2 3
# As estatísticas do jogo são as seguintes:
# Pontos de Saque: 19.05 %
# Pontos de Bloqueio: 63.33 %
# Pontos de Ataque: 75.00 %

qtdJogadores = int(input("Quantidade de jogadores? "))
print("Digite os dados para cada jogador:")


#iniciando as variáveis
tentativasSaque = 0
tentativasBloqueio = 0
tentativasAtaque = 0
sucessosSaque = 0
sucessosBloqueio = 0
sucessosAtaque = 0
  
for i in range(qtdJogadores):
  dados = input().split() #O .split permite que peguemos vários dados dentro de um input único.
  nome = dados[0]
  s = int(dados[1])
  b = int(dados[2])
  a = int(dados[3])
  s1 =int(dados[4])
  b1 = int(dados[5])
  a1 = int(dados[6])

  tentativasSaque += s #alimentando a variável "tentativasSaque" com os dados de S
  tentativasBloqueio += b
  tentativasAtaque += a
  
  sucessosSaque += s1
  sucessosBloqueio += b1
  sucessosAtaque += a1

porcSaques = (sucessosSaque / tentativasSaque) * 100
porcBloqueio = (sucessosBloqueio / tentativasBloqueio) * 100
porcAtaque = (sucessosAtaque / tentativasAtaque) * 100

print("As estatísticas do jogo são as seguintes:")
print(f"Pontos de Saque: {porcSaques:.2f} %")
print(f"Pontos de Bloqueio: {porcBloqueio:.2f} %")
print(f"Pontos de Ataque: {porcAtaque:.2f} %")
  
  
  

