#Lea tres números enteros y ordénelos en orden ascendente. 
# Después, imprima estos valores en orden ascendente, una línea en blanco y 
# luego los valores en la secuencia tal como fueron leídos.

#Entrada: La entrada contiene tres números enteros.

#Salida: Presente la salida como se solicitó anteriormente.

#Ejemplo de entrada	7 21 -14
#Ejemplo de salida  -14
#                   7
#                   21

#                   7
#                   21
#                   -14




x = int(input('ingrese numero 1 ... : '))
y = int(input('ingrese numero 2 ... : '))
z = int(input('ingrese numero 3 ... : '))
 
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
 
 
 
"""
if x > y and x > z:
    mayor = x
    print('numero mayor : ' ,mayor)
else:    
    if y > x and y > z:
        mayor = y
        print('numero mayor : ' ,mayor)
    else:
        mayor = z
        print('numero mayor : ' ,mayor)
    if  y > z:
        medio = y
        print(' numeros ordenados         : ' , mayor , medio, x )
        print(' numeros ingreso original  : ' , x , y, z )
    else:
        medio = z
        print(' numeros ordenados         : ' , mayor , medio, y )
        print(' numeros ingreso original  : ' , x , y, z )
    '''"""
