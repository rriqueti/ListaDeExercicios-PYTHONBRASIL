""" Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).
Solução: Validação de dados em Python """


while True:
    nome = input ('Digite um nome: ')
    
    if len(nome) <= 3:
        print('Nome muito curto')
        continue
    
    while True:
        idade = int(input('Idade: '))
        if idade > 0 and idade <= 150:
            break
        else:
            print ('Idade inválida')
    
    while True:
        sexo = input('[m]asculino ou [f]eminino: ')
        sexo.islower()
        if sexo != 'm' and sexo != 'f':
            print('Resposta inválida')
            continue
        else:
            break
    while True:
        civil = input('Estado Civil: [s], [c], [v], [d]: ')
        if civil in 'scvd':
            break
        else:
            print('Resposta inválida')
            continue
 
    print('Todas perguntas foram respondidas corretamente. \nQuetionário encerrado')
    break
