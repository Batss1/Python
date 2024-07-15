cadastros = []
while True:
    valor = input('Digite um valor: ')
    if valor in cadastros:
        print('Valor já existe')
    else:
        cadastros.append(valor)
        print('Valor adicionado com sucesso...')
    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar == 'N':
        break
    else:
        continue
print('-='* 15)
print(f'Os valores digitados foram: {cadastros}')