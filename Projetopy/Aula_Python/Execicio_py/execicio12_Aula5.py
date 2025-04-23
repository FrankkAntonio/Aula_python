#Contexto: Determinação do tipo de triângulo. Questão: Peça ao usuário para inserir três lados de um triângulo e determine se é um triângulo equilátero, isósceles ou escaleno.
lado1 = int(input('Digite um lado do triangulo: '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digite o terceiro lado: '))

# Processamento e Saída
if lado1 == lado2 == lado3:
    print('Equilátero!')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('Isóceles!')
elif lado1 != lado2 != lado3:
    print('Escaleno!')