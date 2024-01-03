# Escriba un programa que lea 5 valores enteros. 
# Cuente cuantos de los valores son pares, impares, postivos y negativos. 
# Imprima la información siguiendo el ejemplo.

#Entrada: La entrada contiene 5 valores enteros.

#Salida: Imprima un mensaje siguiendo el ejemplo con todas las letras en minúscula, indicando cuantos de los valores son pares, impares, positivos y negativos.

#Ejemplo de entrada	
#       -5
#       0
#       -3
#       -4
#       12

#Ejemplo de salida          3 valor(es) par(es)


a = float(input('ingrrese numero :'))
b = float(input('ingrese  numero :'))
c = float(input('ingrrese numero :'))
d = float(input('ingrese  numero :'))
e = float(input('ingrrese numero :'))

acu = 0
acu1 = 0
acu2 = 0
acu3 = 0
lista = [a, b, c, d, e]
prom = 0

x = len(lista)
print(f' la lista de numeros ingresados es {lista}  y la longitud de la lista es {x}')
for i in range(x):
    if lista[i] % 2 == 0:
        acu += 1
    else:
        acu1 = acu1 + 1
    if lista[i] >  0:
        acu2 = acu2 + 1
    else:
        acu3 = acu3 + 1
    
    prom = prom + lista[i]
    
print(f'de los numeros de la lista son pares  {acu} y los impares son {acu1}')
print(f' los numeros positivos son {acu2} y los negativos son {acu3} ')