

#Faça um programa que leia 5 números e informe o maior número.

valores = []
contador = 1

for i in range(5):
    informe = int(input(f'Digite o {contador}º número: '))
    contador += 1
    valores.append(informe)
print (valores)
maior_valor = max(valores)
print ('O maior valor informado é o número:',maior_valor)