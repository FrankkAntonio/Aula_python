import time

bd_filmes = []

def cadastra_filmes(bd, titulo, ano):
    filme = [titulo, ano]
    bd.append(filme)
    return bd


def lista_filmes(bd):
    for i in range(len(bd)):
       print(f'{i+1} | {bd[i][1]} | {bd[i][0]}')

def altera_filme(bd, indice, titulo, ano):
    bd[indice][0] = titulo
    bd[indice][1] = ano

    return bd


while True:
    print('1- Cadastrar Filme')
    print('2 - Listar Filme')
    print('3 - Alterar Filme')
    op = int(input('Digite sua opção: '))

    if op == 1:
        titulo = input('Digite o titulo do filme:')
        ano = int(input('Digite o ano do filme: '))

        bd_filmes = cadastra_filmes(
            bd = bd_filmes,
            titulo = titulo,
            ano = ano
        )
        print('Filme cadastrado!')
    elif op == 2:

        lista_filmes(bd_filmes)
        print('Filmes Listrados!')
    elif op == 3:
        lista_filmes(bd_filmes)
        i = int(input('Qual filme deseja alterar?'))
        titulo = input('Digite o novo titulo: ')
        ano = int(input('Digite o novo ano: '))
        bd_filmes = altera_filme(
            indice=(i-1),
            titulo=titulo,
            ano=ano
            )

        print('filme alterado!')
    else:
        print(f'Opção {op} inválida!')

    time.sleep(2)