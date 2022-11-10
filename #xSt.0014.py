#xSt.0014.py 


#Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm).
#Calcular e imprimir o seguinte:
#Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área
#Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
#Se o número de lados for igual a 5 escrever PENTÁGONO.

numero_lados = float (input ( 'Digite o número de lados do polígono regular: '))
medida = float (input ('Digite a medida dos lados: '))
if numero_lados == 3:
    print ('TRIÂNGULO')
    altura = ((medida ** 2) - ((medida / 2) ** 2)) ** 0.5 
    valor_area = medida * altura / 2 
    print (f'O valor de sua área é:  {valor_area} ')
elif numero_lados == 4:
    print ('QUADRADO ')
    valor_area = medida * medida 
    print (f'O valor de sua área é:  {valor_area} ')
elif numero_lados == 5:
    print ('PENTÁGONO')
    altura = ((medida ** 2) - ((medida / 2) ** 2)) ** 0.5
    valor_area = medida * altura / 2 * 5 
    print (f'O valor de sua área é:  {valor_area} ')

