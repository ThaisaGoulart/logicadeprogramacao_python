##xSt.0015.py 

#Acrescente as seguintes mensagens à solução da tarefa 14 conforme o caso.
#Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
#Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.

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
elif numero_lados < 3:
    print ('NÃO É UM POLÍGONO.')
elif numero_lados > 5: 
    print ('POLÍGONO NÃO IDENTIFICADO.')



