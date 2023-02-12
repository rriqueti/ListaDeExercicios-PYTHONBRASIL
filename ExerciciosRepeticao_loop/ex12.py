def tabuada(x):
    multiplicador = 1
    while multiplicador <= 10:
        produto = x * multiplicador
        print (f'{x} x {multiplicador} = {produto}')
        multiplicador += 1

x = int(input ('Imprima a tubuada do número: '))
tabuada(x)