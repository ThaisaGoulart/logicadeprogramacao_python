#ExSt.016.py
#Escreva um programa para ler 3 valores inteiros e escrever o maior deles. 
#Considere que o usuário não informará valores iguais.

valor1 = int (input('Digite primeiro valor: '))
valor2 = int (input('Digite segundo valor: '))
valor3 = int (input('Digite terceiro valor:'))

if valor1 > valor2 and valor1 > valor3:
    print (f' {valor1}')
elif valor2 > valor1 and valor2 > valor3:
    print (f' {valor2}')  
else:
     print (f'{valor3}')
