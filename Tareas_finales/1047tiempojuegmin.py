#Leer la hora de inicio y final de un juego, en horas y minutos (hora inicial, 
# minuto inicial, hora final, minuto final). Luego mostrar la duración del juego, 
# sabiendo que el juego puede comenzar en un día y terminar en el siguiente.

#Obs.: El tiempo máximo de juego es de 24 horas y el tiempo mínimo es de 1 minuto.

#Entrada: Cuatro números enteros que representan hora de inicio y final del juego.

#Salida: Mostrar la duración del juego en horas y minutos, 
# en este formato: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” . 
# Esto significa: El juego duró XXX hora(s) y YYY minuto(s).

#Ejemplos de Entrada	7 8 9 10
#Ejemplos de Salida     O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)

t1 = int(input('hora de inicio del juego      (horas de 0 a 23)  : '))
m1 = int(input('minutos de inicio del juego  (minutos de 0 a 59) : '))
t2 = int(input('hora de final del juego       (horas de 0 a 23)  : '))
m2 = int(input('minutos de final del juego   (minutos de 0 a 59) : '))
acu_min = 0
acu_hrs = 0
minutos1 = 0
horas = 0
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
print(f' ------>>>>   el juego DURO  {horas} horas  y {minutos} minutos ')   
