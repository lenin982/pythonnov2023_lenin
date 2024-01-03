# Lea un número entero que corresponda al número de código de área para marcación telefónica. 
# A continuación, imprima el destino de acuerdo con la siguiente tabla:

#      DDD          DESTINATION
#       61          Brasilia
#       71          Salvador
#       11          Sao Paulo
#       21          Rio de Janeiro
#       32          Juiz de Fora
#       19          Campinas
#       27          Victoria
#       31          Belo Horizonte


#Si el número de entrada no se encuentra en la tabla anterior, la salida debe ser:
#DDD nao cadastrado
#Que significa “DDD no encontrado” in Portugues.

#Entrada: La entrada consiste en un único número entero.

#Salida: Imprima el nombre de la ciudad correspondiente a la entrada DDD. Imprimir DDD nao cadastrado si no existe DDD correspondiente al número ingresado.

#Ejemplo de entrada	    11
#Ejemplo de salida      Sao Paulo

ddd = [61,71,11,21,32,19,27,31]
destino = ['Brasilia' , 'Salvador', 'Sao Paolo', 'Rio de Janeiro','Juiz de Fora', 'Campinas' ,'Victoria','Belo Horionte']

num = int(input('Ingrese el DDD deseado :  '))
a = len(ddd)
if num in ddd:
    for aa in range(a):
        if ddd[aa] == num:
            print(f' codigo DDD {ddd[aa]} corresponde destino {destino[aa]}')
else:
    print('codigo DDD INVALIDO...')