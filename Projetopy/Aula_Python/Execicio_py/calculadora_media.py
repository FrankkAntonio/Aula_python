#Crie um programa que peça ao usuário para inserir várias notas de um aluno e calcule a média. Utilize um loop para continuar pedindo notas até que o usuário digite um valor específico para encerrar a entrada (por exemplo, -1).

print('Digite a nota do aluno, para encerrar digite -1')

notas = []
while True:
    try:
        nota = float(input('Digite uma notas: '))
        if nota == -1:
            break
        elif 0 <= nota <= 10:
            notas.append(nota)
        else:
            print('por favor digite uma nota de 0 a 10.')
    except ValueError:
        print('Digite invalido, por favor digite um número: ')


if notas:
    media = sum(notas) / len(notas)
    print(f'\nNotas inseridas {notas}')
    print(f'Média das notas: {media:.2f}')
else:
    print('Nenhuma nota valida foi inserida')

