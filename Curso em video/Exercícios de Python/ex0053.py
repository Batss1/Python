frase = str(input('Dgite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Você digitou a frase {}\n '.format(junto))
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}\n'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase que foi digitada acima não é um palíndromo')

#inverso = junto[::-1]