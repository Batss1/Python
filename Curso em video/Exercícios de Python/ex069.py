num_mulheres20 = num_homens = idade18 = 0
while True:
    continuar = sexo = ' '
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade >= 18:
        idade18 += 1 
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]:')).upper().strip()[0]
        if sexo == 'M':
            num_homens += 1
        if sexo == 'F' and idade < 20:
            num_mulheres20 += 1
        print('-' * 30)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar[S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O número de pessoas com mais de 18 anos é {idade18}')
print(f'O número de homens é {num_homens}')
print(f'O número de mulheres com menos de 20 anos é de {num_mulheres20}')