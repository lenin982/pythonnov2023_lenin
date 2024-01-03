#Leer una valor entero X e imprimir los 6 números impares consecutivos desde X, un valor por línea, incluyendo X si es el caso.

#Entrada: La entrada tendrá un valor entero positivo.

#Salida: La salida tendrá una salida de seis números impares consecutivos.

#Ejemplo de entrada	    8
#Ejemplo de salida      9

lista = []
num = int(input('Numero a ingresar :'))
acu = 0
for i in range(12):
    if num % 2 == 1:
        lista.append(num)
        acu = acu + 1
    num = num + 1
   

print(f'numeros siguientes imares son ..... {lista}')