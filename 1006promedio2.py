#Leer tres valores (variables A, B y C), que son las tres notas de estudiantes. 
# Entonces, calcule el promedio, considerando que la nota A tiene peso 2, la nota B tiene peso 3 y la nota C tiene peso 5. 
# Cosiderar que cada nota puede ser del 0 al 10.0, siempre con un punto decimal.

#Entrada
#El archivo de entrada contiene 3 valores de punto flotante (double) con un dígito decimal después de la coma.

#Salida
#Imprime el mensaje "MEDIA"(Promedio en Portugués) y el promedio de los estudiantes de acuerdo con el siguiente ejemplo, 
# con un espacio en blanco antes y después del signo igual.


nota_A = float (input())
nota_B = float (input())
nota_C = float (input())

sumatoria = (nota_A * 2) + (nota_B * 3) + (nota_C * 5)

MEDIA = ((sumatoria) / (10))

MEDIA= format(MEDIA, '.1f')  

print('MEDIA = ' + str(MEDIA))
