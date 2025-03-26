quantidade_atual = int(input('Digite a quantidade atual do estoque: '))
quantidade_maxima = int(input('Digite a quantidade máxima do estoque: '))
quantidade_minima = int(input('Digite a quantidade mínima do estoque: '))

quantidade_media = (quantidade_maxima + quantidade_minima) / 2

if quantidade_atual >= quantidade_media:
    print('Não efetuar a compra')
else:
    print('Efetuar a compra')