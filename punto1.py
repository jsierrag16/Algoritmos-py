#Algoritmo que lea un numero y en caso de ser negativo lo imprima junto con su positivo
#Variable

Num = float(input("Ingrese un número negativo o positivo: "))

if Num < 0:
    print ("El número", Num, "es negativo, su positivo es: ", abs(Num))
else:
    print ("El", Num, "es un número positivo")