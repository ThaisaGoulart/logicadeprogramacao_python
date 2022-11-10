# desafio 11
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira em mostre quantos dólares ela pode comprar 
#considere US$ 3.27

dinheiro = float (input('Digite quanto dinheiro tem em sua carteira: '))
real = 1
dolar = 3.27
convercao = real/dolar 
total = dinheiro * convercao
print (f'A converção em dólares é: {total}')