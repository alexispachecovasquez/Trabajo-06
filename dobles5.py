import os
#Ejercicio 5
#Comentario:programa para verificar si el individuo puede obtener descuento
#Asignacion de valores:
nmro_premios=float(os.sys.argv[1])
#Inicio if:
if nmro_premios>50:
    print("FELICIDADES")
    print("ganaste 5 premios mas")
if nmro_premios<50:
    print("Gracias por jugar")
#Fin if