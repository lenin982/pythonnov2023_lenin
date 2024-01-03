#Leer un entero N. Este N será el número de números enteros X que serán leídos.

#Mostrar cuantos de estos números X están dentro del intervalo [10,20] y cuantos están fuera de este intervalo.

#Entrada:   La primera línea de entrada es un entero N (N < 10000), que indica el número total de casos de prueba.
# Cada caso es un número entero X (-107 < X < 107).

#Salida:    Para cada caso, imprimir cuantos números están dentro y cuantos valores están fuera del intervalo.

#Ejemplo de entrada	
#       4
#       14
#       123
#       10
#       -25

#Ejemplo de salida
#       2 in
#       2 out

listaIN = []
listaOUT = []
listaTOT = []
num1 = int(input('cantidad de numeros a ingresar :'))
acu = 0
acu1 = 0
for i in range(num1):
    num2 = int(input(f'numeros a ingresar {i}  :'))
    if num2 < 10 or num2 >20 : 
        listaIN.append(num2)
        acu = acu + 1
        
    else :
        listaOUT.append(num2)
        acu1 = acu1 + 1
    listaTOT.append(num2)    
print(listaIN , f' son los numeros FUERA del rango (10 a 20)   {acu1} \n')    
print(listaOUT , f' son los numeros DENTRO del rango (10 a 20)   {acu} \n')
print(f'los numeros ingresados son  {listaIN} + {listaOUT}\n')
print(f'los numeros ingresados son  {listaTOT}')
