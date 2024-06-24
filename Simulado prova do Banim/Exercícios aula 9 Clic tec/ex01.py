#1. Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-o na tela um elemento por linha.
lista = []
#pergunta um número e adiciona na lista
for c in range(10):
    num = int(input(f'Digite o {c+1}º número:'))
    lista.append(num)
#printa um elemento da lista por linha
for c in lista:
    print(c)