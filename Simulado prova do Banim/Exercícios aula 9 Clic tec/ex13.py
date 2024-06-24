# 13. Escreva um programa que leia um número inteiro N. Em seguida calcule e armazene em uma lista os N primeiros
# números primos. Exibir a lista no final. Ex. se N fornecido pelo usuário for 10, então a lista será carregada com:

N = int(input("Digite um número inteiro N para calcular os N primeiros números primos: "))
primos = []
numero = 2  # Começando a busca por primos a partir do número 2
while len(primos) < N:
    controle = True
    if numero < 2:
        controle = False
    else: 
        # Verificar divisibilidade por todos os números de 2 até a raiz quadrada do número
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                controle = False  # Se for divisível por algum número, não é primo
                break  # Saia do loop assim que encontrar um divisor
    if controle:
        primos.append(numero)
    numero += 1

print(primos)