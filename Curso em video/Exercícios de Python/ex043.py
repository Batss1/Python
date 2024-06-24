print('---' * 10)
peso = float(input('\033[1;35mQual é seu peso? (KG) '))
altura = float(input('\033[1;35mQual sua altura? (M) '))
print('---' * 10)
imc = peso / (altura ** 2)
print('\033[1;34mO IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[1;30mVocê está ABAIXO DO PESO NORMAL!')
elif imc < 18.5:
    print('\033[1;32mVocê está na faixa de PESO NORMAL')
elif 18.5 <= imc < 25:
    print('\033[1;33mVocê está em SOBREPESO!')
elif 30 <= imc < 40:
    print('\033[1;31mVocê está em OBESIDADE!')
elif imc >= 40:
    print('\033[1;31mVocê está em OBESIDADE MÓRBIDA!')