#Escribe un programa que lea un número de empleado, su número de horas trabajadas en el mes y el monto recibido por hora. 
# Imprimir el número de empleado y el salario que él/ella recibirá a fin de mes, con dos lugares decimales.

#No se olvide de imprimir los saltos de líneas después del resultado, de lo contrario, recibirá “Presentation Error”.
#No se olvide del espacio en blanco antes y después del signo igual y después de U$.

#Entrada: El archivo de entrada contiene 2 números enteros y 1 valor de punto flotante, representando el número, 
# cantidad de horas trabajadas y el monto recibido del empleado por hora trabajada.

#Output: Imprimir el número y salario del empleado, acorde al siguiente ejemplo, con los espacios en blanco antes y 
# después del signo igual.

#Ejemplos de Entrada    25 100 5.50
#Ejemplos de Salida     NUMBER = 25     SALARY = U$ 550.00

numero_de_empleado = int(input())
horas_trabajadas = int(input())
monto_por_hora = float (input())

SALARY = (horas_trabajadas * monto_por_hora)

SALARY = format(SALARY, '.2f')

print(f"NUMBER = {numero_de_empleado}\nSALARY = U$ " + str(SALARY))
