while(True):
    m = float(input('Uma distancia em metros:'))
    dm = m * 10
    cm = m * 100
    mm = m * 1000
    dam = m / 10
    hm = m / 100
    km = m / 1000
    print('O seu valor é: {}m\n'.format(m))
    print('O valor em decimetros é {}\n'.format(dm))
    print('O valor em centimetros {}\n'.format(cm))
    print('O valor em milimetros {}\n'.format(mm))
    print('O valor em decâmetros {}\n'.format(dam))
    print('O valor em hectometros {}\n'.format(hm))
    print('O valor em quilometros {}\n'.format(km))
