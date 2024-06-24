from time import sleep

n = int(input('Digite um numero inteiro: '))
print('PROCESSANDO...')
sleep(2)
if 2 * int(n / 2) == n:
    print('Esse numero é par!')
else:
    print('Esse número é ímpar!')
