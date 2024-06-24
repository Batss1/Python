n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}\n'.format(nome[0]))
print('Seu ultimo nome é {}\n'.format(nome[len(nome)-1]))
