# # Escreva um programa que faça a criptografia de uma palavra, da seguinte forma:
# Letras de "a" até "e" - 1
# Letras de "f" até "j" - 2
# Letras de "k" até "o" - 3
# Letras de "p" até "z" - 4
# Espaço ou qualquer outro caracter - 5
# O programa deve ter uma função que recebe, como parâmetro de entrada, uma palavra e retorne o valor encriptado correspondente. Seu programa deve realizar a leitura do texto fora da função e usá-la bem como seu retorno para imprimir a saída como os exemplos mostram.


# Exemplo 1

# Digite o texto: Isabel
# Encriptado: 241113

# Digite o texto: Lua de mel
# Encriptado: 3415115313

def encriptar_palavra(palavra): 
    encriptado = "" #Indica que é uma função de String
    for letra in palavra: #checa cada caracter
        if letra >= 'a' and letra <= 'e':
            encriptado += '1' #alimenta a variavel encriptado com o valor 1.
        elif letra >= 'f' and letra <= 'j':
            encriptado += '2'
        elif letra >= 'k' and letra <= 'o':
            encriptado += '3'
        elif letra >= 'p' and letra <= 'z':
            encriptado += '4'
        else:
            encriptado += '5'
    return encriptado

texto = input("Digite o texto: ").lower() #usei o lower pq quando colocava "Isabel", o I voltava 5.
encriptado = encriptar_palavra(texto)
print("Encriptado:", encriptado)