#Lea 6 valores que son números de punto flotante. Después, imprima cuantos de ellos fueron positivos. 
# En la siguiente línea, imprima el promedio de todos los valores positivos ingresados, con un dígito después del punto decimal.

#Entrada: La entrada consiste en 6 números que pueden ser enteros o de punto flotante

#Output: El primer valor de salida es la cantidad de números positivos. La siguiente línea debe mostrar el promedio de los valores positivos ingresados.

#Ejemplo de entrada	
#       7
#       -5
#       6
#       -3.4
#       4.6
#       12

#Ejemplo de salida       4 valores positivos



a = float(input('ingrrese numero :'))
b = float(input('ingrese  numero :'))
c = float(input('ingrrese numero :'))
d = float(input('ingrese  numero :'))
e = float(input('ingrrese numero :'))
f = float(input('ingrese  numero :'))
acu = 0
acu1 = 0
lista = [a, b, c, d, e, f]
prom = 0

x = len(lista)
print(f' la lista de numeros ingresados es {lista}  y la longitud de la lista es {x}')
for i in range(x):
    if lista[i] > 0:
        acu += 1
    else:
        acu1 = acu1 + 1
    prom = prom + lista[i]
    
print(f'de los numeros de la lista son positivos {acu} y negativos son {acu1}')
print(f' el promedio de los numeros ingresados es {prom/i}')