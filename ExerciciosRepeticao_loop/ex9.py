#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

impares = []

for i in range(51):
    if i % 2 != 0:
        impares.append(i)
        
print(impares, sep=" ")