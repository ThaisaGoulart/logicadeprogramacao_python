#exercício 5 
i = 1
salario_minimo = 450.00
while i <= 10:
    print(f'Funcionário {i}')
    categoria = (input ('Digite categoria do funcionário: '))
    if categoria != "o" and categoria != "g":
        print ('CATEGORIA INEXISTENTE. ')
        break
    turno = (input('Digite turno do funcionário: '))
    if turno != "n" and turno != "m" and turno != "v":
        print ('TURNO INEXISTENTE. ')
        break
    hora_trabalhada = float (input('Digite horas trabalhadas: '))
    if categoria == "g" and turno == "n": 
        valor_hora = salario_minimo * 0.18
    elif (categoria == "g" and turno == "v") or (turno == "m"): # cuidado quando usar operadores lógicos diferentes
        valor_hora = salario_minimo * 0.15
    elif categoria == "o" and turno == "n": 
        valor_hora = salario_minimo * 0.13
    else:
        valor_hora = salario_minimo * 0.10
    salario_inicial = hora_trabalhada * valor_hora
    if salario_inicial <= 300.00:
        auxilio_alm = salario_inicial * 0.20
    elif salario_inicial > 300.00 and salario_inicial <= 600.00:
        auxilio_alm = salario_inicial * 0.15
    else: 
        auxilio_alm = salario_inicial * 0.05
        salario_final = salario_inicial + auxilio_alm  
    print (f'Horas trabalhadas: {hora_trabalhada}')
    print (f'Valor das horas: {valor_hora}')
    print (f'O salário inicial:  {salario_inicial}')        
    print (f'Valor auxilio alimentação: {auxilio_alm}')
    print (f'Salário final: {salario_final}')
    i += 1