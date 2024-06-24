# Leia dois números inteiros LMin e LMax. Em seguida leia 10 valores inteiros e inserindo-os em uma lista A somente
# se o valor fornecido estiver no intervalo [LMin, LMax]. Valores fora deste intervalo devem ser ignorados. Ao final,
# apresentar a lista A e seu tamanho efetivo. Observe que para este programa funcionar apropriadamente é
# necessário que LMin seja menor que LMax. Caso o usuário digite LMax menor que LMin, o programa deve inverter
# os valores. Colocar este programa no site do professor


LMin = int(input('Digite o valor de LMin: '))
LMax = int(input('Digite o valor de LMax: '))

if LMin > LMax:
    LMin, LMax = LMax, LMin
    
A = []
contExcluidos = 0
for c in range(10):
    num = int(input('Digite um número: '))
    if num >= LMin and num <= LMax:
        A.append(num)
    else:
        contExcluidos += 1
print(A)
print(f'O tamanho da lista efetiva é: {10 - contExcluidos}')