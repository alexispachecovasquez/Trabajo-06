import os
#Ejercicio 2
#Comentario:Programa para verificar si el individuo es mayor de edad o menor de edad
#Asignacion de valores:
año_nacimiento=float(os.sys.argv[1])
año_actual=float(os.sys.argv[2])
#Processing:
edad=año_actual-año_nacimiento
#Inicio if:
if año_nacimiento<año_actual and edad>=18:
    print("Es mayor de edad")
if año_nacimiento<año_actual and edad<18:
    print("Es menor de edad")
#Fin if
print("Su edad es:",edad)