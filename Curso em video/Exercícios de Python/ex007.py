#n1 = float(input('Priemira nota:'))
#n2 = float(input('Segunda nota:'))
#n4 = (n1 + n2) / 2
#print('A média entre \033[1;30m{}\033[m e \033[1;30m{}\033[m é igual a \033[33m{}\033[m'.format(n1, n2, n3))


n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
n3 = float(input('Terceira nota:'))
n4 = (n1 + n2+ n3) / 3
print('A média trimestral do aluno foi de {}'.format(round(n4)))
if n4 >=6:
    print('O aluno foi aprovado')
else:
    print('O aluno foi reprovado')