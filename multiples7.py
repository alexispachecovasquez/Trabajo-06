import os
#Ejercicio 7
#Comentario:Programa para verificar si el individuo puede salir de juerga con sus amigos
#Asignacion de valores:
dinero_ahorrado=float(os.sys.argv[1])
#Inicio if:
if dinero_ahorrado>60:
    print("Puede salir de juerga")
if dinero_ahorrado<60:
    print("No puede salir de juerga")
else:
    print("Puede salir de juerga")
    print("PERO no es recomendable salir")
#Fin if