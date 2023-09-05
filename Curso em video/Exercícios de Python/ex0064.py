soma = num = vezes = 0
num = int(input('Digite um número[999 para parar]: '))
while num != 999: 
    soma += num 
    vezes += 1
    num = int(input('Digite um número[999 para parar]: '))
print(f'Você digitou {vezes} números e a soma entre eles foi {soma}')