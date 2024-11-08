#Desarrollar el algoritmo que diga si un numero es divisible del otro

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num2 != 0 and num1 % num2 == 0:
    print(f"{num1} es divisible por {num2}.")
elif num3 != 0 and num1 % num3 == 0:
    print(f"{num1} es divisible por {num3}.")
elif num1 != 0 and num2 % num1 == 0:
    print(f"{num2} es divisible por {num1}.")
elif num3 != 0 and num2 % num3 == 0:
    print(f"{num2} es divisible por {num3}.")
elif num1 != 0 and num3 % num1 == 0:
    print(f"{num3} es divisible por {num1}.")
elif num2 != 0 and num3 % num2 == 0:
    print(f"{num3} es divisible por {num2}.")
else:
    print("No hay divisibilidad entre los números.")


