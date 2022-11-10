#desafio 13 
#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade 
#de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m ao quadrado 

#ler largura 
#ler altura 
#calcular a area e quantidade de tinta, cada litro pinta 2 metros ao quadrado 


altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura: '))
area = altura * largura 
litro_metro = 2.0
total = area / litro_metro
print (f' Será necessário {total} litros de tinta' )