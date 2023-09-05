while(True):
    num = int(input('\033[1;30mDigite um número inteiro: '))
    print("""\033[1;32mEscolha uma das bases conversão:
 [ 1 ] converter para BINARIO
 [ 2 ] converter para HEXADECIMAL
 [ 3 ] converter para OCTAL\033[m""")
    opção = int(input('\033[1;34mSua opção: {}, digite um dos números acima para converter sua opção '.format(num)))
    if opção == 1:
        print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
    elif opção == 2:
        print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
    elif opção == 3:
        print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
