print("\nGerador de Senhas")
print("\nPor:\nCaio Luiz Argentino Firmino")
print("Felipe Carvalho de Brito")
print("Gabriel Batista Rodrigues")
print("Pedro Côrtes Loureiro\n------------------------")

AliqINSS = (0.08, 0.09, 0.11, 642.34) # valores aliquota INSS
AliqIR = (0.00, 0.075, 0.15, 0.225, 0.275) # valores aliquota IR
DeducaoIR = (0.00, 142.80, 354.80, 636.13, 869.36) # valores dedução IR

# leitura do arquivo SALARIO.TXT de entrada
SalBrutos = []
arqsal = open('SALARIO.TXT', 'r', encoding='UTF-8')
leitura = 0

# adicionamos um tratamento de excecoes pois ficamos em dúvida
# se o arquivo de teste 1, que possuia uma primeira linha "Bruto\n",
# poderia ser o caso de um arquivo com inclusao impropria de salarios
while leitura != '':
    leitura = arqsal.readline()
    try:
        SalBrutos.append(float(leitura))
    except ValueError:
        continue

arqsal.close()
SalBrutos.sort()

# Calcula aliquota INSS
def Calculo_INSS(a):
    ValINSS = 0
    if a <= 1751.81:
        ValINSS = (a * AliqINSS[0])
        INSS = AliqINSS[0]
    elif a > 1751.81 and a <= 2919.72:
        ValINSS = (a * AliqINSS[1])
        INSS = AliqINSS[1]
    elif a > 2919.72 and a <= 5839.45:
        ValINSS = (a * AliqINSS[2])
        INSS = AliqINSS[2]
    else:
        ValINSS = AliqINSS[3]
        INSS = 0.00
    return ValINSS, INSS


# Calcula aliquota IR
def Calculo_IR(a):
    BaseIR = a - ValINSS
    if BaseIR <= 1903.98:
        ValIR = BaseIR * AliqIR[0] - DeducaoIR[0]
        IR = AliqIR[0]
    elif BaseIR <= 2826.95:
        ValIR = BaseIR * AliqIR[1] - DeducaoIR[1]
        IR = AliqIR[1]
    elif BaseIR <= 3751.05:
        ValIR = BaseIR * AliqIR[2] - DeducaoIR[2]
        IR = AliqIR[2]
    elif BaseIR <= 4664.68:
        ValIR = BaseIR * AliqIR[3] - DeducaoIR[3]
        IR = AliqIR[3]
    else:
        ValIR = BaseIR * AliqIR[4] - DeducaoIR[4]
        IR = AliqIR[4]
    if ValIR < 10.00:
        ValIR = 0.00
    return ValIR, BaseIR, IR

# Cria CALCULOS.TXT e escreve os titulos da Tabela
saida = open('CALCULOS.TXT', 'w', encoding= 'Utf-8')
saida.write(f"{('Bruto'):>15} {('AliqINSS'):>15} {('Val.INSS'):>15} {('Base I.R.'):>15} {('AliqIR'):>15} {('Val.IR'):>15} {('Liquido'):>15} \n")

# Para cada salário, escreve os valores abaixo dos títulos
for salarios in SalBrutos:
    ValINSS, INSS = Calculo_INSS(salarios)
    ValIR, BaseIR, IR = Calculo_IR(salarios)
    SalLiquido = salarios - ValINSS - ValIR
    saida.write(f'{salarios:>15.2f} {INSS*100:>15} {ValINSS:>15.2f} {BaseIR:>15.2f} {IR*100:>15.1f} {ValIR:>15.2f} {SalLiquido:>15.2f}\n')
# Fecha o .txt 
saida.close()


print('\nArquivo CALCULOS.TXT gerado com sucesso.\nFim da execução.')


