cont = soma = 0
print('Escreva valores. Se deseja parar digite 999')
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A quantidade de números digitados foi de {cont}')
print(f'A soma dos números digitados foi de {soma}')
    