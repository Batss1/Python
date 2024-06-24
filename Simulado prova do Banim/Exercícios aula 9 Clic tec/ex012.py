# 12. Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros digitados pelo
# usuário. Exiba na tela a lista preenchida. Em seguida, o programa deve procurar e eliminar os elementos que
# eventualmente estiverem repetidos deixando apenas a primeira ocorrência de cada valor. Apresentar a lista
# resultante na tela.

N = int(input('Digite o número de elementos da lista: '))
lista = []
cont = 0

while cont < N:
    numero = int(input(f'Digite um número da lista: '))
    lista.append(numero)
    cont += 1

print('Lista inicial: ', lista)

listaFinal = []
repetidos = []
for c in range(N):
    if lista[c] not in listaFinal:
        listaFinal.append(lista[c])
    else:
        repetidos.append(lista[c])

print('A lista final sem números repetidos: ', listaFinal)
print('Os números repetidos são: ', repetidos)
