#Lea dos valores enteros X e Y. Imprima la suma de los valores impares entre ellos.

#Entrada: El archivo de entrada contiene dos valores enteros.

#Salida: El programa debe imprimir un número entero. 
# Este número es la suma de todos los valores impares entre los valores de entrada y esta suma es también un número entero.

#Ejemplos de Entrada	
#                       6
#                       -5
#Ejemplos de Salida     5

lista = []
num1 = int(input('Numero a ingresar :'))
num2 = int(input('Numero a ingresar :'))

acu = 0
for i in range((num1+1), (num2), 2):
    if (i) % 2 == 1:
        lista.append(i)
        print(lista , ' la I es = ', i )
        acu = acu + i
    
print(f'la suma de los imapres entre {num1} y {num2} = {acu}')