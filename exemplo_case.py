dia = int(input('Digite um dia númerico: '))
match dia:
  case 1:
     print("Dia útil!")
  case 2:
   print("Final de semana ou feriado!")
  case _:
     print(f"Valor {dia} inválido")