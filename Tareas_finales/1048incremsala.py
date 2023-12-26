#URI Online Judge | 1048    Incremento Salarial     Por Neilor Tonin, URI  Brasil

#Timelimit: 1   La empresa ABC decidió dar un aumento salarial a sus empleados, según la siguiente tabla:

#Salario	            Porcentaje de Reajuste
#0 - 400.00              15%
#400.01 - 800.00         12%
#800.01 - 1200.00        10%
#1200.01 - 2000.00       7%
#Por encima de 2000.00   4%

#Lea el salario del empleado, calcule e imprima el nuevo salario del empleado, 
# así como el dinero ganado y el porcentaje de aumento obtenido por el empleado, 
# con los mensajes correspondientes en portugués, como se muestra a continuación.

#Entrada:   la entrada contiene un solo número de punto flotante, con 2 dígitos luego del punto decimal.

#Salida:    Imprimir 3 mensajes seguidos por el número correspondiente (ver ejemplo) informando el nuevo salario, el dinero extra (ambos deben mostrarse con dos cifras decimales) y el porcentaje obtenido por el empleado. Nota:
#Novo salario:  que significa "Nuevo salario"
#Reajuste ganho: que significa "Dinero ganado"
#Em percentual: que significa "En porcentaje"

#Ejemplo de entrada:        400.00
#Ejemplo de salida          Novo salario: 460.00
#                           Reajuste ganho: 60.00
#                           Em percentual: 15 %

z = "s"
while z == "s" or z == "S":
    sueldo = float(input('ingrese sueldo del empleado : '))
    if sueldo >= 0 and sueldo <= 400:
        aumento = sueldo * 0.15
        salario = sueldo + aumento
    elif sueldo > 400 and sueldo <= 800:
        aumento = sueldo * 0.12
        salario = sueldo + aumento
    elif sueldo > 800 and sueldo < 1200:
        aumento = sueldo * 0.1
        salario = sueldo + aumento
    elif sueldo >= 1200 and sueldo < 2000:
        aumento = sueldo * 0.07
        salario = sueldo + aumento
    else:
        aumento = sueldo * 0.04
        salario = sueldo + aumento
    
    print(f'nuevo salario   : {salario}')
    print(f'reajuste ganado : {aumento}')
    print(f'el porcentaje es: {aumento/sueldo}')   
    z = input(' desea continuar con otro sueldo '   )
      
