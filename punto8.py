#Prepare algoritmo que lea el numero medio de 3 numeros unicos.
#Variables

N1 = int(input("Ingrese el número 1: "))
N2 = int(input("Ingrese el número 2: "))
N3 = int(input("Ingrese el número 3: "))

if (N1 > N2 and N1 < N3) or (N1 > N3 and N1 < N2):
    medio = N1
elif (N2 > N1 and N2 < N3) or (N2 < N1 and N2 > N3):
    medio = N2
else:
    medio = N3
print ("El numero medio es ",medio)