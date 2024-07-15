num = []
for c in range(5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-='*15)
pos_maior = [0]
pos_menor = [0]
maior = menor = num[0]
for c in range(1, len(num)):
    if num[c] > maior:
        maior = num[c]
        pos_maior = [c]
    elif num[c] == maior:
        pos_maior.append(c)
    if num[c] < menor:
        menor = num[c]
        pos_menor = [c]
    elif num[c] == menor:
        pos_menor.append(c)
    
print(f'Lista: {num}\n')
print(f'Menor número: {menor} nas posições  {pos_menor}\n')
print(f'Maior número: {maior}, nas posições {pos_maior}')