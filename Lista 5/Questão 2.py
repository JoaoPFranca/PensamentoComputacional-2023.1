# O código abaixo é um código usado em um Caixa Eletrônico:

# saldo = 1000
# while True: #loop principal
# print('Qual operacao voce deseja realizar?')
# print('1 - SAQUE')
# print('2 - DEPOSITO')
# print('3 - SALDO')
# print('4 - SAIR')
# opcao = int(input('Escolha:'))
# if opcao == 1: #funcionalidade saque
# valor_sacado = float(input('Qual valor você deseja sacar?'))
# if valor_sacado <= saldo:
# saldo = saldo - valor_sacado
# print('Saque autorizado.' + 'Agora o seu saldo atual é de: ' + str(saldo) )
# else:
# print('Saldo insuficiente.')
# elif opcao == 2: #funcionalidade deposito
# valor_deposito = float( input('Qual o valor que você quer depositar?') )
# if valor_deposito > 0:
# saldo = saldo + valor_deposito
# print(str('O seu saldo agora é de: ') + str(saldo) )
# else:
# print('Valor inválido')
# elif opcao == 3: #funcionalidade saldo
# print(str('O seu saldo atual é de: ') + str(saldo))
# elif opcao == 4: #sair
# print('Obrigado por usar os serviços do Caixa Eletrônico')
# break
# else :
# print('Opção inválida, tente novamente!')

# O engenheiro de Software pediu para organizarmos o código usando funções simples, mas sem usar variáveis globais. Assim o código deve ter as seguintes funções:

# Função exibeOpcoes: imprime as opções, lê a escolha do usuário e retorna o valor inteiro da opção escolhida

# Função processaOpcoes: recebe como parâmetro as variáveis opcao e saldo e processa o valor de opcao para charmar as funções: deposito, saque ou saldo. A função também deve usar o retorno sa funções saque e deposito para atualizar o valor do saldo e retornar o valor do saldo atualizado depois das operações.

# Função saldo: recebe como parâmetro o valor do saldo e imprime seu valor.

# Função saque: recebe como parâmetro o valor do saldo, implementa a funcionalidade de saque e retorna o valor do saldo atualizado

# Função deposito: recebe como parâmetro o valor do saldo, implementa a funcionalidade de deposito e retorna do saldo atualizado

# Função principal: implementa o loop principal e chama as funcões exibeOpcoes e processaOpcoes. Essa função deve usar o valor de retorno da função exibeOpocoes para verificar se o usuário quer sair, antes de chamar a função processaOpcoes. Essa função deve também usar o retorno da função processaOpcoes para atualizar o valor da variável saldo.

# Com as implementações das funções o programa deve ficar assim:

# #funcao principal
# #funcao saldo
# #funcao depositio
# #funcao saque
# #funcao exibeOpcoes
# #funcao processaOpcoes


# def principal():
# opcao = 0
# saldo = 1000
# ... resto da implementação da função principal

# principal()


# Exemplo 1

# Qual operacao voce deseja realizar?
# 1 - SAQUE
# 2 - DEPOSITO
# 3 - SALDO
# 4 - SAIR
# Escolha: 2
# Qual o calor depositado: 400
# O seu saldo agora é de: 1400.0

def exibeOpcoes():
    print('Qual operação você deseja realizar?')
    print('1 - SAQUE')
    print('2 - DEPÓSITO')
    print('3 - SALDO')
    print('4 - SAIR')
    opcao = int(input('Escolha: '))
    return opcao

def processaOpcoes(opcao, saldo):
    if opcao == 1: # funcionalidade saque
        saldo = saque(saldo)
    elif opcao == 2: # funcionalidade depósito
        saldo = deposito(saldo)
    elif opcao == 3: # funcionalidade saldo
        print('O seu saldo atual é de:', saldo)
    elif opcao == 4: # sair
        print('Obrigado por usar os serviços do Caixa Eletrônico')
        exit()
    else:
        print('Opção inválida, tente novamente!')
    return saldo

def saque(saldo):
    valor_sacado = float(input('Qual valor você deseja sacar? '))
    if valor_sacado <= saldo:
        saldo -= valor_sacado
        print('Saque autorizado. Agora o seu saldo atual é de:', saldo)
    else:
        print('Saldo insuficiente.')
    return saldo

def deposito(saldo):
    valor_deposito = float(input('Qual o valor que você quer depositar? '))
    if valor_deposito > 0:
        saldo += valor_deposito
        print('O seu saldo agora é de:', saldo)
    else:
        print('Valor inválido')
    return saldo

def principal():
    saldo = 1000
    while True:
        opcao = exibeOpcoes()
        saldo = processaOpcoes(opcao, saldo)

principal()