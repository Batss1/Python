# 11. Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
# aleatoriamente entre 0 e 1000. Exiba na tela a lista gerada. Em seguida, o programa deve ler um valor X e, caso X
# esteja na lista, deve eliminá-lo. Caso haja várias ocorrências de X, todas devem ser eliminadas. Pesquise como
# usar a função del (você vai precisar dela e neste exercício será permitido usá-la).

N = int(input('Digite o número de elementos para a lista: '))
lista = []
for c in range(N):
    num = randint(0,1000)
    lista.append(num)

print(lista)

print('\nVerificador')
X = int(input('Digite um número para ver se está na lista: '))

deletados = []
contador = 0

#Deleta o número digitado caso apareça na lista
for c in range(N-1):
    if X == lista[c]:
        del(lista[c])
        contador += 1
#Apresenta o número e a quantidade de vezes q foi deletado da lista, ao final apresenta a lista nova
if contador == 0:
    print(f'O número {X} não está na lista')
else:
    print(f'O número {X} foi deletado da lista {contador} vez(es)')

    print(f'\nA lista agora é: {lista}')