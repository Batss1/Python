# 2. Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-o na tela na ordem
# inversa à ordem de leitura, sendo um elemento por linha da tela.
lista = []
#pergunta um número e adiciona na lista
for c in range(10):
    num = int(input(f'Digite o {c+1}º número:'))
    lista.append(num)
#printa um elemento da lista por linha
print('\n')
for c in lista[::-1]:
    print(c)


    #contador = 9

    #while contador >=0:
    #    print(lista[contador])
    #    contador -= 1