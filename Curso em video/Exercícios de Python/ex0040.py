n1 = float(input('\033[1;30mQual foi sua primeira nota? '))
n2 = float(input('\033[1;30mE a segunda nota? '))
n3 = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média é {:.1f}'. format(n1, n2, n3))
print('-' * 20)
if n3 < 5:
    print('\033[1;31mREPROVADO!\033[m')
    print('\033[1;30m-' * 20)
elif 7 > n3 >= 5:
    print('\033[1;33mVocê está de recuperação!\033[m')
    print('\033[1;30m-' * 20)
elif n3 >= 7.0:
    print('\033[1;32mVocê foi aprovado!\033[m')
    print('\033[1;30m-' * 20)
