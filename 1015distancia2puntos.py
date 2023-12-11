#Leer los cuatro valores correspondientes a las coordenadas x e y de dos puntos en el plano, 
# p1 (x1, y1) y p2 (x2, y2) y calcular la distancia entre ellos, mostrando cuatro decimales después del punto, 
# de acuerdo a la fórmula:
#Distancia = raiz de (x2 - x1)**2 + (y2 - y1)**2

#Entrada: La entrada contiene dos líneas de datos, la primera contiene dos valores double: x1 y1, 
# la segunda también contiene dos valores double con un dígito después del punto: x2 y2.

#Salida: Calcular y mostrar el valor de la distancia usando la fórmula provista, con 4 dígitos después del punto.

#Ejemplos de Entrada    1.0     7.0
#                       5.0     9.0
#Ejemplos de Salida     4.4721


coordenada_x = input() .split()
x1 = float(coordenada_x[0])
x2 = float(coordenada_x[1])

coordenada_y = input() .split()
y1 = float(coordenada_y[0])
y2 = float(coordenada_y[1])

distancia = (((x2 - x1)**2) + ((y2 - y1)**2))

distancia_raiz = format((distancia)**0.5, '4f')

print=(distancia_raiz)
