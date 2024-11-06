#Algoritmo que lea nombre, edad, sexo, estado civil
#Variables

Nombre = input("Ingrese su nombre: ")
Edad = int(input("Ingrese su edad: "))
Sexo = input("Ingrese (M) si es Masculino o (F) si es Femenino: ")
EstadoCivil = input("Ingrese (S) si esta Solter@ o (C) si es Casad@: ")

#Usar variable.lower() para convertir a minusculas o .upper() para convertir a mayusculas

if Sexo.upper() == "F" and EstadoCivil.lower() == "s" and Edad < 50:
    print ("Su nombre es: ",Nombre)
elif Sexo.upper() == "M" and EstadoCivil.lower() == "c" and Edad > 40:
    print ("Su nombre es: ",Nombre)
else:
    print ("No cumple con las condiciones")