num = (int(input('Digite um número: ')), 
int(input('Digite outro número: ')), 
int(input('Digite mais um número: ')), 
int(input('Digite o último número: ')))

par = 0
for c in num:
    if c % 2 == 0:
        par +=1
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} veze(s)')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('Não existe o valor 3 na tupla')
print(f'Os valores pares digitados fora {par}')