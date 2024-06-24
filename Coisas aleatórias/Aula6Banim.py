1. Escreva um programa que leia um número inteiro e em seguida apresente na tela a tabuada de 0 a 10
para esse número fornecido. Siga o formato apresentado abaixo (supondo que foi digitado 4):
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
...
4 x 10 = 40

# cont = 0
# num = int(input('Digite o número para calcular a tabuada: '))
# while cont < 11:
#     tabuada = num * cont
#     print(f'{num} x {cont} = {tabuada}')
#     cont +=1

2. Escreva um programa que apresente todos os valores inteiros divisíveis por 5 situados entre um valor
mínimo e um máximo, fornecidos pelo usuário. É obrigatório que o valor máximo seja maior que o
mínimo e se isso não ocorrer, deve ser dada uma mensagem de erro ao usuário.

# valor_min = int(input('Digite o valor minímo do intervalo: ')) + 1
# valor_maxi = int(input('Digite o valor máximo do intervalo: '))
# if valor_maxi <= valor_min:
#     print('ERRO... Os valores não correspondem à máximo e mínimo! ')
# a = valor_maxi
# while a < valor_maxi:
#     if a % 5 == 0:
#         print(a)
#     a += 1
    


3. Escreva um programa que leia um número inteiro N e em seguida leia N números reais, separando o
menor e o maior, apresentando-os na tela.

# N = int(input('Digite a quantidade de números: '))
# maior = menor = float(input('Digite um número: '))
# cont = 1
# while cont < N:
#     num = float(input('Digite um número: '))
#     if maior < num:
#         maior = num
#     if menor > num:
#         menor = num
#     cont += 1
# print(f'Menor número da lista: {menor}')
# print(f'Maior número da lista: {maior}')



4. Reescreva um programa do exercício acima considerando exclusivamente os números positivos
fornecidos. Caso seja digitado zero ou um valor negativo o programa deve exibir uma mensagem
"número inválido" e o valor deve ser ignorado.

# N = int(input('Digite a quantidade de números: '))
# maior = menor = None
# cont = 0
# while cont < N:
#     num = float(input('Digite um número: '))
#     if num <= 0:
#         print('Número inválido')
#     else:
#         if maior == None:
#             maior = menor = num
#         if maior < num:
#             maior = num
#         if menor > num:
#             menor = num
#     cont += 1
# if maior == None:
#     print('Número inválido')
# else:
#     print(f'Menor número da lista: {menor}')
#     print(f'Maior número da lista: {maior}')



5. Escreva um programa que contenha um laço que será executado enquanto o número digitado for
diferente de zero. Para cada número digitado pelo usuário mostrar na tela apenas os que forem divisíveis
por 2 e por 3.

# num = int(input('Digite um número: '))
# while num  != 0:
#     if num % 2 == 0 and num % 3 == 0:
#         print(f'{num} é divisível por 2 e 3')
#     num = int(input('Digite um número: '))

6. Elaborar um programa que apresente o somatório dos valores pares existentes na faixa entre 1 e N,
onde N é um número digitado pelo usuário e que deve ser no mínimo 100 (obrigatório garantir esse
requisito).

# N = int(input('Digite o último número para o período: '))
# cont = 2
# soma = 0
# while N < 100:
#     print('Valor inválido!')
#     N = int(input('Digite o último número para o período: '))
# while cont < N:
#     if cont % 2 == 0:
#         soma += cont
#     cont += 1
# print(f'A soma dos números pares entre os intervalos de 1 e {N} é igual a {soma}')



7. Elaborar um programa que efetue a leitura de valores positivos inteiros até que zero ou um valor
negativo seja informado. Ao final devem ser apresentados: o maior e menor valores informados pelo
usuário, a quantidade de valores, a soma e a média de todos.
soma = cont = 0

# maior = menor = num = int(input('Informe um número: '))
# while num != 0 and num > 0:
#     if  num > maior:
#         maior = num
#     if num < menor:
#         menor = num
#     cont += 1
#     soma += num
#     num = int(input('Informe um número: '))
# media = soma / cont

# print(f'O MAIOR valor informado foi {maior} e o MENOR {menor}')
# print(f'A quantidade de valores foi {cont} número(s)')
# print(f'A soma de todos os valores foi de {soma} e a média de {media}')


8. Desenvolva um programa que leia do teclado um número inteiro e mostre na tela se esse número é
primo ou não. Lembrando: um número primo é divisível somente por 1 e por ele mesmo.

# num = int(input('Digite um número: '))

# cont = 1
# tot = 0

# while cont < num +1:
#     if num % cont == 0:
#         tot +=1
#     cont += 1
# if tot == 2:
#     print(f'O número {num} é primo')
# else:
#     print(f'O número {num} não é primo')

resto = 1
num = int(input('Digite um número: '))
while num >= 2:
    if num == 2:
        resto = 1
    elif n % 2 == 0:
        resto = 0
    else:
        resto = 1
        raiz = 0.5 ** num
        i = 3
        while i <= raiz and resto != 0:
            resto = num % i
            i += 2
    if resto != 0:
        print(f'O número {num} é primo')
    else:
        print(f'O número {num} não é primo')
    num = int(input('Digite um número: '))
print('\nFim do programa')



9. Escreva um programa que leia um número inteiro N e em seguida apresente na tela os N primeiros
termos da sequência de Fibonacci. Essa sequência tem como regra de formação o fato de um número
ser a soma dos dois anteriores, sendo que os dois primeiros termos da sequência são, respectivamente,
0 e 1.
Caso de Teste: se N = 9 então a sequência é: 0, 1, 1, 2, 3, 5, 8, 13, 21

# N = int(input('Digite a quantidade de termos para a sequência de Fibonacci: '))
# cont = 2
# A = 0
# B = 1
# print(f'{A} {B}', end=' ')
# while cont < N:
#     C = A + B
#     A = B
#     B = C
#     print(f'{C}', end=' ')
#     cont += 1

10. Reescreva o programa anterior lendo um número inteiro adicional chamado Prim. Nesta versão o
programa deverá apresentar os N termos da sequência de Fibonacci que forem maiores que Prim.

# N = int(input('Digite a quantidade de termos para a sequência Fibonacci: '))
# Prim = int(input('Digite o número primário: '))

# cont = 2
# A = 0
# B = 1

# if A > Prim:
#     print(f'{A} {B}', end=' ')
# elif B > Prim:
#     print(f'{B}', end=' ')
#     cont -= 1
# if B < Prim:
#     cont -=2

# while cont < N:
#     C = A + B
#     A = B
#     B = C
#     if C > Prim:
#         print(f'{C}', end=' ')
#         cont += 1


# 11. Para todos os exercícios acima, faça com que a saída, além de ser exibida na tela, também seja gravada
# em um arquivo texto em disco.

