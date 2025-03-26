print('Programa que fala que dia que é o rodízio de seu carro')
print('-------------------------------------------------------')

final_placa = int(input('Por favor, digite o último digito da placa de seu carro: '))

if final_placa == 1 or final_placa == 2:
    print('Seu rodízio é segunda feira')
elif final_placa == 3 or final_placa == 4:
    print('Seu rodízio é terça feira')
elif final_placa == 5 or final_placa == 6:
    print('Seu rodízio é quarta feira')
elif final_placa == 7 or final_placa == 8:
    print('Seu rodízio é quinta feira')
elif final_placa == 9 or final_placa == 0:
    print('Seu rodízio é sexta feira')
else:
    print('O número que voce digitou não está presente no rodízio')


print('------------------------------------------------')
print('O mesmo programa, mas agora feito com match-case')
print('------------------------------------------------')

final_placa = int(input('Por favor, digite o último digito da placa de seu carro: '))

match final_placa:
    case 1|2:
        print('Seu rodízio é segunda feira')
    case 3|4:
        print('Seu rodízio é terça feira')
    case 5|6:
        print('Seu rodízio é quarta feira')
    case 7|8:
        print('Seu rodízio é quinta feira')
    case 9|0:
        print('Seu rodízio é sexta feira')
    case _:
        print('O número que voce digitou não está presente no rodízio')
