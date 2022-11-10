#ExSt.004.py
#Faça um programa que receba o salário bruto de um funcionário e, usando a tabela a seguir, 
#calcule e mostre o valor a receber. Sabe-se que este é composto 
#pelo salário bruto acrescido de gratificação e descontado o imposto de 7% sobre o salário.


salario_bruto = float (input('Digite o valor do salário bruto: '))
if salario_bruto <= 350.00:
    gratificacao = 100 
elif salario_bruto >= 351.00 and salario_bruto <= 600:
    gratificacao = 75
elif salario_bruto >= 601 and salario_bruto <= 900:
    gratificacao = 50
else:
    gratificacao = 35
calculo = (salario_bruto + gratificacao) * 0.07
salario_liquido = salario_bruto + gratificacao - calculo 
print (f'O salário liquido é: {salario_liquido}')
    