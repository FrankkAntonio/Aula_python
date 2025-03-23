# Problema: As maçãs custam R$ 1,30 cada, se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

maças = int(input('Quantas maçãs você vai comprar: '))

if maças < 12:
    preço_por_maças = 1.30
else:
    preço_por_maças = 1.00

custo_total = maças * preço_por_maças

print(f"O custo total da compra é: R$ {custo_total:.2f}")
