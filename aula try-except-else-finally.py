'''
Tratamento de exceções em Python 
try-except

Sintaxe:
try:
 #codigo que pode gerar uma exceção
except Tipo_de_exceção
 #codigo para lidar com a exceção

else: <opcional>

finally: <opcional>

'''

#Exemplo (sem tratamento de erros)
#num = int(input('Numero: '))
#print(f'Voce digitou o número: {num} ')

#Exemplo (com tratamento de erros)
teste = 1
while teste !=0:
    try:
        num = int(input('Numero: '))
        print(f'Voce digitou o número: {num} ')

    except ValueError:
        print('Voce deve escrever um número!')
    teste =  int(input('Digite 0 para encerrar o programa!'))

if teste ==0:
    print('Voce encerrou o programa!')
