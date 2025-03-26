#ATRIBUIÇÕES
nome = str(input('Qual é seu nome: '))
N1 = float(input('Qual sua primeira nota?: '))
N2 = float(input('Qual sua segunda nota?: '))
N3 = float(input('Qual sua terceira nota?: '))


media = (N1 + N2 + N3)/3
conceito_obtido = media


#IMPRESSOES
print('Nome: ', nome)
print('Média: ', media)

if media >=6:
    print('Voce foi APROVADO!')
else:
    print('Voce foi REPROVADO!')

match conceito_obtido:
    

    case m if 9 <= m <= 10:
        print('Seu conceito obtido é A!')
    case m if 8 <= m < 9:
        print('Seu conceito obtido é B!')
    case m if 7 <= m < 8:
        print('Seu conceito obtido é C!')
    case m if 6 <= m < 7:
        print('Seu conceito obtido é D!')
    case m if m < 6:
        print('Seu conceito obtido é E!')
    case _:
        print('Seu número é inválido')


#Outra forma de ser feito
print('Outra forma de ser feito')

if media >= 9 and media <= 10:
    status = 'aprovado'
    conceito = 'A'
elif media >= 8 and media < 9:
    status = 'aprovado'
    conceito = 'B'
elif media >= 7 and media < 8:
    status = 'aprovado'
    conceito = 'C'
elif media >= 6 and media < 7:
    status = 'aprovado'
    conceito = 'D'
else:
    status = 'reprovado'
    conceito = 'E'

match conceito:
    case 'A':
        print(f'Nome: {nome}, você foi {status} com conceito {conceito} \n Média: {media:.1f}')
    case 'B':
        print(f'Nome: {nome}, você foi {status} com conceito {conceito} \n Média: {media:.1f}')
    case 'C':
        print(f'Nome: {nome}, você foi {status} com conceito {conceito} \n Média: {media:.1f}')
    case 'D':
        print(f'Nome: {nome}, você foi {status} com conceito {conceito} \n Média: {media:.1f}')
    case 'E':
        print(f'Nome: {nome}, você foi {status} com conceito {conceito} \n Média: {media}')












