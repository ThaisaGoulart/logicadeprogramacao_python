#ExSt002.py
#Faça um programa que receba a idade e o peso de uma pessoa. De acordo com a tabela a seguir,
#verifique e mostre em qual grupo de risco essa pessoa se encaixa.

idade = int (input('Digite sua idade: '))
peso = float (input ('Digite seu peso: '))

if idade < 20 and peso <= 60:
    print ('Grupo de risco 9')
elif idade < 20 and peso >= 60 and peso <= 90:
    print ('Grupo de risco 8')
elif idade < 20 and peso > 90:
    print('Grupo de risco 7')
elif idade >= 20 <= 50 and peso <= 60:
    print ('Grupo de risco 6')
elif idade >= 20 <= 50 and peso >= 60 and peso <= 90:
    print ('Grupo de risco 5')
elif idade >= 20 <= 50 and peso > 90:
    print ('Grupo de risco 4')
elif idade > 50 and peso <= 60:
    print ('Grupo de risco 3')
elif idade > 50 and peso >=60 and peso <= 90:
    print ('Grupo de risco 2')
else: 
    print ('Grupo de risco 1')




    

    
    




