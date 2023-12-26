#Leer cuatro números (N1, N2, N3, N4), con 1 dígito después del punto decimal, 
# correspondiente a 4 resultados obtenidos por un estudiante. Calcular el promedio con pesos 2, 3, 4 e 1 respectivamente, 
# para estos 4 resultados e imprimir el mensaje "Media: " (Promedio), segudio por el cálculo obtenido. 
# Si el promedio es de 7.0 o más, imprimir el mensaje "Aluno aprovado." (Estudiante Aprobado). 
# Si el promedio es menor que 5.0, imprimir el mensaje: "Aluno reprovado." (Estudiante Reprobado). 
# Si el promedio es entre 5.0 and 6.9, incluyendo este, el programa deberá imprimir el mensaje "Aluno em exame." (Estudiante en examén).

#En caso de examen, lea una puntuación más. Imprimir el mensaje "Nota do exame: " 
# (Nota de examen) seguido por la puntuación mostrada. Vuelva a calcular el promedio 
# (suma la puntuación del examen con el promedio calculado anteriormente y divida por 2) e 
# imprima el siguiente mensaje “Aluno aprovado.” (Estudiante Aprobado) 
# en caso de que el promedio sea 5.0 o más o "Aluno reprovado." (Estudiante Reprobado) 
# en caso de que el promedio sea 4.9 o menor. Para estos 2 casos (Aprobado o reprobado después del examen) 
# imprimir el mensaje "Media final: " (Promedio Final) Seguido por el promedio final para este estudiante en la última línea.

#Entrada: La entrada contiene cuatro números flotante que representan las calificaciones de los estudiantes.

#Salida: Imprimir todas las respuestas con un dígito después del punto decimal.

#Ejemplo de entrada	    2.0 4.0 7.5 8.0 6.4
#Ejemplo de salida      Media: 5.4
#                       Aluno em exame.
#                       Nota do exame: 6.4
#                       Aluno aprovado.
#                       Media final: 5.9



m = "SI"
while m == "SI" or m == "si":
    n1 = float(input('ingrese nota 1 ... : '))
    if n1 >=0 and n1 <= 10:
        n2 = float(input('ingrese nota 2 ... : '))
        if n2 >= 0 and n2 <= 10:
            n3 = float(input('ingrese nota 3 ... : '))
            if n3 >= 0 and n3 <= 10:
                n4 = float(input('ingrese nota 4 ... : '))
            else:
                print("Invalida, nota esta fuera del rango   ...")
        else:
            print("Invalida, nota esta fuera del rango   ...")
    else:
        print("Invalida, nota esta fuera del rango   ...")
    
    n11 = float("{0:.1f}".format(n1))
    n22 = float("{0:.1f}".format(n2))
    n33 = float("{0:.1f}".format(n3))
    n44 = float("{0:.1f}".format(n4))
    prom = (n11*2 + n22*3 + n33*4 + n44)/10
    print(" promedio de las notas obtenidas   = " , prom)
    if prom >= 7:
        print(" ALUMNO APROBADO ...")
    elif prom >= 5 and prom < 7:
        print(" ALUMNO SUPLETORIO ...")
        n5 = float(input('ingrese nota supletorio ... : '))
        n55 = float("{0:.1f}".format(n5))
        nuevoprom = (prom + n55)/2
        if nuevoprom >= 5:
            print(f"ALUMNO APROBADO nota del supletorio  =  {n55} y el promedio es {nuevoprom} ")
        else:  
            print(" ALUMNO REPROBADO ...", nuevoprom)
    elif prom < 5:
        print(" ALUMNO REPROBADO ...")
        
    m = input('desea continuar ingresar mas notas   ... SI / NO :')
