# Jogo de Craps. Faça um programa de implemente 
# um jogo de Craps. O jogador lança um par de 
# dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, 
# você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é 
# chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 
# ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar 
# este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random

def girarDados(a=2, b=12):
    return random.randint(2, 12)

rodada = 0
while True:
    resultadoJogo = girarDados()
    
    pontuacao = 1
    if resultadoJogo in (2,3,12) and rodada == 0:
        print('número', resultadoJogo, 'CRAPS! você Perdeu')
        break
    if rodada == 0 and resultadoJogo == 7 or resultadoJogo == 11:
        print('numero', resultadoJogo,'NATURAL, você Ganhou!')
        break
    if resultadoJogo in (4, 5, 6, 8, 9, 10):
        print (f'PONTO! Você ganhou uma vantagem')
        pontuacao -= 1
    if resultadoJogo == 7 and pontuacao == 1:
        print('número', resultadoJogo, 'CRAPS! você Perdeu')
        break
    rodada += 1  
