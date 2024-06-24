print('-' * 30)
print('SUPER BARATÃO')
print('-' * 30)
maior_1000 = total = cont = menor = 0
nome_menor = ' '
while True:
    continuar = ' '
    produto = str(input('Nome do produto: '))
    valor = float(input('Valor do produto '))
    cont += 1
    if valor >= 1000:
        maior_1000 += 1
    total += valor
    if menor > valor or cont == 1:
        menor = valor
        nome_menor = produto
    while continuar not in 'SN':
        continuar = str(input('Quer continuar[S/N]:  ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-' * 30, 'FIM DO PROGRAMA', '-' * 30)
print(f'O total da compra foi de {total:.2f}')
print(f'Temos {maior_1000} produtos que custam mais que R$1000')
print(f'O produto mais barato é o {nome_menor} custando R${menor}')