#Data com mês por extenso. Construa uma função que receba uma 
# data no formato DD/MM/AAAA e devolva uma string no formato 
# D de mesPorExtenso de AAAA. Opcionalmente, valide a data e 
# retorne NULL caso a data seja inválida.

def informeData(d,m,a):
    mesesAno = ['','Janeiro','Fevereiro','Março','Abril','Maio',
                'Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    return f'{d} de {mesesAno[m]} de {a}'

d = int(input('Dia: '))
m = int(input('MÊS: '))
a = int(input('Ano: '))   

print(informeData(d,m,a))
