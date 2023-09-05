from random import randint

pc = randint(0, 10)
print('''Sou seu COMPUTADOR...
Acabei de pensar em um número entre 0 e 10
Será que você consegue adivinhar qual foi?''')
tenta = 0
acertou = False

while not acertou:
    palpite = int(input('Qual é seu palpite? '))
    tenta += 1
    if palpite == pc:
        acertou = True
    else:
        if palpite > pc:
            print('Menor, tente novamente: ')
        elif palpite < pc:
            print('Maior, tente novamente: ')

print('Parabéns você ACERTOU o número que pensei na {} tentativa!!!'.format(tenta))
