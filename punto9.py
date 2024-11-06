#Algoritmo que ordene de mayor a menor

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

# Ordenar de mayor a menor usando condiciones
if a > b and a > c:
    if b > c:
        ordenado = [a, b, c]
    else:
        ordenado = [a, c, b]
elif b > a and b > c:
    if a > c:
        ordenado = [b, a, c]
    else:
        ordenado = [b, c, a]
else:
    if a > b:
        ordenado = [c, a, b]
    else:
        ordenado = [c, b, a]

print("Números ordenados de mayor a menor:", ordenado)
