numeros = []
contador = 1

def soma():
    soma_numeros = sum(numeros)
    print ('A soma dos números é ', soma_numeros)
    media_numeros = (soma_numeros / (len(numeros)))
    print ('A media dos numeros é ', media_numeros)
    
for i in range(5):
    informe_numero = int(input(f'Digite o {contador}º número: '))
    contador += 1
    numeros.append(informe_numero)
    
soma()



 