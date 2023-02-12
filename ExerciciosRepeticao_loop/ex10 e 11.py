#Faça um programa que receba dois números 
# inteiros e gere os números inteiros que 
# estão no intervalo compreendido por eles.

lista = []
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro maior que o primeiro numero: '))

if num2 < num1:
    print('O segundo número informado foi menor que o primeiro')
    
else:

    while num1 <= num2:
        lista.append(num1)
        print(num1)
        num1 += 1
    
    print('A soma dos número entre o primeiro numero e o segundo é ', sum(lista))

