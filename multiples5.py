import os
#Ejercicio 5
#Comentario:programa para verificar si el individuo puede obtener descuento
#Asignacion de valores:
nmro_premios=float(os.sys.argv[1])
#Inicio if:
if nmro_premios>50:
    print("FELICIDADES")
    print("ganaste 5 premios mas")
if nmro_premios<50 and nmro_premios>20:
    print("FELICIDADES")
    print("ganaste 1 premio mas")
if nmro_premios>49 and nmro_premios<70:
    print("FELICIDADES")
    print("ganaste 10 premios mas")
else:
    print("Gracias por jugar")
#Fin if