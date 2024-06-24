print('-' * 30, 'CAIXA ELETRÔNICO','-' * 30)
saque = int(input('Qual o valor será sacado?'))
cedula = 50
contador_cedulas = 0
while True:
    if saque >= cedula:
        saque -= cedula
        contador_cedulas += 1
    else:
        if contador_cedulas > 0:
            print(f'Total de {contador_cedulas} cédulas de {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contador_cedulas = 0
print('Volte sempre ao Banco Inter! Tenha uma boa tarde!')