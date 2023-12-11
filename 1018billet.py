##En este problema tienes que leer un valor entero y calcular el menor número posible de billetes 
# en que puede ser descompuesto. Los billetes posibles son 100, 50, 20, 10, 5, 2 y 1. 
# Imprimir el valor leído y la lista de billetes.

#Entrada: La entrada contiene un valor entero N (0 < N < 1000000).

#Salida: Imprimir el número leído y la cantidad mínima necesaria de billetes en lenguaje portugués, como muestra el ejemplo. 
# No olvides imprimir el final de línea luego de cada línea, de otra forma recibirás “Presentation Error”.

#Ejemplo de entrada:    576
#Ejemplo de salida:     576
#                       5 nota(s) de R$ 100,00
#                       1 nota(s) de R$ 50,00
#                       1 nota(s) de R$ 20,00
#                       0 nota(s) de R$ 10,00
#                       1 nota(s) de R$ 5,00
#                       0 nota(s) de R$ 2,00
#                       1 nota(s) de R$ 1,00

cantidad = int(input())

cuantosde100 = (cantidad//100)
cantidad =  (cantidad%100)
cuantosde50 = (cantidad//50)
cantidad =  (cantidad%50)
cuantosde20 = (cantidad//20)
cantidad =  (cantidad%20)
cuantosde10 = (cantidad//10)
cantidad =  (cantidad%10)
cuantosde5 = (cantidad//5)
cantidad =  (cantidad%5)
cuantosde2 = (cantidad//2)
cantidad =  (cantidad%2)
cuantosde1 = (cantidad//1)
cantidad =  (cantidad%1)

print (cantidad)
print(cuantosde100, "nota(s) de R$ 100,00")
print(cuantosde50, "nota(s) de R$ 50,00")
print(cuantosde20, "nota(s) de R$ 20,00")
print(cuantosde10, "nota(s) de R$ 10,00")
print(cuantosde5, "nota(s) de R$ 5,00")
print(cuantosde2, "nota(s) de R$ 2,00")
print(cuantosde1, "nota(s) de R$ 1,00")
