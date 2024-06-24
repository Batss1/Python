# 19. Faça um programa que permaneça em laço até que seja digitado um valor menor ou igual a zero. Cada valor válido
# (positivo) digitado deve ser inserido em uma lista na posição imediatamente antes do primeiro elemento que seja
# maior que valor que está sendo inserido. Isso resultará em uma lista ordenada de forma crescente. Será
# necessário usar o método insert da lista – pesquise sobre ele.


lista = []

valor = int(input("Digite um valor (digite 0 ou um número negativo para parar): "))

# Enquanto o valor digitado for positivo, continua o loop
while valor > 0:
    # Encontrando a posição onde o valor deve ser inserido para manter a ordem crescente
    posicao = 0
    while posicao < len(lista) and lista[posicao] <= valor:
        posicao += 1
    
    # Inserindo o valor na posição adequada
    lista.insert(posicao, valor)

    valor = int(input("Digite um valor (digite 0 ou um número negativo para parar): "))

print("Lista ordenada:", lista)