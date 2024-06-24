1. Escreva um programa que calcule os N primeiros termos de uma progressão geométrica (PG) com razão
R e primeiro termo P fornecidos pelo usuário. Também deve ser calculada e apresentada a soma desses
N termos. Caso de teste:
Entrada: N = 8 P = 2 e R = 3
Saída: 2 6 18 54 162 486 1458 4374

# n = int(input('Digite o numero de termos da PG: '))
# p = int(input('Digite o primeiro termo: '))
# r = int(input('Digite a razão: '))
# cont = 1
# while cont <= n:
#     print(p)
#     p *= r
#     cont += 1



 
 # num = float(input())
 # if 0 <= num <= 25:
 #     print('Intervalo [0,25]')
 # elif 25 < num <= 50:
 #     print('Intervalo (25,50]')
 # elif 50 < num <= 75:
 #     print('Intervalo [50,75]')
 # elif 75 < num <= 100:
 #     print('Intervalo (75,100]')
 # else:
 #     print('Fora do intervalo')

# salario = float(input())
# reajuste = 0
# if  0 < salario <= 400.00:
#     reajuste = salario * 0.15
#     salario = salario * 1.15
#     print(f'Novo salario: {salario:.2f}')
#     print(f'Reajuste ganho: {reajuste:.2f}')
#     print('Em percentual: 15 %')
# elif  400.00 < salario <= 800.00:
#     reajuste = salario * 0.12
#     salario = salario * 1.12
#     print(f'Novo salario: {salario:.2f}')
#     print(f'Reajuste ganho: {reajuste:.2f}')
#     print('Em percentual: 12 %')
# elif  800.00 < salario <= 1200.00:
#     reajuste = salario * 0.10
#     salario = salario * 1.10
#     print(f'Novo salario: {salario:.2f}')
#     print(f'Reajuste ganho: {reajuste:.2f}')
#     print('Em percentual: 10 %')
# elif  1200.00 < salario <= 2000.00:
#     reajuste = salario * 0.07
#     salario = salario * 1.07
#     print(f'Novo salario: {salario:.2f}')
#     print(f'Reajuste ganho: {reajuste:.2f}')
#     print('Em percentual: 7 %')
# else:
#     reajuste = salario * 0.04
#     salario = salario * 1.04
#     print(f'Novo salario: {salario:.2f}')
#     print(f'Reajuste ganho: {reajuste:.2f}')
#     print('Em percentual: 4 %')


#     for c in range(2,102,2):
#     print(c)
# X = int(input())
# Y = int(input())
# somaImpar = 0
# if X < Y:
#     for c in range(X,Y):
#         if c % 2 != 0:
#             somaImpar += c
# else:
#     for c in range (Y,X):
#         if c % 2 != 0:
#             somaImpar += c

# print(somaImpar)


# N = int(input())
# coelhos = ratos = sapos = 0
# cont = 1
# while cont <= N:
#     cobaias = input().split()
#     if 'C' in cobaias:
#         cobaias = int(cobaias[0])
#         coelhos += cobaias
#     elif 'R' in cobaias:
#         cobaias = int(cobaias[0])
#         ratos += cobaias
#     elif 'S' in cobaias:
#         cobaias = int(cobaias[0])
#         sapos += cobaias
#     cont += 1
# total = coelhos + sapos + ratos
# print(f'Total: {total} cobaias')
# print(f'Total de coelhos: {coelhos}')
# print(f'Total de ratos: {ratos}')
# print(f'Total de sapos: {sapos}')
# print(f'Percentual de coelhos: {coelhos / total * 100:.2f} %')
# print(f'Percentual de ratos: {ratos / total * 100:.2f} %')
# print(f'Percentual de sapos: {sapos / total * 100:.2f} %')







# x = 1
# somaPositiva = somaNegativa = 0
# while x != 0:
#     x = int(input('Digite um número: '))
#     if x > 0:
#         somaPositiva += x
#     else:
#         somaNegativa += x
# print(f'Total dos positivos: {somaPositiva}')
# print(f'Total dos negativos: {somaNegativa}')]

# cont = 1
# n = int(input('Digite a quantidade de números: '))
# soma = 0
# while cont <= n:
#     num = float(input(f'Digite o {cont} º valor: '))
#     if num > 0:
#         soma += num
#     cont += 1
# print(f'A soma dos valores fornecidos foi: {soma}')