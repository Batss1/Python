from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU IMPAR')
acertou = True
pontos = 0
while True:
    pc = randint(0, 10)
    valor = escolha = 0
    if acertou == False:
        break
    print('-='*15)
    valor = int(input('Digite um valor: '))
    while escolha not in ('PI'):
        escolha = str(input('P/I? ')).upper().strip()[0]
        print('-'*15)
        print(f'Você jogou o número {valor} e o computador {pc}. Total de {valor + pc}', end='')
        print('deu PAR' if (valor + pc) % 2 == 0 else 'deu IMPAR')
        if (valor + pc) % 2 == 0:
            if escolha == 'P':
                pontos += 1
                print('VOCÊ GANHOU')
                print('Vamos jogar novamente')
            elif escolha != 'P':
                acertou = False
                print('VOCÊ PERDEU')   
        if (valor + pc) % 2 != 0:
            if escolha == 'I':
                pontos += 1
                print('VOCÊ GANHOU')
                print('Vamos jogar novamente')
            elif escolha != 'I':
                acertou = False
print('-'*15)
print(f'Game over. Você venceu {pontos} vezes')