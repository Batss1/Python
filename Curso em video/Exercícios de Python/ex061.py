print("""==============================
        CALCULO DE PA
==============================""")
prime = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = prime
vezes = 1
while vezes <= 10:
    print(f'{termo} ', end=' → ')
    termo += razao
    vezes += 1
print('FIM', end='')