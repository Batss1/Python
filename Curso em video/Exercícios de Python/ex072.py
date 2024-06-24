numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze',
'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
N = int(input('Digite um número entre 0 e 20: '))
while not 0 <= N <= 20:
    N = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[N]}')