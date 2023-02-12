#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual 
# ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    senha = ''
    usuario = input('Login: ')
    senha = input('Senha: ')
    #validação da senha
    
    if usuario == senha:
        print ('A senha informada não pode ser igual ao usuário')
        
    if usuario != senha:
        print ('Usuario e senha cadastrado com sucesso')
        break