#Promedio con las 2 notas mas altas

Nota1 = float(input("Ingrese la primera nota: "))
Nota2 = float(input("Ingrese la segunda nota: "))
Nota3 = float(input("Ingrese la tercera nota: "))

if Nota1 <= Nota2 and Nota2 <= Nota3:
    promedio = (Nota2 + Nota3) / 2
elif Nota2 <= Nota1 and Nota2 <= Nota3:
    promedio = (Nota1 + Nota3) / 2
else:
    promedio = (Nota1 + Nota2) / 2

print("Su calificación final (promedio de las dos notas más altas) es:", promedio)
