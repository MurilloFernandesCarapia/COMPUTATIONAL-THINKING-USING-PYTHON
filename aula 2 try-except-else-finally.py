'''
Exemplo com multiplas exceções 
'''
while True:
    try:
        n1 = int(input('Número 1: '))
        n2 = int(input('Número 2: '))
        result = n1/n2
        print(f' O resultado é {result}')

    except ZeroDivisionError:
        print('Não é permitido divisão por zero! ')

    except ValueError:
        print('Por favor digite apenas Números !')