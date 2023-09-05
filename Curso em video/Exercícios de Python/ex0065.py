resp = 'S'
quantidade = soma = média = maior = menor = 0
while resp in 'Ss':
    número = int(input('Digite um número: '))
    quantidade += 1
    soma += número
    if quantidade == 1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quantidade
print(f'Você digitou {quantidade} números e a  média dos valores é {média}')
print(f'O menor número entre eles é {menor} e o maior número é {maior}')
print('Acabou')



