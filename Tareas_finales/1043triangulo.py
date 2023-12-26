#Lea 3 números del tipo punto flotante (A, B y C) y verifique si es posible realizar un triángulo con ellos. 
# Si esto es posible, calcular el perímetro del triángulo y mostrar el siguiente mensaje:


#Perimetro = XX.X
# Si esto no es posible, calcular el área de un trapecio, cuyas bases son A, B y su altura es C, y mostrar el siguiente mensaje:
# Area = XX.X
#
# Entrada: El archivo de entrada contiene tres valores del tipo punto flotante.
# Salida: Imprima el resultado con un dígito luego del punto decimal.

#Ejemplo de entrada     6.0 4.0 2.0
#Ejemplo de salida      Area = 10.0

z = "S"
while z == 'S' or z == 's':
    a = float(input('ingrese numero 1 ... : '))
    b = float(input('ingrese numero 2 ... : '))
    c = float(input('ingrese numero 3 ... : '))
    if (a+b) > c:
        perimetro = a + b + c
        print('perimetro del triangulo es igual a : ' , perimetro)
    else:
        areaTrapecio = c*((a+b)/2)
        print(f'area del trapecio  =  {areaTrapecio:.1f}'.format(areaTrapecio))
    z = input(" desea continuar en el programa S o N   " )       
