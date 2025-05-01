#Escreva uma função chamada "conta_vogais" que receba uma string como parâmetro e retorne o número de vogais presentes nessa string. Considere que a string pode conter letras maiúsculas e minúsculas

def conta_vogais(texto):
    contado = 0
    vogais = ['a', 'e','i','o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letra in texto:
        if letra in vogais:
            contado += 1
    return contado


print(conta_vogais('abacaxi'))








