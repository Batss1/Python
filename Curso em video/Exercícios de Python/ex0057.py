gen = str(input('Informe seu sexo(F/M): ')).upper().strip()[0]
while gen not in 'FfMm':
    gen = str(input('Dados inválidos. Digite novamente seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(gen))
