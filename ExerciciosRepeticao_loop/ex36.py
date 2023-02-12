# Desenvolva um programa que faça a tabuada de um número qualquer 
# inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e 
# terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
cancelador = 1

while cancelador !=0:
    print ('Digite 0 para fechar o programa')
    num_inf = int(input ('Tabuada do: '))

    if num_inf == 0:
        cancelador = 0
        print ('Programa encerrado')
        break
    
    prim_nm = int(input ('Começar do numero: '))
    seg_nm = int(input ('Terminar no número: '))
    
    if prim_nm < seg_nm:
        while prim_nm <= seg_nm:
            produto = num_inf * prim_nm
            print (num_inf, 'x', prim_nm, '=', produto)
            prim_nm += 1
    else:
        print('O segundo numero multiplicador informado é menor que o primeiro')

    