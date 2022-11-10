#desafio 10 
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros 

from re import M


valor = int(input('Digite um valor em metros: '))
centimetro = valor * 100 
milimetro = valor * 1000
print (f'O valor em centímetros é {centimetro} e o valor em milímetros é {milimetro}')

