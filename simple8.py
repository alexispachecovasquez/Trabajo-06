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
#Fin if