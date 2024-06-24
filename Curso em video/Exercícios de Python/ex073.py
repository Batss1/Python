times = ('Flamengo','Internacional','Juventude','Bragantino','Cruzeiro','Fortaleza','Athletico-PR','Grêmio','Vasco da Gama',
'Bahia','Palmeiras','Criciúma','Atlético-MG','Fluminense','Corinthians','Botafogo','Atlético-GO','EC Vitória','São Paulo','Cuiabá')

print('Os 5 primeiros colocados da tabela do brasileirão são:')
for c in range(5):
    print(times[c])
print('-='*30)

print(f'Os últimos 4 colocados da tabela: {times[-4:]}')
print('-='*30)

print(f'Os times em ordem alfabética: {sorted(times)}')
print('-='*30)

posicao = times.index('Corinthians')
print(f'O time Corinthians está em {posicao + 1}ª posição')

