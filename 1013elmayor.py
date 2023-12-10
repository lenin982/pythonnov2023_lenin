#Hacer un programa que lea 3 valores enteros y presente el mas grande seguido del mensaje "eh o maior". Usando la siguiente fórmula.

#Entrada: El archivo de entrada contiene 3 valores enteros.

#Salida: Imprimir el mas grande de los 3 valores seguido por un espacio y el mensaje "eh o maior".

#Ejemplos de Entrada    7   14  106
#Ejemplos de Salida      106 eh o maior

formula = input() .split()
a = int(formula[0])
b = int(formula[1])
c = int(formula[2])


MAIOR_AB = max(a, b, c)
print(str(MAIOR_AB) + " eh o maior")

