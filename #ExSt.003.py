#ExSt.003.py 
#Faça um programa que receba a idade de um nadador e mostre sua categoria, 
#usando as regras a seguir. Para idade inferior a 5, qual mensagem deveríamos mostrar?

idade = int(input('Digite sua idade: '))
if idade <= 5 and idade <= 7:
    print ('Categoria infantil. ')
elif idade >= 8 and idade <= 10:
    print ('Categoria juvenil. ')
elif idade >= 11 and idade <= 15:
    print ('Categoria adolescente. ')
elif idade >= 16 and idade <=30:
    print ('Categoria adulto. ')
elif idade > 30:
    print ('categoria sênior.')
else:
    print ('Esta idade não corresponde as categorias existentes.')
