# Escreva um programa que lê a quantidade dos alunos de uma turma. Em seguida, o programa deve ler os nomes de cada aluno e imprimi-los na ordem inversa.


# Exemplo 1

# Quantos nomes? 3
# João
# Paulo
# Augusto
# Você digitou:
# Augusto
# Paulo
# João

qtd = int(input("Digite a quantidade de alunos na turma: "))

listaAlunos = [] #faz uma lista de alunos
for i in range(qtd): #para i até o intervalo qtd
    nome = input() #adiciona o nome
    listaAlunos.append(nome) # o append adiciona um nome ao final da lista

print("Você digitou: ")
for nome in reversed(listaAlunos):
    print(nome)