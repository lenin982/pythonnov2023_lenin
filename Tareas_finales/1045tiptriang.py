#Recibir 3 números double (A, B and C) que representan los lados de un triángulo y 
# ordenarlos de manera decreciente, de tal manera que el lado A sea el mas grande de los tres lados. 
# A continuación, determinar el tipo de triángulo que pueden formar, basado en los siguientes casos, 
# mostrando siempre el mensaje apropiado:

#si A ≥ B + C, mostrar el mensaje: NAO FORMA TRIANGULO
# si A2 = B2 + C2, mostrar el mensaje: TRIANGULO RETANGULO
# si A2 > B2 + C2, mostrar el mensaje: TRIANGULO OBTUSANGULO
# si A2 < B2 + C2, mostrar el mensaje: TRIANGULO ACUTANGULO
# si los tres lados son del mismo tamaño, mostrar el mensaje: TRIANGULO EQUILATERO
# si sólo dos lados son iguales y el tercero es diferente, mostrar el mensaje: TRIANGULO ISOSCELES

# Entrada: La entrada contiene tres números double, A (0 < A) , B (0 < B) y C (0 < C).

# Salida: Mostrar todas las clasificaciones del triángulo presentadas en la entrada.

#Ejemplos de Entrada    7.0 5.0 7.0
#Ejemplos de Salida     TRIANGULO ACUTANGULO
#                       TRIANGULO ISOSCELES


w = "S"
while w == 'S' or w == 's':
    x = float(input('ingrese lado A ... : '))
    y = float(input('ingrese lado B ... : '))
    z = float(input('ingrese lado C ... : '))
    if x > y and x > z and y > z:
        print(f" el mayor es  {x} el medio es {y} y el menor es {z}")
    else:
        if y > x and y > z and x > z:
            print(f" el mayor es  {y} el medio es {x} y el menor es {z}")
        else:
            if y > x and y > z and z > x:
                print(f" el mayor es  {y} el medio es {z} y el menor es {x}")
            else:        
                if z > x and z > y and y > x:
                    print(f" el mayor es  {z} el medio es {y} y el menor es {x}")
                else:
                    if  z > x and z > y and x > y:
                        print(f" el mayor es  {z} el medio es {x} y el menor es {y}")
                    else:
                        #if x > y and x > z and z > y:
                        print(f" el mayor es  {x} el medio es {z} y el menor es {y}")
    print(' numeros ingreso original  : ' , x ,"  " , y, "   " , z )
 
    if (x+y) > z:
        perimetro = x + y + z
        print('perimetro del triangulo es igual a : ' , perimetro)
    else:
        areaTrapecio = z*((x+y)/2)
        print(f'area del trapecio  =  {areaTrapecio:.1f}'.format(areaTrapecio))
    w = input(" desea continuar en el programa S o N   " )       
