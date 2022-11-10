#ExSt.018.py

#Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo,
#Retângulo ou Obtusângulo.
#Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
#Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º)
#TriânguloAcutângulo: possui três ângulos agudos. (menor que 90º)
 
a = float (input('Digite o primeiro ângulo: '))
b = float (input('Digite o segundo ângulo: '))
c = float (input('Digite o terceiro ângulo: '))
soma = a + b + c 

if soma > 180 or soma < 180:
    print ('Os valores digitados não formam um triângulo.')
elif a == 90 or b == 90 or c == 90:
    print ('Triângulo Retângulo: possui um ângulo reto. (igual a 90º)')
elif a > 90 or b > 90 or c > 90:
    print ('Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º)')
else:
    print ('Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)')
    