# num = int(input('Escreva um número: '))
# if num > 0:
#     print(f'Número apresentado é positivo, ({num})')
# elif num < 0:
#     print(f'Número apresentado é negativo, ({num})')
# else:
#     print('Número apresentado é igual a zero')


# nomeLutador = input('Digite seu nome: ')
# peso = float(input('Digite seu peso: '))
# if peso < 65:
#     print(f'O lutador {nomeLutador} pesa {peso} kg e se enquadra na categoria Pena')
# elif 65 <= peso < 72:
#     print(f'O lutador {nomeLutador} pesa {peso} kg e se enquadra na categoria Leve')
# elif 72 <= peso < 79:
#     print(f'O lutador {nomeLutador} pesa {peso} kg e se enquadra na categoria Ligeiro')
# elif 79 <= peso < 86:
#     print(f'O lutador {nomeLutador} pesa {peso} kg e se enquadra na categoria Meio médio')
# elif 86 <= peso < 93:
#     print(f'O lutador {nomeLutador} pesa {peso} kg e se enquadra na categoria Médio')
# elif 93 <= peso < 100:
#     print(f'O lutador {nomeLutador} pesa {peso} kg e se enquadra na categoria Meio pesado')
# else:
#     print(f'O lutador {nomeLutador} pesa {peso} kg e se enquadra na categoria Pesado')




# A = float(input('Digite um número: '))
# B = float(input('Digite outro número: '))
# C = float(input('Digite mais um número: '))

# delta = (B**2) -4 * A * C

# if delta > 0:
#     r1 = (-B + (delta ** 0.5)) / (2 * A)
#     r2 = (-B - (delta ** 0.5)) / (2 * A)
#     print(f'As raízes reais para a equação são r1 = {r1}, r2 = {r2}')
# elif delta < 0:
#     print('Não existe raízes reais para delta menor que Zero')
# else:
#     r1 = r2 = (-B + (delta ** 0.5)) / (2 * A)
#     print(f'As raízes reais para a equação são iguais por seu Delta ser igual a zero, r1 = {r1} r2 = {r2}')




# a = float(input('Digite um valor: '))
# b = float(input('Digite outro valor: '))
# c = float(input('Digite outro valor: '))
# if a and b and c > 0:
#     print('Valor inválido! Não é possivel formar um lado do triangulo com valores negativos e 0')
# else:
#     if (a + b > c) and (b + c > a) and (a + c > b):
#         print('Os valores apresentados formam um Triangulo')
#         if a == b or b == c or a == c:
#             print('Isósceles')
#         elif a == b == c:
#             print('Equilatero')
#         else:
#             print('Escaleno')
#     else:
#         print('Os valores apresentados NÃO formam um Triangulo')


# valor = int(input())
# cedula = 100
# cont_cedulas = 0
# print(valor)
# while valor != 0:
#     if valor >= cedula:
#         valor -= cedula
#         cont_cedulas += 1
#     else:
#         print(f'{cont_cedulas} nota(s) de R${cedula},00')
#         if cedula == 100:
#             cedula = 50
#         elif cedula == 50:
#             cedula = 20
#         elif cedula == 20:
#             cedula = 10
#         elif cedula == 10:
#             cedula = 5
#         elif cedula == 5:
#             cedula = 2
#         elif cedula == 2:
#             cedula = 1
#         cont_cedulas = 0
# print(f'{cont_cedulas} nota(s) de R${cedula},00')
# if cedula == 2 and valor == 0:
#     print(f'{valor} nota(s) de R$1,00')

resto = 1
num = int(input('Digite um número: '))
while num >= 2:
    if num == 2:
        resto = 1
    elif num % 2 == 0:
        resto = 0
    else:
        resto = 1
        raiz = num ** 0.5
        i = 3
        while i <= raiz and resto != 0:
            resto = num % i
            i += 2
    if resto != 0:
        print(f'O número {num} é primo')
    else:
        print(f'O número {num} não é primo')
    num = int(input('Digite um número: '))
print('\nFim do programa')