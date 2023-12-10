#Haga un programa que calcule y muestre el volumen de una esfera mediante un radio (R) dado. 
#La fórmula para calcular dicho volumen es: (4/3) * pi * R3. Considere asignar a Pi el valor: 3.14159.

#Tip: Use (4/3.0) ó (4.0/3) en su fórmula, algunos lenguajes (incluyendo C++) asumen que la división entre dos enteros es otro entero. :)

#Entrada: La entrada consiste de un valor entero.

#Salida: La salida será el mensaje "VOLUME" como en el siguiente ejempo con un espacio antes y luego del igual. El valor debe ser presentado con 3 dígitos decimales.

#Ejemplos Entrada:	     3
#Ejemplos Salida:        VOLUME = 113.097

R = int(input())

pi = float(3.14159)

fraccion = (4/3.0)

Vol = (fraccion * pi * R**3)

DIFERENCA= format(DIFERENCA, '.0f')
