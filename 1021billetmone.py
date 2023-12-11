#Recibir un valor de punto flotante con dos números decimales. Este valor representa un valor monetario. 
# Luego de esto, calcular el menor numero posible de billetes y monedas en los cuales su valor puede ser descompuesto. 
# Los billetes a tener en cuenta son de 100, 50, 20, 10, 5, 2. Las monedas posibles son de 1, 0.50, 0.25, 0.10, 0.05 y 0.01. 
# Mostrar el mensaje "NOTAS:" seguido de una lista de billetes y el mensaje "MOEDAS:" seguido de una lista de monedas.

#Entrada: El archivo de entrada contiene un valor de punto flotante N (0 ≤ N ≤ 1000000.00).

#Salida: Mostrar la mínima cantidad de billetes y monedas necesarias para cambiar el valor inicial, como en el ejemplo dado.

#Ejemplos de Entradas:          576.73
#Ejemplos de Salidas:           NOTAS:
#                               5 nota(s) de R$ 100.00
#                               1 nota(s) de R$ 50.00
#                               1 nota(s) de R$ 20.00
#                               0 nota(s) de R$ 10.00
#                               1 nota(s) de R$ 5.00
#                               0 nota(s) de R$ 2.00
#                               MOEDAS:
#                               1 moeda(s) de R$ 1.00
#                               1 moeda(s) de R$ 0.50
#                               0 moeda(s) de R$ 0.25
#                               2 moeda(s) de R$ 0.10
#                               0 moeda(s) de R$ 0.05
#                               3 moeda(s) de R$ 0.01

NOTAS = float(input(),2)

cuantosde100 = (NOTAS//100)
NOTAS =  (NOTAS%100)
cuantosde50 = (NOTAS//50)
NOTAS =  (NOTAS%50)
cuantosde20 = (NOTAS//20)
NOTAS =  (NOTAS%20)
cuantosde10 = (NOTAS//10)
NOTAS =  (NOTAS%10)
cuantosde5 = (NOTAS//5)
NOTAS =  (NOTAS%5)
cuantosde2 = (NOTAS//2)
NOTAS =  (NOTAS%2)

cuantosde1 = (NOTAS//1)
NOTAS =  (NOTAS%100)
cuantosde0_50 = (MOEDAS//50)
MOEDAS =  (MOEDAS%50)
cuantosde0_25 = (MOEDAS//20)
MOEDAS =  (MOEDAS%20)
cuantosde0_10 = (MOEDAS//10)
MOEDAS =  (MOEDAS%10)
cuantosde0_05 = (MOEDAS//5)
MOEDAS =  (MOEDAS%5)
cuantosde0_01 = (MOEDAS//2)
MOEDAS =  (MOEDAS%2)

cuantosde1 = (cantidad//1)
cantidad =  (cantidad%1)

print (NOTAS)
print(cuantosde100, "nota(s) de R$ 100,00")
print(cuantosde50, "nota(s) de R$ 50,00")
print(cuantosde20, "nota(s) de R$ 20,00")
print(cuantosde10, "nota(s) de R$ 10,00")
print(cuantosde5, "nota(s) de R$ 5,00")
print(cuantosde2, "nota(s) de R$ 2,00")


print (MOEDAS)
print(cuantosde100, "moeda(s) de R$ 1.00")
print(cuantosde50, "moeda(s) de R$ 0.50")
print(cuantosde20, "moeda(s) de R$ 0.25")
print(cuantosde10, "moeda(s) de R$ 0.10")
print(cuantosde5, "moeda(s) de R$ 0.05")
print(cuantosde2, "moeda(s) de R$ 0.01")
