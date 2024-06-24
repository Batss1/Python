# 14. Escreva um programa que leia do teclado duas listas com tamanho 10, com números inteiros. Em seguida o
# programa deve juntar as duas listas em uma única lista com o tamanho 20. 
lista1 = [int(input(f"Digite o {i+1}º número da primeira lista: ")) for i in range(10)]
lista2 = [int(input(f"Digite o {i+1}º número da segunda lista: ")) for i in range(10)]

# Juntando as duas listas em uma única lista
lista_combinada = lista1 + lista2

print("Lista combinada:", lista_combinada)