a = int(input('\033[1;33mEm que ano você nasceu?\033[m '))
b = 2020 - a
if b <= 9:
    print('\033[1;30m-' * 25)
    print('\033[1;30mVocê tem {} anos'.format(b))
    print('\033[1;30m-' * 25)
    print('\033[1;35mE então se classifica como um nadador MIRIM!')
elif b <= 14:
    print('\033[1;30m-' * 25)
    print('\033[1;30mVocê tem {} anos'.format(b))
    print('\033[1;30m-' * 25)
    print('\033[1;34mE então se classifica como um nadador INFANTIL!')
elif b <= 19:
    print('\033[1;30m-' * 25)
    print('\033[1;30mVocê tem {} anos'.format(b))
    print('\033[1;30m-' * 25)
    print('\033[1;36mE então se classifica como um nadador JUNIOR!')
elif b <= 25:
    print('\033[1;30m-' * 25)
    print('\033[1;30mVocê tem {} anos'.format(b))
    print('\033[1;30m-' * 25)
    print('\033[1;32mE então se classifica como um nadador SÊNIOR!')
elif b > 25:
    print('\033[1;30m-' * 25)
    print('\033[1;30mVocê tem {} anos'.format(b))
    print('\033[1;30m-' * 25)
    print('\033[1;31mE então tem mais de 25 anos, então se classifica como um nadador MASTER!')
