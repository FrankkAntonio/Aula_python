nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input('Digite a segunda nota: '))

resultado = (nota1 + nota2) / 2

if resultado >= 6:
    print(f'O aluno tirou {resultado }, portanto ele foi aprovado ')
else:
    print(f'O aluno tirou {resultado}, portanto ele foi reprovado')


