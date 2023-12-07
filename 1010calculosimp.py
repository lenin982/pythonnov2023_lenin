#En este problema, la tarea consiste en leer un código de un producto 1, 
# el número de unidades del producto 1, el precio de una unidad de producto 1, 
# el código de un producto 2, el número de unidades del producto 2 y el precio de una unidad de producto 2. 
# Después de esto, calcular y mostrar la cantidad a pagar.

#Entrada: El archivo de entrada contiene dos líneas de datos. En cada línea habrá 3 valores: 
# Dos enteros y un valor flotante con 2 dígitos después del punto decimal.

#Salida: El archivo de salida debe ser un mensaje como en el siguiente ejemplo. 
# Recuerde el espacio antes de ":" y antes del símbolo "R$". El valor debe ser presentado con 2 dígitos después del punto.

#Ejemplos de Entrada:   12  1   5.30
#                       16  2   5.10
#Ejemplos de Salida:    VALOR A PAGAR: R$ 15.50

VALOR_1 = input().split()
a = int(VALOR_1[0])
b = int(VALOR_1[1])
c = float(VALOR_1[2])

prod_valor_1 = (b * c)

VALOR_2 = input().split()
d = int(VALOR_2[0])
e = int(VALOR_2[1])
f = float(VALOR_2[2])

prod_valor_2 = (e * f)

suma_valores = (prod_valor_1 + prod_valor_2)

#suma_valores = format(suma_valores, ':2f')

print('VALOR A PAGAR: R$ {suma_valores:2f}")
