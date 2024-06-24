casa = float(input('\033[1;34mValor da casa: '))
salario = float(input('\033[1;34mSalário do comprador: '))
anos = int(input('\033[1;34mQuanto anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('\033[1;33mPara pegar uma casa de R${:.2f} em {:.1f} anos \033[m'.format(casa, anos), end='')
print('\033[1;33mParaa prestação será de {:.2f}\033[m'.format(prestacao))
if prestacao <= minimo:
    print('\033[4;32mEmprestimo CONCEDIDO!')
else:
    print('\033[4;31mEmprestimo NEGADO!')
