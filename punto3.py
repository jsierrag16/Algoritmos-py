#Aplicar aumento del 15% en caso de que el sueldo es inferior a 300.000
#Variable

Sueldo = float(input("Ingrese el sueldo del trabajador: "))

if Sueldo < 300000:
    print ("Se le aumenta el 15%", round(Sueldo*1.15,1))
else:
    print ("No se hace aumento")