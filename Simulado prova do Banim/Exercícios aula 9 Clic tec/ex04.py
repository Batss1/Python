# 4.Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50) e em seguida preencha uma lista
# com N elementos inteiros gerados aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random –
# veja o quadro sobre isso no exercício 9).
from random import randint
num = int(input('Digite um número(entre 0 e 50): '))
while num > 50 or num < 0:
    print('Número inválido, digite um número entre 0 e 50')
    num = int(input('Digite um número: '))
A = []
for c in range(num):
    num_lista = randint(0,1000)
    A.append(num_lista)
for c in A:
    print(c)