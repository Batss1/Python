# Refaça o exercício anterior generalizando-o para N valores inteiros digitados no teclado, onde N é um número
# fornecido pelo usuário. Esse N deve ser usado no programa ao invés do tamanho fixo de 10 sugerido no programa
# anterior. Colocar este programa no site do professor

LMin = int(input('Digite o valor de LMin: '))
LMax = int(input('Digite o valor de LMax: '))
N = int(input('Digite a quantidade de valores: '))

if LMin > LMax:
    LMin, LMax = LMax, LMin
    
A = []
contExcluidos = 0
for c in range(N):
    num = int(input('Digite um número: '))
    if num >= LMin and num <= LMax:
        A.append(num)
    else:
        contExcluidos += 1
print(A)
print(f'O tamanho da lista efetiva é: {N - contExcluidos}')