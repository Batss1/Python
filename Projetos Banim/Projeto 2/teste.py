
cont = 0
senha = ''

Tipo = input('Digite o tipo: ')
match Tipo:
    case 'a': 
        lista = [chr(i) for i in range(48,58)]
    case 'b':
        lista = [chr(i) for i in range(65,91)] 
        lista += [chr(c) for c in range(97,123)]
    case 'c':
        lista = [chr(i) for i in range(65,91)] 
        lista += [chr(i) for i in range(48,58)]
    case 'd':
        lista = [chr(i) for i in range(65,91)] 
        lista += [chr(c) for c in range(97,123)]
        lista += [chr(i) for i in range(48,58)]
    case 'e':
        lista = [chr(i) for i in range(65,91)] 
        lista += [chr(c) for c in range(97,123)]
        lista += [chr(i) for i in range(48,58)]
        lista += ["-", "_", ":", "@", "#", "$", "&", "?"]

print(lista)