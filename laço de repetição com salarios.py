'''
Crie um programa em Python que recebe como entrada quatro salário, o programa deve calcular a média salarial e exibir o salário, o programa deve calcular a média salarial e exibir os salário que estão abaixo da média.
'''

salarios = [0, 0, 0, 0]
soma = 0

i = 0 #controle do looping
#preenchendo a lista salarios
while i < 4:
    salarios[i] = float(input('Salário R$: '))
    soma +=salarios[i]
    i+=1

#calcular media
media = soma/len(salarios)
print (f'Média Salarial: {media:.2f}')

#imprimir os salários que estão abaixo da média

i = 0
while i<4:
    if salarios[1] < media:
        print(f'Salário abaixo da média: {salarios[1]:.2f}')
    i+=1