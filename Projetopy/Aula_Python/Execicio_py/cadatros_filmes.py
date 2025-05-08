import time
from logging import exception

from loguru import logger

bd_filmes = []

def cadastra_filmes(bd, titulo, ano):
    filme = [titulo, ano]
    bd.append(filme)
    return bd

def lista_filmes(bd):
    logger.info('Listagem de fimes')
    for i in range(len(bd)):
       print(f'{i+1} | {bd[i][1]} | {bd[i][0]}')

def altera_filme(bd, indice, titulo, ano):
    bd[indice][0] = titulo
    bd[indice][1] = ano
    return bd

def salva_filmes(bd):
    with open('bd_filmes.txt', 'w', encoding='utf-8') as arquivo:
        for i in range(len(bd)):
            logger.info(f'Salvando o filme {bd[i][0]}')
            arquivo.write(f'{bd[i][1]}, {bd[i][0]}\n')


while True:
    print('1- Cadastrar Filme')
    print('2 - Listar Filme')
    print('3 - Alterar Filme')
    print('4 - Salvar Filmes')

    try:
        op = int(input('Digite sua opção: '))
    except exception as e:
        logger.error(f'Error: {e}')
        logger.info('Digite um valor númerico!')
        op = -1

    if op == 1:
        logger.info('Iniciando o cadastro de filme.')

        titulo = input('Digite o titulo do filme:')
        ano = int(input('Digite o ano do filme: '))

        bd_filmes = cadastra_filmes(
            bd = bd_filmes,
            titulo = titulo,
            ano = ano
        )
        logger.info('filme cadastrado com sucesso!')

    elif op == 2:
        logger.info('iniciando listagem de Filmes')
        lista_filmes(bd_filmes)
        logger.info('Filmes listado com sucesso!')

    elif op == 3:
        logger.info('iniciando alteração de filmes')
        lista_filmes(bd_filmes)
        i = int(input('Qual filme deseja alterar?'))
        titulo = input('Digite o novo titulo: ')
        ano = int(input('Digite o novo ano: '))
        bd_filmes = altera_filme(
            indice=(i-1),
            titulo=titulo,
            ano=ano
            )

        logger.info('Filmes alterado com sucesso!')

    elif op == 4:
        logger.info('iniciando persistencia dos filmes')
        salva_filmes(bd_filmes)
        logger.info('Filmes salvos com sucesso!')

    else:
        print(f'Opção {op} inválida!')

    time.sleep(2)