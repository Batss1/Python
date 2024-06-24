from random import randint

tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
# maior = max(tupla)
# menor = min(tupla) -- forma simples com função

maior = menor = tupla[0]
for c in tupla:
    if c > maior:
        maior = c
    if c < menor:
        menor = c

print('Os valores sorteados foram: ', end= '')
for c in tupla:
    print(f'{c} ', end='')
print(f'\nO maior valor sorteado foi {maior} \n ')
print(f'O menor valor sorteado foi {menor} \n ')