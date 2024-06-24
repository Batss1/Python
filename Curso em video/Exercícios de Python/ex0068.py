from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*15)
valor = escolha = pontos = 0
acertou = True
pc = randint(0, 10)
while True:
    if acertou == False:
        break
    valor = int(input('Digite um valor: '))
    escolha = str(input('P/I? ')).upper().strip()
    print('-'*15)
    if (valor + pc) % 2 == 0:
        if escolha == 'P':
            pontos += 1
        elif escolha != 'P':
            acertou == False
    if (valor + pc) % 2 != 0:
        if escolha == 'I':
            pontos += 1
        elif escolha != 'I':
            acertou == False

Impar = (valor + pc) % 2 == 0
print(f'Você jogou o número {valor} e o computador {pc}. Total de {valor + pc} deu {}')