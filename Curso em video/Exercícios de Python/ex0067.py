valor = 0
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if valor < 0:
        break
    for c in range (1, 11):
        print(f'{valor} x {c} = {valor * c}')
    print('-'*30)
print('TABUADA ENCERRADA, VOLTE SEMPRE!!')
