#desafio 12 

salario = float(input('Digite o valor do salário: '))
aumento = float (input('Digite o percentual de aumento: '))
calculo = salario * aumento /100
valor_aumento = salario + calculo
print (f'O salário fica em {valor_aumento}')