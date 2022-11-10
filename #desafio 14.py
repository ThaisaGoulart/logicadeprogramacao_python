#desafio 14 
#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto 



preço = float(input('Digite o preço do produto:'))
desconto = float(input('Digite o percentual de desconto:'))
valor_do_desconto = preço * desconto / 100
a_pagar = preço - valor_do_desconto
print (f'O valor do produto com desconto é {a_pagar}')
