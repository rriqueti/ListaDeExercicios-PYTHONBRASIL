#Supondo que a população de um país A 
# seja da ordem de 80000 habitantes com uma 
# taxa anual de crescimento de 3% e que a população de 
# B seja 200000 habitantes com uma 
# taxa de crescimento de 1.5%. Faça um programa 
# que calcule e escreva o número de anos 
# necessários para que a população do país A 
# ultrapasse ou iguale a população do país B, mantidas as 
# taxas de crescimento.



pop_a = int(input('População A: '))
taxa_a = float(input ('Taxa de crescimento A: (%)'))
pop_b = int(input('População B: '))
taxa_b = float(input ('Taxa de crescimento B: (%)'))
     
porcento_a = taxa_a / 100
porcento_b = taxa_b / 100
contagem_ano = 0

while pop_a < pop_b:
    pop_a = pop_a + (taxa_a * pop_a)
    pop_b = pop_b + (taxa_b * pop_b)
    contagem_ano += 1
    
print (pop_a, pop_b)


print (f'Demorou {contagem_ano} anos para que a população A alcançace a população B')
    
    
    
