somaidade = 0
mulhernum = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
for c in range(1, 5):
    print('--------{}ª PESSOA--------'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    gen = str(input('Gênero [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and gen in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if gen in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if idade < 20 and gen in 'Ff':
        mulhernum += 1


médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Existem {} mulheres com menos de 20 anos no grupo.'.format(mulhernum))