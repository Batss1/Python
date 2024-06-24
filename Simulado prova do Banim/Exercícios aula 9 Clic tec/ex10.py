# 10. Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
# aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random). Exiba na tela a lista gerada. Em
# seguida, o programa deve ler um valor X e informar se tal valor está, ou não está presente, bem como informar a
# posição de X na lista. Se houver mais de uma ocorrência de X na lista informe todas as posições. Neste exercício
# não é permitido usar os operadores in e not in. Também não é permitido usar qualquer função pronta de Python.

from random import randint

N = int(input('Digite o número de elementos para a lista: '))
lista = []
for c in range(N):
    num = randint(0,1000)
    lista.append(num)

print(lista)

print('\nVerificador')
X = int(input('Digite um número para ver se está na lista: '))

#Verifica sem o uso de in e not in, se o número está na lista
cont = 0
posicao = 0
while cont < N:
    if lista[cont] == X:
        posicao = cont + 1
    cont += 1

if posicao == 0:
    print(f'O número {X} não está na lista')
else:
    print(f'O número {X} está na lista, sua posição é a {posicao}')

