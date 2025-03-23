# 01 Processamento de dados
n_conta = (input('Digite o número da conta: '))
saldo = float(input('Digite seu saldo: '))
debito = float(input('Digite seu débito: '))
credito = float(input('Digite seu crédito: '))

#02 processamento
print(f'Saldo atual é R${saldo}.')
saldo_atual = saldo * debito + credito

#03 saída
if saldo_atual >= 0:
    print(f'O Saldo R${saldo_atual} é Positivo!')
else:
    print(f'O Saldo R${saldo_atual} é Negativo!')


