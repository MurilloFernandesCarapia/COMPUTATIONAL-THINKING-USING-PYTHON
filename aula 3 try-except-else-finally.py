try:
    n1= int(input('Digite o n1: '))
    n2= int(input('Digite o n2: '))
    resultado = n1/n2
    print(f'{resultado}')
    lista = [1,2,3]

    for n in lista:
        print(f'Elemento: {n}')

    num = int(input('Digite um outro número para a lista: '))
    lista.append(num)

    print (lista[3])

except ValueError:
    print('Por favor digite apenas Números!')

except ZeroDivisionError:
    print('Erro: Divisão por ZERO!')

except IndexError:
    print('Indice fora do Range!')
except Exception as e:
    print(f'Erro genérico! O seu é {e}')

else: #opcional
    print('Deu tudo certo!')

finally: #opcional
    print('Encerrando o Programa!')