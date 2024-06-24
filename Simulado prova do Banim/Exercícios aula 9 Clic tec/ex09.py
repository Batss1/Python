# Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
# aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random). Exiba na tela a lista gerada. Em
# seguida, o programa deve ler um valor X e informar se tal valor está, ou não está presente na lista. Neste exercício
# é permitido usar os operadores in e/ou not in.

from random import randint

N = int(input('Digite o número de elementos para a lista: '))
lista = []
for c in range(N):
    num = randint(0,1000)
    lista.append(num)

print(lista)

#Verifica através de in e not in, se o número está na lista
print('\nVerificador')
X = int(input('Digite um número para ver se está na lista: '))

if X in lista:
    print(f'O número {X} está na lista')
else:
    print(f'O número {X} não está na lista')