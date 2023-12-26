#Leer dos valores enteros (A y B). Luego, el programa deberá imprimir el mensaje 
# "Sao Multiplos" (son múltiplos) o "Nao sao Multiplos" (no son múltiplos), dependiendo de los números leidos.

# Entrada: La entrada consta de dos números enteros.

# Salida: Imprimir el mensaje relativo a la entrada, tal como se indicó anteriormente.

#Ejemplo de entrada:    6 24
#Ejemplo de salida: Sao Multiplos


z = "s"
while z == "s" or z == "S":
    a = int(input('ingrese  1 ... : '))
    b = int(input('ingrese  2 ... : '))
    c = a % b
    print(f' el residuo entre {a} y {b} es   {c}')
    if c == 0 :
        print(f"entonces ,  {a} es multiplo de {b}")
    else:
        print (f" {a} NO es multiplo de {b} ")
    z = input(" desea continuar   S  /  N  :")
