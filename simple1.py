import os
#Ejercicio 1
#Comentario:Programa para verificar si la division se puede calcular o no
#Asignacion de valores:
Diviendo=float(os.sys.argv[1])
divisor=float(os.sys.argv[2])
#Processing:
Resultado=Diviendo/divisor
#Inicio if:
if divisor==0:
    print("La division es imposible")
#Fin if
print("El resultado es:",Resultado)