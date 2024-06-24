salario = float(input('Qual o seu salário? R$: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Você ganhava {:.2f}\n Agora você irá começar a receber {:.2f} R$ agora'.format(salario, novo))