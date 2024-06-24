# 15. Escreva um programa que preencha com números inteiros duas listas denominadas A e B com diferentes
# tamanhos nA e nB, respectivamente. Em seguida o programa deve juntar as duas listas em uma única lista com o
# tamanho nA+nB. Exibir na tela a lista resultante. Veja o exemplo:

# Lendo os tamanhos das listas A e B
nA = int(input("Digite o tamanho da lista A: "))
nB = int(input("Digite o tamanho da lista B: "))

# Preenchendo a lista A com números inteiros
A = [int(input(f"Digite o {i+1}º número da lista A: ")) for i in range(nA)]

# Preenchendo a lista B com números inteiros
B = [int(input(f"Digite o {i+1}º número da lista B: ")) for i in range(nB)]

# Juntando as duas listas em uma única lista
lista_combinada = A + B

print("Lista combinada:", lista_combinada)