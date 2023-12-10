#Calcular el consumo promedio de un coche cuando se conoce la distancia total recorrida (en km) y 
# el total de combustible gastado (en litros).

#Entrada: El archivo de entrada contiene dos valores: un valor entero X que representa 
# la distancia total (en km) y el segundo valor es un número punto flotante Y  que representa 
# el total de combustible gastado, con un dígito después del punto decimal.

#Salida: Imprimir un valor que representa el consumo promedio de un coche, con 3 dígitos después del punto decimal, 
# seguido por el mensaje "km/l".

#Ejemplo de entrada     500     35.0
#Ejemplo de salida      14.286 km/l


distancia = int(input())
litros = float(input())

formula = (distancia / litros)

formula = format(formula, ".3f")

print(str(formula) + " km/l")
