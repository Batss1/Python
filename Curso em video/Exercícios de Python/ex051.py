print("""==============================
        CALCULO DE PA
==============================""")
firs = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = firs + (10 - 1) * razão
for c in range(firs, termo + razão, razão):
    print('{} '.format(c), end=' → ')
print('Acabou!')

