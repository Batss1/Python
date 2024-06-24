print("""==============================
        CALCULO DE PA
==============================""")
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
adicional = 10
while adicional != 0:
    total = total + adicional
    while cont <= total:
        print(f'{termo} ', end=' → ')
        termo += razao
        cont += 1
    print('PAUSA')
    adicional = int(input('Quantos termos você quer mostrar a mais: '))
print(f'Progressão finalizada com {cont} termos mostrados')



