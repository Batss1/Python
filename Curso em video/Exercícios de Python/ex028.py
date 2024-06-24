from random import randint
from time import sleep

pc = randint(0, 5)  # Numero que vai ser escolhido
print('\033[1;42;36m------------------JOGO DA ADIVINHAÇÃO------------------\033[m\n')
print('-=-' * 19)
print('\033[1;34mTente adivinhar um número que eu vou pensar entre 0 e 5.\033[m')
print('-=-' * 19)
jogador = int(input('\033[30mEm que número eu pensei?\033[m '))  # Número do jogador
print('\033[4;36mPROCESSANDO SEU NÚMERO...\033[m\n')
sleep(2)
if jogador == pc:
    print('\033[1;32mVocê acertou o número!\n')
    print('-' * 10)
    print('VITÓRIA!!')
    print('-' * 10)
else:
    print('\033[1;31mVocê errou o número!\n')
    print('-' * 8)
    print('Derrota')
    print('-' * 8)
    print('Tente outra vez!')
