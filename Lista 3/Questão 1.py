#Escreva um programa que receba um número N para gerar os N primeiros termos da série de Fibonacci: 1, 1, 2, 3, 5, 8, 13, …

# número de termos: 5

# série de Fibonacci: 1 1 2 3 5

n = int(input("número de termos: "))

fibonacci = [1, 1]  # Começa sequência com os dois primeiros termos: 1 e 1, para que seja possível pegar o 2 e assim vai.

if n <= 2:
    fibonacci = fibonacci[:n] 
else:
    while len(fibonacci) < n:
        proxTermo = fibonacci[-1] + fibonacci[-2]  # Calcula o próximo termo
        fibonacci.append(proxTermo)  # Adiciona o próximo termo à sequência ao final da lista

print("série de Fibonacci:", ' '.join(map(str, fibonacci))) #A função map() é usada para converter cada elemento da lista em uma string usando a função str(), e o método join() é usado para concatenar todos os elementos da lista em uma única string separada por espaço.