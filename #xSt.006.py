#xSt.006.py 

#Faça um programa que receba o salário de um funcionário chamado Carlos. Sabe-se que outro funcionário,
#João, tem salário equivalente a um terço do salário de Carlos. Carlos aplicará seu salário integralmente 
#na caderneta de poupança, que rende 2% ao mês, e João aplicará seu salário integralmente no fundo de 
#renda fixa, que rende 5% ao mês. O programa deverá calcular e mostrar a quantidade de meses necessários
#para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos.

salario_carlos = float(input( 'Digite o salário do funcionário: '))
salario_joao = salario_carlos * 1/3 
poupanca = 1.02
renda_fixa = 1.05 
meses = 0
while salario_joao <= salario_carlos:
    salario_carlos = salario_carlos * poupanca 
    salario_joao = salario_joao * renda_fixa 
    print(f'O salário do carlos agora vale: {salario_carlos:.2f}')
    print(f'O salário do joão agora vale: {salario_joao:.2f}\n')
    meses += 1
    
print(f'Levará {meses} meses para a renda se equiparar')



