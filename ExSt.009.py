#ExSt.009.py
#Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma 
#mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).

nascimento = int (input ('Digite ano de nascimento: '))
if nascimento <= 2006:
    print ('Você possui idade para votação. ')
else:
    print ('Você não possui idade para votação.')