frase = str(input('Digite seu nome:')).strip()
print('Seu nome em letras maiusculas é: {}\n'.format(frase.upper()))
print('Seu nome em letras maiusculas é: {}\n'.format(frase.lower()))
print('Seu nome tem {} letras\n'.format(len(frase)-frase.count(' ')))
print('Seu primeiro nome tem {} letras\n'.format(frase.find(' ')))

