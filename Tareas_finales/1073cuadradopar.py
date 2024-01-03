#Leer un entero N. Imprimir el cuadrado para cada uno de los valores pares desde 1 hasta N incluyendo N si es el caso.

#Entrada:   La entrada contiene un entero N (5 < N < 2000).

#Salida:    Imprimir el cuadrado de cada uno de los valores pares desde 1 hasta N, como en el ejemplo dado.

#Ten cuidado! Algunos lenguajes automaticamente imprime 1e+006 en lugar de 1000000. 
# Por favor configura tu programa para imprimir el formato correcta ajustando la precisión de la salida.

#Ejemplo de entrada	
#       6

#Ejemplo de salida
#       2^2 = 4
#       4^2 = 16
#       6^2 = 36

num1 = int(input('numeros a ingresar :'))
acu = 0
pot = 0
for i in range(num1):
    if i%2 == 1:
        pass
    else: 
        pot = i**2
        acu = acu + pot
        print(f'{i} a la potencia 2  = {pot}')