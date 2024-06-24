# 3. Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50) e em seguida leia N números reais
# em uma lista A. Exiba a lista na tela, um elemento por linha.

num = int(input('Digite um número(entre 0 e 50): '))
while num > 50 or num < 0:
    print('Número inválido, digite um número entre 0 e 50')
    num = int(input('Digite um número: '))
A = []
for c in range(num):
    num_lista = int(input(f'Digite o {c+1}º valor da lista: '))
    A.append(num_lista)
for c in A:
    print(c)