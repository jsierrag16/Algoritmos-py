#Escriba el algoritmo que al capturar un numero entero convierta grados centigrados a Kelvin
#Variables

entrada = input("Introduce un valor: ")

try:
    numeroEntero = int(entrada)
    kelvin = numeroEntero + 273.15
    print ("La temperatura en valor de Kelvin es: ",kelvin)
except ValueError:
    try:
        numeroFlotante = float(entrada)
        if numeroFlotante > 10.5:
            print("el numero es mayor a 10.5")
        else:
            print("el numero es menor a 10.5")
    except ValueError:
        if len(entrada) == 1:
            print("Mi nombre es Juan")
        else:
            print("entrada no valida")