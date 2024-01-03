#En un país imaginario llamado Lisarb, toda la gente está muy feliz de pagar sus impuestos 
# porque saben que no existen políticos corruptos y los impuestos se utilizan para beneficiar a la población, 
# sin ninguna apropiación indebida. La moneda de este país es el Rombus, cuyo símbolo es R$.

#Lea un valor con 2 dígitos después del punto decimal, equivalente al salario de un habitante de Lisarb. Luego imprima el valor que esta persona debe pagar de impuestos, de acuerdo con la siguiente tabla.

#Recuerde, si el salario es de R$ 3,002.00 por ejemplo, la tasa del 8% es sólo sobre R$ 1.000,00, porque el salario de R$ 0,00 a R$ 2,000.00 es libre de impuestos. En el siguiente ejemplo, la tasa total es de 8% sobre R$ 1000,00 + 18% sobre R$ 2,00, resultando R$ 80,36. La respuesta debe imprimirse con 2 dígitos después del punto decimal.

#Entrada: La entrada contiene sólo un número de punto flotante, con 2 dígitos después del punto decimal.

#Salida: Imprima el mensaje "R$" seguido de un espacio en blanco y el impuesto total a pagar, con dos dígitos después del punto decimal. Si el valor es hasta 2000, imprima el mensaje "Isento".

#Ejemplos de Entrada	3002.00

# Outputs Samples       R$ 80.36


z = "s"
while z == "s" or z == "S":
    sueldo = float(input('ingrese sueldo del empleado : '))
    if sueldo >= 0 and sueldo <=2000:
        print('Sueldo ingresado no paga impuestos ') 
        impuesto = 0
    elif sueldo > 2000 and sueldo <= 3000:
        impuesto = (sueldo - 2000) * 0.08
        
    elif sueldo > 3000 and sueldo <= 4500:
        impuesto = (sueldo - 2000) * 0.18
        
    else:
        impuesto = (sueldo - 2000) * 0.28
        
    print(f'salario         : {sueldo}')
    print(f'impuesto        : {impuesto:.2f}')
    z = input(' desea continuar con otro sueldo '   )
      
