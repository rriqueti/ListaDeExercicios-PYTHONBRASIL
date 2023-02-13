#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 
#14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
#Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para 
#registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def conversao(a,b):
  if a >= 13 and a <= 24:
    a = a -12
    print('Sua hora é',a,':',b,"PM")
  else:
    print('Sua hora é',a,':',b, "AM")

while True:
  print ('Digite 99 para sair')
  a = int(input('Digite a hora: '))
  if a == 99:
    print('Programa encerrado')
    break
  else:
    b = int(input('Digite os minutos: '))
    conversao(a,b)
    print( )
