# 20. Faça um programa que leia um número inteiro N obrigatoriamente maior que 10. Preencha uma lista de tamanho
# N com números inteiros aleatórios. Exiba na tela a lista gerada e em seguida coloque-a em ordem crescente
# usando o método da bolha. Não é permitido usar o método sort da lista


import random

# Lendo o valor de N
N = int(input("Digite um número inteiro maior que 10: "))
while N <= 10:
    N = int(input("Por favor, digite um número inteiro maior que 10: "))

# Preenchendo a lista com números inteiros aleatórios
lista = [random.randint(1, 100) for _ in range(N)]

print("Lista gerada:", lista)

# Ordenando a lista usando o método da bolha
for i in range(N):
    for j in range(0, N-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print("Lista ordenada:", lista)