#Desarrollar un programa que capture 3 numeros e imprima por pantallas cual de los numeros es mayor, el menor, cuales son iguales, si los 3 son diferentes 
#Variables

Num1 = float(input("Ingrese el primer número: "))
Num2 = float(input("Ingrese el segundo número: "))
Num3 = float(input("Ingrese el tercer número: "))

Mayor = max(Num1, Num2, Num3)
Menor = min(Num1, Num2, Num3)

if Num1 == Num2 == Num3:
    print("Los tres números son iguales.")
elif Num1 != Num2 != Num3 != Num1:
    print("Los tres números son diferentes.")
else:
    print("Al menos dos números son iguales.")

print("El mayor es: ", Mayor)
print("El menor es: ", Menor)
