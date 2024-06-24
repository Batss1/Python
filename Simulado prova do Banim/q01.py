print("Gabriel Batista Rodrigues")
print("Pedro Rodrigues Ferreira")
print("Questão 1")
 
from random import randint
palpites = []
nmin = int(input('Digite um número mínimo: '))
nmax = int(input('Digite um número máximo: '))

while nmax < nmin + 100:
    print('Digite valores válidos')
    nmin = int(input('Digite um número mínimo: '))
    nmax = int(input('Digite um número máximo: '))

sorteado = randint(nmin, nmax)
contador = 1
X = int(input(f'Palpite {contador}º: '))
palpites.append(X)
if X == sorteado:
    print("Parabéns! Você acertou de cara!")
    palpites.append(X)
else:
    while X != sorteado:
        if X < nmin or X > nmax:
            print("Número inválido! fora do intervalo")
            X = int(input(f'Palpite {contador}º: '))
        else:
            if X > sorteado:
                print("Seu número é maior do que o sorteado")
                palpites.append(X)
                contador += 1
                X = int(input(f'Palpite {contador}º: '))
            else:
                print("Seu número é menor que o sorteado")
                palpites.append(X)
                contador += 1
                X = int(input(f'Palpite {contador}º: '))

if len(palpites) > 1:
    palpites.append(X)
    print("Parabéns! Você acertou!")
print(f"Você realizou {len(palpites)} palpite(s) \nSeu(s) palpite(s) = {palpite}")


