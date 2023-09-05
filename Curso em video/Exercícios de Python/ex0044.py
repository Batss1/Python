print('{:=^40}'.format(' ARMARINHOS FERNANDO '))
preço = float(input('\033[1;31mPreço das compras: R$ '))
print("""\033[1;33mFORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque (com 10% de desconto) 
[ 2 ] á vista no cartão (com 5% de desconto) 
[ 3 ] 2x no cartão (sem juros)
[ 4 ] 3x ou mais no cartão (com 20% de juros)\033[m""")
opção = int(input('\033[1;34mQual sua forma de pagamento? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparcela = int(input('Quantas parcelas? '))
    parcela = total / totalparcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparcela, parcela))
print('Sua compra de {:.2f} vai custar {:.2f}R$ no final'.format(preço, total))
        
