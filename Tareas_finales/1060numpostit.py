#Escriba un programa que lea 6 números. Estos números sólo serán positivos o negativos (ignorar valores nulos). Imprima la cantidad total de números positivos.

#Entrada: Seis números, positivos y/o negativos.

#Salida: Imprimir un mensaje con la cantidad total de números positivos.

#Ejemplo de entrada	
#               7
#               -5
#               6
#               -3.4
#               4.6
#               12

#Ejemplo de salida      4 valores positivos


a = float(input('ingrrese numero :'))
b = float(input('ingrese  numero :'))
c = float(input('ingrrese numero :'))
d = float(input('ingrese  numero :'))
e = float(input('ingrrese numero :'))
f = float(input('ingrese  numero :'))
acu = 0
acu1 = 0
lista = [a, b, c, d, e, f]

x = len(lista)
print(f' la lista de numeros ingresados es {lista}  y la longitud de la lista es {x}')
for i in range(x):
    if lista[i] > 0:
        acu += 1
    else:
        acu1 = acu1 + 1
    
print(f'de los numeros de la lista son positivos {acu} y negativos son {acu1}')