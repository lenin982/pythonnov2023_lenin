#Leer un valor entero, que es la duración en segundos de un evento realizado en una fábrica, 
# e informarlo expresado en horas:minutos:segundos.

#Entrada: El archivo de entrada contiene al entero N.

#Output: Imprimir el tiempo leído del archivo de entrada (segundos) convertido en horas:minutos:segundos como el ejemplo siguiente.

#Ejemplos de Entrada:       556
#Ejemplos de Salida:        0:9:16

segundos_in = int(input())

hora = (segundos_in//3600)
segundos_in = (segundos_in%3600)
minuto = (segundos_in//60)
segundos_in = segundos_in%60
segundo = (segundos_in//1)

print(f"{hora}:{minuto}:{segundo}")
