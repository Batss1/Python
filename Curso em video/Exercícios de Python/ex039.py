a = int(input('\033[1;30mEm que ano você nasceu?\033[m '))
b = 2020 - a
if b == 18:
    print('\033[1;33mVocê ja tem 18 anos, está na hora de se alistar!')
elif b < 18:
    print('\033[1;31mVocê ainda não tem 18 anos, então você não prescisa se alistar! ')
elif b >= 19:
    print('\033[1;32mVocê já tem mais de 18, você tem {} anos, então ja passou do seu tempo de alistamento'.format(b))
