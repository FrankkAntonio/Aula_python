num = int(input('Digite um número da tabuada: '))

print('---- Solução com FOR ----')
for m in range(1, 11):
    resultado = num * m
    print(f'{num} x {m} = {resultado} ')

print('---- Solução com WHILE ----')
ciclos = 1

while ciclos <= 10:
    resultado = num * ciclos
    print(f'{num} x {ciclos} = {resultado}')
    # Incremento
    ciclos += 1
