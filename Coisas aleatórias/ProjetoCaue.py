resposta = input('Digite 0 para ler as instruções ou qualquer outra coisa para seguir sem ler: ')
if resposta == '0':
    print('\nEste programa avalia a validade de uma conclusão a partir de N premissas,'
          'sendo que todas as premissas são do tipo "Se... Então...". \n'
          'Para o programa funcionar, você deve digitar as premissas iguais exatamente do mesmo jeito. \n'
          'Por exemplo: "Se uma pessoa é feliz" não será considerada a mesma premissa que "Se a pessoa'
          ' é feliz", pois elas não estão escritas de maneira idêntica. \nPreste atenção também nos acentos e'
          ' letras maiúsculas e minúsculas.\n\n'
          'É recomendado escrever sem acentos e no máximo uma palavra por premissa, se preferir uma só letra.\n'
          'Exemplo: "Se matematica, então inteligente". "Se M, então I". Etc.\n\n'
          'Negações: usar "nao ", sem acento, só minúsculas, com espaço depois de "nao". Só assim o '
          'programa irá reconhecer a premissa como a negação de outra.\n'
          'Exemplo: "nao feliz" é a negação de "feliz". "Não feliz" NÃO é a negação de "feliz"!\n')

correto = False
while not correto:
    n = input('Digite quantas premissas: ')
    try:
        n = int(n)
        if n > 1:
            correto = True
        else:
            print('A quantidade deve ser um número natural maior que 1')
    except:
        print('A quantidade deve ser um número natural maior que 1')

argumentos = []
for i in range(n):
    valor = input(f'Premissa {i+1}, parte 1. Se : ')
    argumentos.append([valor, i, 'se', ''])
    valor = input(f'Premissa {i + 1}, parte 2. Então : ')
    argumentos.append([valor, i, 'então', ''])

valor = input(f'Conclusão, parte 1. Se: ')
argumentos.append([valor, n, 'se', 'verdade'])
valor = input(f'Conclusão, parte 2. Então: ')
argumentos.append([valor, n, 'então', ''])

validade = ''
mudanca = False
while validade == '':
    for argumento in argumentos:
        if argumento[3] != '':
            if argumento[0] == argumentos[-1][0]:
                if argumento[3] == 'verdade':
                    validade = 'A conclusão é válida'
                else:
                    validade = 'A conclusão é uma falácia (contradição)'
                mudanca = True
            else:
                for argumento_2 in argumentos:
                    if argumento_2[3] == '':
                        if argumento_2[0] == argumento[0]:
                            argumento_2[3] = argumento[3]
                            mudanca = True
                        elif ((argumento_2[0] == f'nao {argumento[0]}') or
                            (argumento[0][:4] == 'nao ' and argumento[0][4:] == argumento_2[0])):
                            if argumento[3] == 'verdade':
                                argumento_2[3] = 'falso'
                            else:
                                argumento_2[3] = 'verdade'
                            mudanca = True
                        elif (argumento[2] == 'então' and argumento[3] == 'falso'
                              and argumento[1] == argumento_2[1]):
                            argumento_2[3] = 'falso'
                            mudanca = True
                        elif (argumento[2] == 'se' and argumento[3] == 'verdade'
                              and argumento[1] == argumento_2[1]) and argumento[1] != n:
                            argumento_2[3] = 'verdade'
                            mudanca = True

    if not mudanca:
        validade = 'A conclusão é uma falácia (contingência)'
    else:
        mudanca = False

print(validade)