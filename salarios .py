salarios = []
soma = 0

for i in range(4):
    salario = float(input('Salário R$: '))
    soma+=salario
    salarios.append(salario) #adiciona salario em salarios

media = soma/len(salarios)
print(f'Média: {media:.2f}')

for salario in salarios:
    if salario < media:
        print(f'Salário: {salario:.2f}')