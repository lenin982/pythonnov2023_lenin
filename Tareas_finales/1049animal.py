#En este problema, su trabajo es leer tres palabras en portugués. 
# Estas palabras definen un animal de acuerdo con la siguiente tabla, de izquierda a derecha. 
# Después, imprima el animal elegido definido por estas tres palabras.



#Entrada:   La entrada contiene 3 palabras, una por línea, que se utilizará para identificar al animal, de acuerdo con la tabla anterior, con todas las letras en minúsculas.

#Salida:    Imprima el nombre del animal de acuerdo con la entrada dada.

#Ejemplo de entrada	    vertebrado
#                       mamifero
#                       onivoro
#Ejemplo de salida   homem

lista1 = ['VERTEBRADO', 'INVERTEBRADO']
lista2 = ['AVE' , 'MAMIFERO', 'INSECTO', 'ANELIDEO']
lista3 = ['CARNIVORO' ,'OMNIVORO', 'HERBIVORO' ,'HEMATOFAGO']
resultado = ['AGUILA', 'POMBA', 'HOMEN', 'VACA','PULGA', 'LAGARTA', 'SANGUIJUELA', 'MINHOCA']
acu = 0
z = "s"
while z == "s" or z == "S":
    print(f"elija la primera clasificacion de animales --->{lista1}<---")
    clase1 = input('ingrese su seleccion : ')
    print(f"elija la segunda clasificacion de animales --->{lista2}<---")
    clase2 = input('ingrese su seleccion : ')
    print(f"elija la tercera clasificacion de animales --->{lista3}<---")
    clase3 = input('ingrese su seleccion : ')
   
    variables = [clase1.upper(), clase2.upper(), clase3.upper()]
    print(f' sus selecciones han sido  : -----> {variables} <----')   
    
    if clase1.upper() == lista1[0] and clase2.upper() == lista2[0] and clase3.upper() == lista3[0]:
        print(f"el animal resultante es {resultado[0]}")
    elif clase1.upper() == lista1[0] and clase2.upper() == lista2[0] and clase3.upper() == lista3[1]:
        print(f"el animal resultante es {resultado[1]}")
    elif clase1.upper() == lista1[0] and clase2.upper() == lista2[1] and clase3.upper() == lista3[1]:
        print(f"el animal resultante es {resultado[2]}")     
    elif clase1.upper() == lista1[0] and clase2.upper() == lista2[1] and clase3.upper() == lista3[2]:
        print(f"el animal resultante es {resultado[3]}")
    elif clase1.upper() == lista1[1] and clase2.upper() == lista2[2] and clase3.upper() == lista3[3]:
        print(f"el animal resultante es {resultado[4]}")
    elif clase1.upper() == lista1[1] and clase2.upper() == lista2[2] and clase3.upper() == lista3[2]:
        print(f"el animal resultante es {resultado[5]}")    
    elif clase1.upper() == lista1[1] and clase2.upper() == lista2[3] and clase3.upper() == lista3[3]:
        print(f"el animal resultante es {resultado[6]}")        
    elif clase1.upper() == lista1[1] and clase2.upper() == lista2[3] and clase3.upper() == lista3[1]:
        print(f"el animal resultante es {resultado[7]}")      
    else:
        print("no hay respuesta para su seleccion..."   )               
    z = input(' desea continuar con otra clasificacion de animales S / N '   )