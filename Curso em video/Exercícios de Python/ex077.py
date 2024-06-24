palavras = ('Aprender', 'Programar', 'linguagem', 'Curso', 'Python', 'Gratis')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ',end='')
    for vogais in p:
        if vogais.upper() in 'AEIOU':
            print(f'{vogais.upper()}',end=' ')