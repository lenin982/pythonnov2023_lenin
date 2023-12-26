#Usando la siguiente tabla, escribe un programa que lea el código y la cantidad de un producto. 
# Luego, imprime el valor a pagar. 
# Este es un programa muy simple que tiene solo la intención de practicar los comandos de selección.

#code       specification       price
#   1       Cachorro Quente     R$ 4.00
#   2       X-salada            R$ 4.50
#   3       X-Bacon             R$ 5.00
#   4       Torrada simples     R$ 2.00
#   5       Refrigerante        R$ 1.50

#Entrada: El archivo de entrada contiene dos números enteros X e Y. 
# X es el código del producto e Y es la cantidad de ese artículo de acuerdo a la tabla anterior.

#Salida: La salida debe mostrar el mensaje "Total: R$ " seguido por el valor total a pagar, 
# con 2 dígitos después del punto decimal.

#Ejemplo de entrada	            3 2
#Ejemplo de salida       Total: R$ 10.00

producto_1 = "Cachorro Quente)" 
precio_1 = 4.00 
codigo_1 = 1001 

producto_2 = "X-salada" 
precio_2 = 4.50 
codigo_2 = 1002 

producto_3 = "X-Bacon)" 
precio_3 = 5.00 
codigo_3 = 1003 

producto_4 = "Torrada simples" 
precio_4 = 2.00 
codigo_4 = 1004 

producto_5 = "Refrigerante" 
precio_5 = 1.50 
codigo_5 = 1005 

m = "SI" 

while m == "SI" or m == "si": 

    cod = int(input('ingrese codigo del producto entre 1001 y 1005... :')) 

    if cod >= 1001 and cod <= 1005: 

        if cod == 1001: 

            cant = int(input('cantidad del producto a calcular ... ')) 

            pago = cant * precio_1 

            print(f'Total a Pagar por {cant}  unidades del {producto_1}  =  {pago}') 

        elif cod == 1002: 

            cant = int(input('cantidad del producto a calcular ... ')) 

            pago = cant * precio_2 

            print(f'Total a Pagar por {cant} unidades del {producto_2}  = {pago}') 

        elif cod == 1003: 

            cant = int(input('cantidad del producto a calcular ... ')) 

            pago = cant * precio_3 

            print(f'Total a Pagar por {cant} unidades del {producto_3} = {pago}') 

        elif cod == 1004: 

            cant = int(input('cantidad del product a calcular ... ')) 

            pago = cant * precio_4 

            print(f'Total a Pagar por {cant} unidades del {producto_4} = {pago}') 

        elif cod == 1005: 

            cant = int(input('cantidad del product a calcular ...')) 

            pago = cant * precio_5 

            print(f'Total a Pagar por {cant} unidades del {producto_5} = {pago}') 

    else: 

        print('vuelva a ingresar codigo, valor ingresado no es valido...!!!') 

    m = input('producto no existe desea continuar   ... SI / NO ') 

 