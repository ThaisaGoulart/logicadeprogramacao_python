#ExSt.011.py
#As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem 
#compradas pelo menos doze.
#Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.

maca = float (input(' Digite o numero de maçãs compradas: '))
if maca < 12: 
    calculo1 = maca * 0.30 
    print (f'Custo total de maçãs: {calculo1}')
else: 
    calculo2 = maca * 0.25
    print (f'Custo total de maçãs: {calculo2} ')

