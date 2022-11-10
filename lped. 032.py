#lped.036.py

valor_compra = float (input ('Digite o valor de compra: '))
if valor_compra < 10.00:
    lucro = 1.7
elif valor_compra >= 10.00 and valor_compra < 30.00:
    lucro = 1.5
elif valor_compra >= 30.00 and valor_compra < 50.00:
    lucro = 1.4
else:
    lucro = 1.3

venda_final = (valor_compra * lucro) 
print (f'O valor de venda é {venda_final}')

