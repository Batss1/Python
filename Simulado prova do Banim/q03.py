print("Gabriel Batista Rodrigues")
print("Pedro Rodrigues Ferreira")
print("Questão 3") 


tupla = (16,23,27,34)
NV = int(input('Digite o número de vendas: '))
while NV < 0:
    NV = int(input('Digite o número de vendas: '))
precoVarejo = precoAtacado = 0

for c in range(NV):
    print(f'Venda {c+1}')
    Cod = int(input(f'Digite o Código do produto: '))
    while Cod not in tupla:
        print('Código inválido')
        Cod = int(input(f'Digite o Código do produto: '))
    QV = int(input(f'Digite a quantidade da venda do produto: '))
    if Cod == 16:
        if QV < 50:
            precoVarejo += QV * 14.35
            print(precoVarejo)
        else:
            precoAtacado += QV * 12.93
            print(precoAtacado)
    elif Cod == 23:
        if QV < 100:
            precoVarejo += QV * 35.12
            print(precoVarejo)
        else:
            precoAtacado += QV * 29.85
            print(precoAtacado)
    elif Cod == 27:
        if QV < 70:
            precoVarejo += QV * 19.35
            print(precoVarejo)
        else:
            precoAtacado += QV * 16.76
            print(precoAtacado)
    elif Cod == 34:
        if QV < 40:
            precoVarejo += QV * 63.40
            print(precoVarejo)
        else:
            precoAtacado += QV * 58.25
            print(precoAtacado)


print(f'Total de Vendas do Grupo Varejo: {precoVarejo:.2f}')
print(f'Total de Vendas do Grupo Atacado: {precoAtacado:.2f}\n')
print(f'Vendas Totais: R$ {precoAtacado + precoVarejo}')
