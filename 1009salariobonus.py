#Escriba un programa que lea el nombre de un vendedor, su salario fijo y el total de las ventas 
# realizadas por él en el mes (en dinero). Considerando que el vendedor recibe un 15% de los productos vendidos, 
# escribir el salario final (total) de cada vendedor a fin de mes, con dos cifras decimales.

#- No olvide de imprimir un final de linea luego del resultado, de otra forma recibirá “Presentation Error”.
#- No olvide los espacios en blanco.

#Entrada: La entrada contiene un texto (primer nombre del empleado), y dos valores de doble precisión, los cuales representan el salario del vendedor y el valor total vendido por él.

#Salida: Imprimir el salario total del vendedor, de acuerdo a los ejemplos.

#Ejemplo de entrada	    JOAO    500.00  1230.30
#Ejemplo de salida      TOTAL = R$ 684.54

numero_del_vendedor = input()
salario_fijo = float(input())
total_ventas = float (input())

COMISION = (total_ventas * 0.15)

COMISION_SALARIO = (COMISION + salario_fijo)

COMISION_SALARIO = format(COMISION_SALARIO, '.2f')

print(f"TOTAL = R$ {COMISION_SALARIO}")
