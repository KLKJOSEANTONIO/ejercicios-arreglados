#PRACTICA FUNCIONES "MASTERMIND"
import random
def generaClave(valores, tamañoclave):
    for i in range(tamañoclave):
        valor = random.choice(valores)
        clave.append(valor)
    return clave
def compruebaIntento(clave,intento):
    global respuesta_pista
    if clave == intento:
        respuesta_pista=["*","*","*","*","*"]
        return respuesta_pista
    if len(respuesta_pista)!=5:
        respuesta_pista=["","","","",""]
    for i in range(len(clave)):
        if clave[i] == intento[i]:
            respuesta_pista[i]="*"
        else:
            if intento[i]not in clave:
                respuesta_pista[i]="?"
            if intento[i] in clave:
                respuesta_pista[i]="+"
    return respuesta_pista
valores = ("a","b","c","d",1,2,3,4)
clave=[]
intento=[]
respuesta_pista = []
jugadas = 0
generaClave(valores,5)
while jugadas<10:
    caracter=input("Introduzca un numero o letra (de la a-d y del 1-4): ")
    if caracter.isdigit():
        caracter=int(caracter)
    if caracter not in valores:
        print("No es valido")
    else:
        intento.append(caracter)
    if len(intento)==5:
        print(intento)
        print(compruebaIntento(clave,intento))
        if compruebaIntento(clave,intento) == ["*","*","*","*","*"]:
            print("Has ganado...")
            exit()
        else:
            intento=[]
            jugadas+=1
print("Has perdido")
print(f"La clave era,{clave}")
#furula🤙