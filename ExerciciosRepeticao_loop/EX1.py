#Faça um programa que peça uma nota, 
# entre zero e dez. Mostre uma mensagem 
# caso o valor seja inválido e continue 
# pedindo 
# até que o usuário informe um valor válido.


while True:
    nota_informada = int(input ('Digite uma nota de 0 a 10: '))
    
    if nota_informada > 10 or nota_informada < 0:
        print ('A nota informada não é valida')
    else:
        print ('A nota informada é', nota_informada)
        break
            