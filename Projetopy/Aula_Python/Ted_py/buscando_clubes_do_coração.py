clubes = [
    'Flamengo',
    'Vasco',
    'Botafogo',
    'Gremio',
    'Fluminense'

]

clube = input('Digite o clube desejado: ')
find = False

for i in range(len(clubes)):

   if clube.upper() == clubes[i].upper():
     find = True

if find:
    print('Achei!')
else:
    print('Não achei!')



