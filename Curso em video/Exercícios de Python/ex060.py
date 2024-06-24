from math import factorial
num = int(input('Digite um número para calcular o seu fatorial: '))
c = num
f = factorial(num)
print(f'Calculando {num}! : ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ' , end='')
    c -= 1
print(f'{f}')

