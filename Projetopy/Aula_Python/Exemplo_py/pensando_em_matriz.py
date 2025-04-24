from random import randint

matriz = []

for i in range(10):
    lista_temporaria = []
    for l in range(10):
        lista_temporaria.append(randint(0, 1000))

    matriz.append(lista_temporaria)
maior = -1

for li in range(len(matriz)):
    print(matriz[li])
    for co in range(len(matriz[li])):
      if maior < (matriz[li][co]):
          maior = (matriz[li][co])

print(f'Esse é o maior valor: {maior}')

