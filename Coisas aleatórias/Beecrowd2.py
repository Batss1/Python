# cont = 0
# N = int(input('d'))
# while cont < N:
#     soma = 0
#     X, Y = map(int, input('d').split())
#     if X > Y:
#         X, Y = Y, X
#     X += 1
#     while X < Y:
#         if X % 2 != 0:
#             soma += X
#             X += 2
#         else:
#             X += 1
#     print(soma)
#     cont +=1




# Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero).
# Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).


# M, N = input('Entrada: ').split()
# M = int(M)
# N = int(N)
# soma = 0
# while M > 0 and N > 0:
#     if M > N:
#         M,N = N,M
#     while M <= N:
#         print(M,end=' ')
#         soma += M
#         M +=1
#     print(f'Sum={soma}')
#     M, N = input('Entrada: ').split()
#     M = int(M)
#     N = int(N)
#     soma = 0




# Leia uma quantidade indeterminada de duplas de valores inteiros X e Y.
# Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.


# X, Y = input().split()
# X = int(X)
# Y = int(Y)

# while X != Y:
#     if X > Y:
#         print('Decrescente')
#     else:
#         print('Crescente')
#     X, Y = input().split()
#     X = int(X)
#     Y = int(Y)



# Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". 
# Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002. 

# senha = 2002
# pin = int(input())
# while pin != senha:
#     print('Senha Invalida')
#     pin = int(input())
# print('Acesso Permitido')




# Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. 
# O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).


# X, Y = input().split()
# X = int(X)
# Y = int(Y)

# while X != 0 and Y != 0:
#     if X > 0 and Y > 0:
#         print('primeiro')
#     elif X < 0 and Y > 0:
#         print('segundo')
#     elif X < 0 and Y < 0:
#         print('terceiro')
#     else: 
#         print('quarto')
#     X, Y = input().split()
#     X = int(X)
#     Y = int(Y)




# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. 
# Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.


# nota1 = float(input())
# while nota1 < 0 or nota1 > 10:
#     print('nota invalida')
#     nota1 = float(input())

# nota2 = float(input())
# while nota2 < 0 or nota2 > 10:
#     print('nota invalida')
#     nota2 = float(input())
# print(f'media = {(nota1 + nota2) / 2}')


# Escreva um programa para ler as notas da primeira e a segunda avaliação de um aluno. Calcule e imprima a média semestral. 
# O programa só deverá aceitar notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

# No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, solicitando ao usuário que informe um código (1 ou 2) 
# indicando se ele deseja ou não executar o algoritmo novamente, (aceitar apenas os código 1 ou 2). 
# Se for informado o código 1 deve ser repetida a execução de todo o programa para permitir um novo cálculo, caso contrário o programa deve ser encerrado.

# resposta = 1
# while resposta == 1:
#     nota1 = float(input())
#     while nota1 < 0 or nota1 > 10:
#         print('nota invalida')
#         nota1 = float(input())

#     nota2 = float(input())
#     while nota2 < 0 or nota2 > 10:
#         print('nota invalida')
#         nota2 = float(input())
#     print(f'media = {(nota1 + nota2) / 2:.2f}')
#     resposta = int(input('novo calculo (1-sim 2-nao)\n'))
#     while resposta != 1 and resposta != 2:
#          resposta = int(input('novo calculo (1-sim 2-nao)\n'))


# Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão apresentadas na execução do programa, 
# seguindo a lógica do exemplo abaixo. Para valores com mais de 6 dígitos, todos os dígitos devem ser apresentados.

N = int(input())

for c in range(1, N+1):
    print(f'{c} {c**2} {c**3} ')
    print(f'{c} {(c**2) + 1} {(c**3) + 1}')
