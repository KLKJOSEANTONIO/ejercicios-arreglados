#datos
jugada=tuple
lista_jugadas = [(0,0,0)]
turno_nro_uno = str
turno_nro_dos = str
nro_jugada_tres = str
pos1=int
pos2=int
pos3=int
puntuacion = 0
nro_jugadas = 0
jugadas_calculadas = 0
puntuacion_total = ()
while True:
    turno_nro_uno = input("Introduzca numero bolos tirados en la primera tirada(ej:'3','X' para strike): " )
    try:
        turno_nro_uno = int(turno_nro_uno)
        turno_nro_dos = input("Introduzca los bolos tirados en el segundo intento(ej:'5', '/' para spare): ")
        try:
            turno_nro_dos = int(turno_nro_dos)
            nro_jugadas+=1
            puntuacion += turno_nro_uno+turno_nro_dos
            jugadas_calculadas +=1
            jugada = (turno_nro_uno,turno_nro_dos)
            puntuacion_total=(puntuacion,nro_jugadas,jugadas_calculadas)
            lista_jugadas[0]=puntuacion_total
            lista_jugadas.append(jugada)
            print(lista_jugadas)
        except ValueError:
            if turno_nro_dos == "/":
                pass
            else:
                print("Error, no es un valor valido...")
    except ValueError:
        if turno_nro_uno.upper() == "X":
            pass
        else:
            print("Error, no es un valor valido...")
    if nro_jugadas==10:
        exit()