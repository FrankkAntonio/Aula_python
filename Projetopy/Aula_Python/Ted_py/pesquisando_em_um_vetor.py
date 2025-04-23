from random import randint

lista_numeros = []

for n in range(20):
    numero = randint(0, 1000)
    lista_numeros.append(numero)

print(lista_numeros)