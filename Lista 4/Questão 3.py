# Em uma turma de alunos que conversavam muito, um professor montou a seguinte estratégia. Após os alunos se sentarem, ele mandava os alunos trocarem de lugar. Para ajudar esse processo, crie um programa para ajudar esse professor. O programa deve ler um valor N, que representa a quantidade de alunos. Em seguida, deve ler os nomes de cada aluno. Considere a sequência lida como a ordem das cadeiras dos alunos. O programa deve então imprimir os nomes em uma nova ordem, trocando os alunos sentados em cadeiras de número par (o da primeira cadeira par vai para a última par, o da segunda para a antepenúltima, etc.).
# Se houver uma quantidade ímpar de cadeiras pares (em uma turma de 7 alunos, vão haver 3 cadeiras pares), o aluno da cadeira central não terá seu local trocado.

# Quantos alunos? 7
# Digite os nomes dos alunos:
# Joao
# Maria
# Afonso
# Tenorio
# Kleber
# Airton
# Tulio

# Nova lista:
# Joao
# Airton
# Afonso
# Tenorio
# Kleber
# Maria
# Tulio

n = int(input("Quantos alunos? "))

alunos = []
for i in range(n):
    nome = input("Digite o nome do aluno {}: ".format(i + 1))
    alunos.append(nome)

meio = n // 2
for i in range(meio):
    if n % 2 == 0:  
        if i % 2 == 0:
            alunos[i], alunos[n - i - 1] = alunos[n - i - 1], alunos[i]
    else:  
        if i % 2 != 0:
            alunos[i], alunos[n - i - 1] = alunos[n - i - 1], alunos[i]


print("Nova lista:")
for aluno in alunos:
    print(aluno)

