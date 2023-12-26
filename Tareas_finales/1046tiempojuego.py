#Leer el tiempo de comienzo y el tiempo del final del juego, en horas. 
# Calcular la duración del juego, sabiendo que el juego comienza un día y finaliza al otro día, 
# con un máximo de duración de 24 horas. El mensaje deberá ser mostrado en portugues “O JOGO DUROU X HORA(S)” 
# que significa “EL JUEGO DURÓ X HORA(S)”

#Entrada: Dos número enteros representando el inicio y el final del tiempo de juego.

#Salida: Imprimir la duración del juego como en el ejemplo.

#Ejemplo de entrada     16 2
#Ejemplo de salida      O JOGO DUROU 10 HORA(S)


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
