#Lea un número entero entre 1 y 12, inclusive. Imprima el mes del año correspondiente a este número, 
# en inglés y con la primera letra en mayúscula.

#Entrada: La entrada contiene sólo un número entero.

#Salida: Imprimir el nombre del mes acorde al número de entrada, con la primera letra en mayúscula.

#Ejemplo de entrada	        4


#Ejemplo de salida          April

meses = ['enero', 'febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
numero = [1,2,3,4,5,6,7,8,9,10,11,12]

num = int(input('INGRESE EL numero del MES deseado :  '))
a = len(numero)
if num in numero:
    for aa in range(a):
        if numero[aa] == num:
            print(f' el  numero del mes ingresado es  {numero[aa]} corresponde el mes {meses[aa].capitalize()}')
else:
    print('MES NO INVALIDO...')
