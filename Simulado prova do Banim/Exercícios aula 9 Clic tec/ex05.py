# Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50 – o programa deve garantir isso em
# um laço) e em seguida leia N números reais em uma lista A. O programa deve separar os valores lidos em A em
# outras duas listas NEG e POS, a primeira contendo somente os valores negativos e a segunda contendo os valores
# positivos e zero. Apresentar na tela as listas NEG e POS e a quantidade de valores contidos em cada uma. Colocar
# este programa no site do professor.

N = int(input('Digite um número entre 0 e 50: '))
while N < 0 and N > 50:
    N = int(input('Digite um número entre 0 e 50: '))
    
cont = 0
A = []
while cont < N:
    num = float(input(f'Digite o {cont+1}º número: '))
    cont += 1
    A.append(num)

contNeg = 0
contPos = 0
NEG = []
POS = []
for c in A:
    if c < 0:
        NEG.append(c)
        contNeg += 1
    else:
        POS.append(c)
        contPos += 1

print(f'A lista NEG é: {NEG}, existe {contNeg} elementos na lista')
print(f'A lista POS é: {POS}, existe {contPos} elementos na lista')