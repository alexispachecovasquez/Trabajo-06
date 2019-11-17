import os
#Ejercicio 6
#Comentario:Programa para verificar el estado de salud del adulto , sabiendo que tiene 30 años y mide 1.70
#Asignacion de valores:
peso=float(os.sys.argv[1])
#Inicio if:
if peso<60:
    print("Se encuentra en desnutricion")
    print("Mal estado de salud")
if peso>80:
    print("Se encuentra en obesidad ")
    print("Mal estado de salud")
if peso>59 and peso<81:
    print("Se encuentra en su peso ideal ")
    print("Buen estado de salud")
else:
    print(":)")
#Fin if