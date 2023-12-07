#Escriba un programa que lea tres valores de punto flotante: A, B y C. Luego, calcular y mostrar:
#a) El área del triángulo rectángulo de base A y altura C.
#b) El área del círculo de radio C (Pi = 3.14159).
#c) El área del trapecio el cual tiene A y B como bases, y C como altura.
#d) El área del cuadrado de lado B.
#e) El área del rectángulo de lados A y B.

#Entrada: La entrada contiene tres valores de doble precisión con un dígito luego del punto decimal.

#Salida: La salida contiene 5 renglones. Cada uno de los renglones corresponde a las áreas descriptas anteriormente, siempre con el mensaje correspondiente (en portugués) y un espacio entre los dos puntos y el valor. El valor calculado debe ser presentado con 3 dígitos luego del punto decimal.

#Ejemplo de entrada 3.0 4.0 5.2

#Ejemplo de salida  TRIANGULO: 7.800 CIRCULO: 84.949 TRAPEZIO: 18.200 QUADRADO: 16.000 RETANGULO: 12.000

valor_A = float(input())
valor_B = float(input())
valor_C = float(input())

pi = float(3.14159)

area_triangulo_rect = format((1/2) * valor_A * valor_C, '.3f')
area_circulo = format(2 * pi * valor_C, '.3f')
area_trapecio = format((((valor_A + valor_B) * valor_C) / 2), '.3f')
area_cuadrado = format((valor_B * 4), '.3f')
area_rectangulo = format((valor_A + valor_B) * 2, '.3f')

print(f"TRIANGULO: {area_triangulo_rect}\nCIRCULO:{area_circulo}\nTRAPEZIO: {area_trapecio}\nCUADRADO: {area_triangulo_rect}\nRECTANGULO: {area_rectangulo}")
