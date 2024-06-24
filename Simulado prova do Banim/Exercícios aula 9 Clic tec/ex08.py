# Refaça o exercício anterior de modo que os valores inválidos, ou seja, os que estão fora do intervalo [Min, Max]
# sejam inseridos em uma segunda lista chamada R. Apresentar na tela a lista de valores aceitos (lista A) e a lista de
# valores rejeitados (lista R), bem como o tamanho de cada um. Colocar este programa no site do professor.

LMin = int(input('Digite o valor de LMin: '))
LMax = int(input('Digite o valor de LMax: '))
N = int(input('Digite a quantidade de valores: '))

if LMin > LMax:
    LMin, LMax = LMax, LMin
    
A = []
R = []
contExcluidos = 0
for c in range(N):
    num = int(input('Digite um número: '))
    if num >= LMin and num <= LMax:
        A.append(num)
    else:
        R.append(num)
        contExcluidos += 1
print(f'\nNúmeros aceitos: {A}')
print(f'Números rejeitados: {R}')
print(f'\nO tamanho da lista efetiva é: {N - contExcluidos} \nE o da lista excluida é:  {contExcluidos}\n')