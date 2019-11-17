import os
#Ejercicio 8
#Comentario:programa para verificar si el individuo puede ir de paseo
#Asignacion de valores:
pasajes=20
comida=30
golosinas=10
dinero=float(os.sys.argv[1])
#Processing:
total=pasajes+comida+golosinas
#Inicio if:
if dinero<total:
    print("OH NO")
    print( "No puedes salir")
if dinero>total:
    print("FELICIDADES")
    print( "Si puedes salir")
else:
    print("FELICIDADES")
    print("Si puedes salir")
    print("Se recomienda no realizar ningun gasto preprogramado")


#Fin if