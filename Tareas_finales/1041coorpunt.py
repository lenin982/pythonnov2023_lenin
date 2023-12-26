#Escriba un algoritmo que lea dos valores flotantes (x e y), 
# que deben representar las coordenadas de un punto en un plano. A continuación, 
# determine qué cuadrante pertenece el punto o si está sobre uno de los ejes cartesianos o el origen (x = y = 0).

#Si el punto está en el origen, escriba el mensaje "Origem".

#Si el punto está sobre el eje X, escriba "Eixo X", de lo contrario si el punto está sobre el eje Y, escriba "Eixo Y".

#Entrada: La entrada contiene las coordenadas de un punto.

#Salida: La salida deberá mostrar en pantalla el cuadrante en el que se encuentra el punto.

#Ejemplo de entrada 4.5 -2.2
#Ejemplo de salida  Q4

x = float(input('ingrese valor de eje X ... : '))
y = float(input('ingrese valor de eje Y ... : '))
 
if x == 0 and y == 0:
    print(' el punto ingresado esta en el origen del plano cartesiano...')
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q2")
elif x < 0 and y > 0:
    print("Q4")
else:
    print(" uno de los ejes esta en eje como punto 0 ")
