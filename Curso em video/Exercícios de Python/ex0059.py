from time import sleep
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print("""    [1] somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa)""")
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = (a + b)
        print(f'A soma entre {a} + {b} é {soma}')
    elif opção == 2:
        multiplicação = (a * b)
        print(f'A multiplicação entre {a} x {b} é {multiplicação}')
    elif opção == 3:
        if a > b:
            maior = a
        else:
            maior = b
        print(f'Entre {a} e {b} o maior valor é {maior}')
    elif opção == 4:
        print('Informe os números novamente:')
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando ...')
    else:
        print('Opção Inválida. Tente novamente.')
    print('=-=' * 10 )
    sleep(2)
print('Fim do programa, volte sempre!')
