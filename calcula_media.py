print("-----------------------------------")
print("Olá esse programa calculo sua média")
print("-----------------------------------")

N1= float(input("Coloque a sua nota da primeira prova: "))
N2= float(input("Coloque a sua nota da segunda prova: "))
N3= float(input("Coloque a sua nota da terceira prova: "))

media = (N1 + N2 + N3)/3

print( " Sua média das provas são:", media)

if media >= 6:
    print("Voce foi aprovado de ano")
else:
    print("Voce foi reprovado de ano")

