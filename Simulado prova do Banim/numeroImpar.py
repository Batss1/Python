"""Solução do exercício 8 da lista de exrcídios da aula 6
   versão B - solução usando um busca exaustiva com interrupção no momento
   em que o resultado fique evidente"""

N = int(input('Digite um inteiro: '))
while N >= 2:
    if N == 2:  # 2 é primo
        Resto = 1
    elif N % 2 == 0:  # N é par e maior que 2
        Resto = 0  
    else: # verificação de ímpares
        # aqui começa o algoritmo de teste exaustivo
        Resto = 1
        raiz = N ** 0.5
        i = 3
        while i <= raiz and Resto != 0:  # neste algoritmo sempre existem 2 condições para permanência no laço
            Resto = N % i
            i += 2

    if Resto != 0:
        print(f'{N} é Primo')
    else:
        print(f'{N} não é Primo')

    N = int(input('Digite um inteiro: '))

print('\nFim do Programa')




"""Solução do exercício 8 da lista de exrcídios da aula 6
   versão A - solução usando um contador"""

N = int(input('Digite um inteiro: '))
while N >= 2:
    cont = 0
    i = 2
    while i < N:
        if N % i == 0:
            cont += 1
        i += 1

    if cont == 0:
        print(f'{N} é Primo')
    else:
        print(f'{N} não é Primo')

    N = int(input('Digite um inteiro: '))

print('\nFim do Programa')




