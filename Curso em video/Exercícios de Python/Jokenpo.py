from random import randint
while True:
    print('=====================PEDRA PAPEL E TESOURA=====================')
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''') 
    jogador = int(input('Qual é sua jogada? '))
    print('-=-' * 8)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=-' * 8)
    if computador == jogador:
        print('EMPATE!')
    elif computador == 1 and jogador == 2:
        print('VITÓRIA DO JOGADOR!')
    elif computador == 2 and jogador == 1:
        print('VITÓRIA DO COMPUTADOR!')
    elif computador == 0 and jogador == 2:
        print('VITÓRIA DO COMPUTADOR!')
    elif computador == 2 and jogador == 0:
        print('VITÓRIA DO JOGADOR!')
    elif computador == 0 and jogador == 1:
        print('VITÓRIA DO JOGADOR!')
    elif computador == 1 and jogador == 0:
        print('VITÓRIA DO COMPUTADOR!')