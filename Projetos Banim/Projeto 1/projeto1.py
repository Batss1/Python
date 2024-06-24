# leitura dos dados e armazenamento na lista dados
dados = []
arq = open('vendas.txt','r', encoding='utf-8')
s = arq.readline().rstrip()
while s != '':
    s = s.split(';')
    dados.append([int(s[0]), int(s[1]), float(s[2])])
    s = arq.readline().rstrip()
arq.close()


cont = 0
Soma = 0
codigo = int(input('Digite o código: '))
while codigo != 0:
    while cont < len(dados) and codigo in range(10000, 21001):
        if codigo == dados[cont][0]:
            Soma += dados[cont][1] * dados[cont][2]
        cont += 1
    if codigo not in range(10000, 21001):
        print(f'{codigo} Código inválido (Deve ser entre 10000 e 21000)')
    else:
        print(f'Total vendido do produto {codigo} = R$ {Soma:.2f}\n')
    codigo = int(input('Digite o código: '))
    cont = 0
    Soma = 0
print('Fim do programa')

