import os
#Ejercicio 4
#Comentario:programa para verificar si el alumno aprobara o no
#Asignacion de valores:
examen1=float(os.sys.argv[1])
examen2=float(os.sys.argv[2])
trabajo_final=float(os.sys.argv[3])
exposicion_final=float(os.sys.argv[4])
#Processing:
promedio=(examen1+examen2+trabajo_final+exposicion_final)/4
#Inicio if:
if promedio<11:
    print("Jalaste programacion")
#Fin if
print("Su promedio es de:",promedio)











