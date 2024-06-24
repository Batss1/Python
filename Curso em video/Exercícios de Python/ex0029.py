vel = float(input('Qual é a velocidade atual do seu carro? '))
if vel > 80:
    print('Você foi multado!, o limite maximo de velocidade é de 80Km/h!\n')
    multa = (vel - 80) * 7.00
    print('===========Você deve pagar uma multa de R${:.2f}!==========='.format(multa))
else:
    print('Tudo bem por aqui! Siga em frente sem ultrapassar o limite de velocidade de 80Km/h!')
