#xSt.017.py 
#Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, 
#Isósceles ou Escaleno
#Sendo que:
#Triângulo Equilátero: possui os 3 lados iguais.
#Triângulo Isóscele: possui 2 lados iguais.
#Triângulo Escaleno: possui 3 lados diferentes.

medida_lados1 = float(input ('Digite a primeira medida dos lados do  triângulo: '))
medida_lados2 = float(input ('Digite a segunda medida dos lados do  triângulo: '))
medida_lados3 = float(input ('Digite a terceira medida dos lados do triângulo: '))
if medida_lados1 == medida_lados2 == medida_lados3:
    print ('Triângulo Equilátero: possui os 3 lados iguais.' )
elif medida_lados1 == medida_lados2 != medida_lados3:
    print ('Triângulo Isóscele: possui 2 lados iguais.' ) 
elif medida_lados1 == medida_lados3 != medida_lados2: 
    print ('Triângulo Isóscele: possui 2 lados iguais.' )
elif medida_lados3 == medida_lados2 != medida_lados1:
    print ('Triângulo Isóscele: possui 2 lados iguais.' )
else:
    print('Triângulo Escaleno: possui 3 lados diferentes')

    