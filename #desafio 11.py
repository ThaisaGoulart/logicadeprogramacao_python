#desafio 11 
# faça um programa que leia um número inteiro e mostre sua tabuada 

# Para i variando de 1 a 10
# Para (de, até, incremento)
numero = int(input('Digite um numero:'))
print (f' A tabuada de {numero} é')
#para i (in = dentro) (range= varia)
for i in range (1,11,1):
    multiplicacao = numero * i
    print (multiplicacao)