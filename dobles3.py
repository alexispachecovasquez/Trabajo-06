import os
#Ejercicio 3
#Comentario:programa para verificar si el individuo debe renunciar
#Asignacion de valores:
sueldo_mensual=float(os.sys.argv[1])
gasto_mensual=float(os.sys.argv[2])
#Inicio if:
if sueldo_mensual<gasto_mensual:
    print("Mal estado economico")
    print("renunciar al trabajo")
if sueldo_mensual>gasto_mensual:
    print("Buen estado economico")
    print("No renunciar al trabajo")
#Fin if
