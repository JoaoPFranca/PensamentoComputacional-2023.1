# Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

# Nome do Atleta: Eduardo Aranha
# Nota_1: 9.9
# Nota_2: 7.5
# Nota_3: 9.5
# Nota 4: 8.5
# Nota_5: 9.0
# Nota_6: 8.5
# Nota_7: 9.7

# Resultado final:
# Atleta: Eduardo Aranha
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

atleta = input("Nome do Atleta: ")
n1 = float(input("Nota_1: "))
n2 = float(input("Nota_2: "))
n3 = float(input("Nota_3: "))
n4 = float(input("Nota_4: "))
n5 = float(input("Nota_5: "))
n6 = float(input("Nota_6: "))
n7 = float(input("Nota_7: "))

notas = [n1, n2, n3, n4, n5, n6,n7]  #Coloca tudo numa lista para poder usar max, min, sum e remove

maior = max(notas)
menor = min(notas)

notas.remove(maior)  #tira da lista. sua sintaxe é lista.remove(posicao)
notas.remove(menor)

media = (sum(notas) / 5)  #sum é soma

print(" ")  #só pra ficar bonito no output
print("Resultado Final:")
print(f"Nome do Atleta: {atleta}")
print(f"Melhor nota: {maior}")
print(f"Pior nota: {menor}")
print(f"Média: {media:.2f}")
