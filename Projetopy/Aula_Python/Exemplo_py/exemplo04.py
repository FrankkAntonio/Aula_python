idade = int(input('Digite sua idade: '))

# Idade > 17
if idade >= 18:
    print('Pode ficar na festa de boas!')

# idade > 14 and idade < 18
elif 14 < idade < 18: # Inclucivo e não inclusivo
    print('Desapareça daqui!')

else:
    print('Vá sin bora!')