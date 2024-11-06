
densidad = 3.5 

longitud = float(input("Ingrese la longitud de la varilla en cm: "))
diametro = float(input("Ingrese el diámetro de la varilla en cm: "))

masa = (diametro * longitud) / densidad

if 7.5 < longitud <= 9.0:
    if 0.5 <= diametro <= 1.3:
        if masa <= 5.8:
            print("La pieza es aceptada.")
        else:
            print("La pieza es rechazada: la masa excede el límite de 5.8 gramos.")
    else:
        print("La pieza es rechazada: el diámetro no está dentro del rango permitido (0.5 cm - 1.3 cm).")
else:
    print("La pieza es rechazada: la longitud no está dentro del rango permitido (7.5 cm - 9.0 cm).")
