# Meu script
nivel = input('Digite nível de acesso: ').upper()
if nivel == "ADM":
    genero = input('Digite seu gênero: ')
    if genero == "FEMININO":
        print('Olá administradora!')
    else:
        print('Olá administrador!')
elif nivel == "USR":
    genero = input('Digite seu gênero: ')
    if genero == "FEMININO":
        print('Olá usuária!')
    else:
        print('Olá usuário!')
elif nivel == "GUEST":
    print('Olá visitante!')
else:
    print('Olá Desconhecido!')


# O script da FIAP
nivel=input("Digite o nível de acesso: ").upper()
if nivel=="ADM" or nivel=="USR":
    genero=input("Digite o seu gênero: ").upper()
    if nivel=="ADM":
        if genero=="FEMININO":
            print("Olá administradora")
        else:
            print("Olá administrador")
    else:
        if genero=="FEMININO":
            print("Olá usuária")
        else:
            print("Olá usuário")
elif nivel=="GUEST":
    print("Olá visitante")
else:
    print("Olá desconhecido(a)")