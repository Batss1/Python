a = int(input('\033[1;30mDigite o primeiro valor: '))
b = int(input('\033[1;30mDigite o segundo valor: '))
print('-' * 40)
if a > b:
    print('\033[1;33mO primeiro valor é maior que o segundo!')
elif b > a:
    print('\033[1;33mO segundo valor é maior que o primeiro')
elif a == b:
    print('\033[1;33mOs dois valores são iguais')
