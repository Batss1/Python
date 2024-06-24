from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a pessoa número {} nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo, nesta lista existem um total de {} pessoas maiores de idade\nE o total de {} pessoas menores de idade'.format(totmaior, totmenor))
