#Gratificação de natal 
#Uma empresa decidiu dar uma gratificação de Natal a seus funcionários,
#  #baseada no número de horas extras e no número de horas que o funcionário faltou ao trabalho. 
#O valor do prêmio é obtido pela consulta à tabela que se segue, na qual:
#H = número de horas extras – (2/3 * ( número de horas falta ))


horas_extras = float (input('Digite as horas extras: '))
horas_faltas = float (input ('Digite horas faltas: '))
horas_extras = horas_extras * 60
horas_faltas = horas_faltas * 60 
h = horas_extras - (2/3 * (horas_faltas))
if h < 600:
    gratificacao = 100
    print ('Gratificação de 100,00 reais.')
elif h >= 600 and h <= 1200:
    gratificacao = 200
    print ('Gratificação de 200,00 reias.')
elif h >= 1201 and h <= 1800:
    gratificacao = 300
    print ('Gratificação de 300 reais.')
else:
    gratificacao = 500
    print ('Gratificação de 500 reais. ')




