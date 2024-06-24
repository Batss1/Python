import random

saida = open('SALARIO.TXT','w', encoding='utf-8')
for _ in range(1000):
    saida.write(f'{random.uniform(1640.00, 9000.00):.2f}\n')

saida.close()
print('\nSalários criados com sucesso\n')