#ExSt.012.py
#Escreva um programa para ler 3 valores inteiros
# (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.
valor1 = int (input('Digite primeiro valor: '))
valor2 = int (input('Digite segundo valor: '))
valor3 = int (input('Digite terceiro valor:'))

if valor1 > valor2 and valor2 > valor3:
    print (f' {valor3}, {valor2},{valor1}')
elif valor2 > valor1 and valor1 > valor3:
    print (f' {valor3}, {valor1} ,{valor2} ')  
elif valor1 > valor3 and valor3 > valor2:
    print (f'{valor2},{valor3},{valor1}')
elif valor2 > valor3 and valor3 > valor1:
    print (f'{valor1},{valor3},{valor2}')
elif valor3 > valor2 and valor2 > valor1:
    print (f'{valor1},{valor2},{valor3}')
else:
    print(f'{valor2},{valor1},{valor3}')



