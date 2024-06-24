# Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50 – o programa deve garantir isso em
# um laço) e em seguida leia N números reais em uma lista A. O programa deve separar os valores lidos em A em
# outras duas listas NEG e POS, a primeira contendo somente os valores negativos e a segunda contendo os valores
# positivos e zero. Apresentar na tela as listas NEG e POS e a quantidade de valores contidos em cada uma. Colocar
# este programa no site do professor.

# N = int(input('Digite um número: '))
# while N < 0 and N > 50:
#     N = int(input('Digite um número entre 0 e 50: '))
# cont = 0
# A = []
# while cont < N:
#     num = float(input(f'Digite o {cont+1}º número: '))
#     cont += 1
#     A.append(num)

# contNeg = 0
# contPos = 0
# NEG = []
# POS = []
# for c in A:
#     if c < 0:
#         NEG.append(c)
#         contNeg += 1
#     else:
#         POS.append(c)
#         contPos += 1

# print(f'A lista NEG é: {NEG}, existe {contNeg} elementos na lista')
# print(f'A lista POS é: {POS}, existe {contPos} elementos na lista')



# Leia dois números inteiros LMin e LMax. Em seguida leia 10 valores inteiros e inserindo-os em uma lista A somente
# se o valor fornecido estiver no intervalo [LMin, LMax]. Valores fora deste intervalo devem ser ignorados. Ao final,
# apresentar a lista A e seu tamanho efetivo. Observe que para este programa funcionar apropriadamente é
# necessário que LMin seja menor que LMax. Caso o usuário digite LMax menor que LMin, o programa deve inverter
# os valores. Colocar este programa no site do professor


# LMin = int(input('Digite o valor de LMin: '))
# LMax = int(input('Digite o valor de LMax: '))

# if LMin > LMax:
#     LMin, LMax = LMax, LMin
# A = []
# contExcluidos = 0
# for c in range(10):
#     num = int(input('Digite um número: '))
#     if num >= LMin and num <= LMax:
#         A.append(num)
#     else:
#         contExcluidos += 1
# print(A)
# print(f'O tamanho da lista efetiva é: {10 - contExcluidos}')




# Refaça o exercício anterior generalizando-o para N valores inteiros digitados no teclado, onde N é um número
# fornecido pelo usuário. Esse N deve ser usado no programa ao invés do tamanho fixo de 10 sugerido no programa
# anterior. Colocar este programa no site do professor

# LMin = int(input('Digite o valor de LMin: '))
# LMax = int(input('Digite o valor de LMax: '))
# N = int(input('Digite a quantidade de valores: '))

# if LMin > LMax:
#     LMin, LMax = LMax, LMin
# A = []
# contExcluidos = 0
# for c in range(N):
#     num = int(input('Digite um número: '))
#     if num >= LMin and num <= LMax:
#         A.append(num)
#     else:
#         contExcluidos += 1
# print(A)
# print(f'O tamanho da lista efetiva é: {N - contExcluidos}')




# Refaça o exercício anterior de modo que os valores inválidos, ou seja, os que estão fora do intervalo [Min, Max]
# sejam inseridos em uma segunda lista chamada R. Apresentar na tela a lista de valores aceitos (lista A) e a lista de
# valores rejeitados (lista R), bem como o tamanho de cada um. Colocar este programa no site do professor.

# LMin = int(input('Digite o valor de LMin: '))
# LMax = int(input('Digite o valor de LMax: '))
# N = int(input('Digite a quantidade de valores: '))

# if LMin > LMax:
#     LMin, LMax = LMax, LMin
# A = []
# R = []
# contExcluidos = 0
# for c in range(N):
#     num = int(input('Digite um número: '))
#     if num >= LMin and num <= LMax:
#         A.append(num)
#     else:
#         R.append(num)
#         contExcluidos += 1
# print(f'\nNúmeros aceitos: {A}')
# print(f'Números rejeitados: {R}')
# print(f'\nO tamanho da lista efetiva é: {N - contExcluidos} \nE o da lista excluida é:  {contExcluidos}\n')
