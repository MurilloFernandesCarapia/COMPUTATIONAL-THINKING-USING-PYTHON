print ("---------------------------------------------")
print ("Olá esta é uma calculadora feita em Python...")
print ("---------------------------------------------")

num1 = float(input("Qual o seu primeiro número: "))
num2 = float(input("Qual o seu segundo número: "))



opcao =  str(input("Escolha o tipo de operação \n(a - Multiplicação, \n b - Subtração, \n c - Soma, \n d - Divisão) : "))


if  opcao == "a":
    print ("Resultado: ", num1 * num2 )
elif opcao == "b" :
    print ("Resultado: ", num1 - num2 )
elif opcao == "c" :
    print ("Resultado: ", num1 + num2)
elif  opcao == "d" :
    print ("Resultado: ", num1 / num2)

