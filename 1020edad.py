#Leer un entero, que corresponde a la edad de una persona (en días) e imprimirlo en años, meses y días, 
# seguido del respectivo mensaje “ano(s)”, “mes(es)”, “dia(s)”.

#Nota: Para facilitar el cálculo, considere al año con 365 días y al mes con 30. 
# En los casos de prueba nunca habrá una situacion que permita 12 meses y algunos días, como 360, 363 ó 364. 
# Este es sólo un ejercicio para plantear un simple razonamiento matemático.

#Entrada: La entrada consiste en un solo valor entero.

#Salida: Mostrar el resultado, como se muestra a continuación.

#Ejemplo Entradas:      400
#Ejemplo Salidas:       1 ano(s)
#                       1 mes(es)
#                       5 dia(s)

edad = int(input())

año = (edad//365)
edad = (edad%365)

mes = (edad//30)
edad = (edad%30)

dia = (edad//1)
edad = (edad%1)

print(año," ano(s)")
print(mes, " mes(es)")
print(dia, " dia(s)")
