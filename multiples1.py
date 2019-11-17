import os
#Ejercicio 1
#Comentario:Programa para verificar si la division se puede calcular y si es una fraccion propia o impropia
#Asignacion de valores:
Diviendo=float(os.sys.argv[1])
divisor=float(os.sys.argv[2])
#Processing:
Resultado=Diviendo/divisor
#Inicio if:
if divisor>0 and Diviendo>divisor:
    print("La division posible")
    print("fraccion impropia")
if divisor>0 and divisor>Diviendo:
    print("La division posible")
    print("fraccion propia")
if divisor==0:
    print("La division es imposible")
else:
    print("El resultado es la unidad")
#Fin if
print("El resultado es:",Resultado)