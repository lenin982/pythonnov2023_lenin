#Leer un valor entero X (1 <= X <= 1000).  Entonces imprima los números impares del 1 hasta X, 
# cada uno en una línea, incluyendo X si es el caso.

#Entrada: La entrada tendrá un valor entero.

#Salida: Imprimir todos los valores impares entre 1 y X, incluyendo X si es el caso.

#Ejemplo de entrada     8
#Ejemplo de salida      1


impares = []

for i in range(1001):
    par = i % 2
    if par == 1:
        impares.append(i)

print(impares)

