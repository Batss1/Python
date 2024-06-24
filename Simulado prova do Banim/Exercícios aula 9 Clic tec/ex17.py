# 17. Escreva um programa que leia do teclado dois números inteiros nA e nB e leia também duas listas denominados
# A e B com os tamanhos nA e nB, respectivamente. Na leitura de cada uma das listas é obrigatório que não sejam
# aceitos valores repetidos. Em seguida, o programa deve juntar as duas listas em um única lista R (resultante)
# tomando o cuidado de que a lista R não deve ter valores duplicados. Veja o exemplo:


nA = int(input("Digite o tamanho da lista A: "))
A = []

# Preenchendo a lista A sem valores repetidos
for i in range(nA):
    novo_numero = int(input(f"Digite o {i+1}º número da lista A: "))
    while novo_numero in A:
        print("Este número já está na lista. Por favor, insira outro número.")
        novo_numero = int(input(f"Digite o {i+1}º número novamente da lista A: "))
    A.append(novo_numero)

# Lendo o tamanho da lista B
nB = int(input("Digite o tamanho da lista B: "))
B = []

# Preenchendo a lista B sem valores repetidos
for i in range(nB):
    novo_numero = int(input(f"Digite o {i+1}º número da lista B: "))
    while novo_numero in B:
        print("Este número já está na lista. Por favor, insira outro número.")
        novo_numero = int(input(f"Digite o {i+1}º número novamente da lista B: "))
    B.append(novo_numero)

# Juntando as duas listas e removendo valores duplicados
R = []
for num in A + B:
    if num not in R:
        R.append(num)

print("Lista resultante:", R)

