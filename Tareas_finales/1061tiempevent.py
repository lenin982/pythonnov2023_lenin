#Pedro está organizando un evento en su Universidad. El evento será en el mes de abril, 
# comenzando y terminando en dicho mes. El problema es: Pedro quiere calcular la duración del evento en segundos, 
# sabiendo obviamente el comienzo y el final del mismo.

#Sabes que el evento puede durar de unos pocos segundos a algunos días, 
# así que debes ayudar a Pedro a calcular el tiempo total correspondiente a la duración del evento.

#Entrada: La primera línea de la entrada contiene información sobre el día de inicio del evento en el formato "Dia xx". La siguiente línea contiene la hora de inicio del evento en el formato presentado en la entrada de muestra. Luego, 2 líneas de entrada con el mismo formato, correspondientes al final del evento.

#Salida: Su programa debe imprimir la siguiente salida, una información por línea, 
# considerando que si cualquier información es nula por ejemplo, el número 0 debe imprimirse en lugar de W, X, Y o Z:

#W dia(s)
#X hora(s)
#Y minuto(s)
#Z segundo(s)

#Obs: Considere que el evento del caso de prueba tiene duración mínima de un minuto.

#Ejemplo de entrada	
#Dia 5
#08 : 12 : 23
#Dia 9
#06 : 13 : 23

#Ejemplo de salida         3 dia(s)

d1 = int(input('ingrese dia de inicio del evento    (1 a 31 dias de abril) :)'))
t1 = int(input('hora de inicio del juego    (horas de 0 a 23)  : '))
m1 = int(input('minutos de inicio del juego     (minutos de 0 a 59) : '))
d2 = int(input('ingrese dia de fin del evento   (1 a 31 dias de abril):)'))
t2 = int(input('hora de final del juego     (horas de 0 a 23)  : '))
m2 = int(input('minutos de final del juego  (minutos de 0 a 59) : '))
acu_min = 0
acu_hrs = 0
minutos1 = 0
horas = 0
dias = d2 - d1
if t2 > t1:
    horas = t2 - t1
    if m2 >  m1:
        minutos = m2 - m1
    else:
        minutos = 60-(m1-m2)
        if minutos == 60:
            minutos = 0
else:
    horas = (24 + t2) - t1
    if m2 >=  m1:
        minutos = m2 - m1
    else:
        minutos = 60-(m1-m2)
        horas = horas -1

segundos_minutos = minutos * 60
horas_minutos = segundos_minutos * 60
segundos_dias = horas_minutos * dias * 24
print(f' ------>>>>   el juego DURO  un total de {segundos_dias} segundos   ')   