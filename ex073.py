times = ('Palmeiras', 'Internacional', 'Fluminense',
          'Corinthians', 'Flamengo', 'Athletico-PR',
          'Atlético-MR', 'Fortaleza', 'São Paulo',
          'América-MG', 'Botafogo', 'Santos',
          'Goiás', 'Bragantino', 'Coritiba',
          'Cuiabá', 'Ceará SC', 'Atlético-GO',
          'Avaí', 'Juventude')
print('-='*20)
print(f'Lista de times do Brasileirão: {times}')
print('-='*20)
print(f'Os 5 primeiros são {times[:5]}')
print('-='*20)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*20)
print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição')

# for c in times:
#    print(c)
# print(f'Os 4 últimos são {times[16:]}')