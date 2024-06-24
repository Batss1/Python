# 16. Escreva um programa que leia uma lista com N números inteiros, onde N é um número inteiro previamente
# digitado pelo usuário. O programa não deve aceitar um número digitado que já esteja inserido na lista, sendo que
# quando esta situação ocorrer uma mensagem deve ser dada ao usuário. Por fim exibir na tela a lista resultante.
N = int(input("Digite o tamanho da lista: "))
lista = []

for i in range(N):
    novo_numero = int(input("Digite um número inteiro: "))
    if novo_numero in lista:
        print("Este número já está na lista. Por favor, insira outro número.")
    else:
        lista.append(novo_numero)

print("Lista resultante:", lista)