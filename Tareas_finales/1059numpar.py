#Escriba un programa que imprima todos los números pares entre 1 y 100, incluir los extremos si corresponde.

#Entrada: En este problema, extremadamente simple, no hay entrada.

#Salida: Imprima todos los números pares entre 1 y 100, incluidos los extremos, uno por linea.

#Ejemplo de entrada	

#Ejemplo de salida      2
#                       4
#                       6
#                       ...
#                       100

pares = []

for i in range(101):
    par = i % 2
    if par == 0:
        pares.append(i)

print(pares)
