#Creacion de un juego de uno contra el computador
import random
import sys
import snoop
import time

#Solo inclui estos numeros y colores para tener mayor control en la creacion
numeros = [1,2,3,4]#aca se incluye el +2, saltar turno y reversa
colores = ["azul"]
cartas = []
segundasCartas = []
mano = []
ultima = []
jugadores = []
listaJugadores = []
x= ""
contador = 0
sentido = "derecha"

#Aca generamos el deck de cartas
for i in range(len(numeros)):
    for a in range(len(colores)):
        x = str(numeros[i]) + " " + colores[a]
        cartas.append(x)
#random.shuffle(cartas)
#cartas.append("+4")
#cartas.append("cambiar color")
#cartas[1] = ("reversa azul")
print(cartas)
        #cartas.extend([x, x]) #Activar para duplicar las cartas en el mazo

"""def robar(x):
    robar = random.sample(cartas, x)
    for i in robar:
        cartas.remove(i)
    return robar"""
def robar(x): #Funcion que indica cuantas cartas se deben robar

    robadas = cartas[0: x]
    for i in robadas:
        cartas.remove(i)
    return robadas

def join(x): #une los items de un array y los muestra como strings
    a = ", ".join(x)
    return a

def nombres(x): #funcion para definir los nombres de los jugadores
    for i in range(x):
        jugador = str(input("Ingresa el nombre del jugador: "))
        jugadores.append(jugador)
    print("\n\n\n")
    return jugadores[i]

def shuffle(list):
    random.shuffle(list)
    cartas = list.copy()
    print(cartas)
    print(segundasCartas)
    return cartas

def nocartas(cartas):
        print("Se acabaron las cartas, vamos a revolverlas nuevamente \n Brrrrrrrrr \n BRRRRRR")
        cartas = segundasCartas.copy()
        shuffle(cartas)
        segundasCartas.clear()
        print(f"Cartas revueltas.\nLa ultima carta jugada fue: {ultima}")
        return cartas

def dividir(palabra):#funcion que divide los arrays para poder buscar por numero o color
        palabra = list([i for i in palabra.split()])
        return palabra

while True:
    try:
        numeroJugadores = int(input("Introduce el numero de jugadores: "))
        for i in range((numeroJugadores)):
            listaJugadores.append(i)
        print(listaJugadores)
        break
    except ValueError:
        print("Oops! ese no es un numero, intenta nuevamente.")

nombres(numeroJugadores)
print("********Damos inicio al juego********")
primera = cartas[0]
ultima = primera
print(f"La primera carta es: {ultima}")
cartas.remove(ultima)
segundasCartas.append(ultima)

#se da inicio al robo de las primeras cartas por jugador
for i in range(numeroJugadores):
    mano.append(robar(3))

i = 0
keep = True
while keep:
    if sentido == "derecha":
        if len(jugadores) <= i:
            i = 0
        check = True
        while check:
            if contador == 1: #se ejecuta si se juega el +2
                if len(cartas) < 1: #cuando las cartas se acaban se revuelven nuevamente para seguir el juego
                    nocartas()
                    mano[i].extend(robar(2))
                    print(f"{jugadores[i].capitalize()}, el jugador anterior jugó la carta {ultima} por lo cual deberas robar {dividir(ultima[1])} y perder tu turno\n")
                    contador = 0
                    time.sleep(4)
                    check = False
                    break
                else:
                    mano[i].extend(robar(2))
                    print(f"{jugadores[i].capitalize()}, el jugador anterior jugó la carta {ultima} por lo cual deberas robar {dividir(ultima[1])} y perder tu turno\n")
                    contador = 0
                    time.sleep(4)
                    check = False
                    break
            elif contador == 2:# se ejecuta si se juega el +4
                mano[i].extend(robar(4))
                print(f"\n{jugadores[i].capitalize()}, el jugador anterior jugó la carta {carta} por lo cual deberas robar {dividir(carta[1])} y perder tu turno\n")
                contador = 0
                time.sleep(4)
                check = False
                break
            elif contador == 3:#se ejecuta si se juega saltar turno
                print(f"\n{jugadores[i].capitalize()}, el jugador anterior jugó la carta {carta} y perderas tu turno\n")
                contador = 0
                time.sleep(4)
                check = False
                break

            print(f"\n\n\nla ultima carta jugada fue: {ultima}")
            print(f"{jugadores[i].capitalize()}, tu mano es: {join(mano[i])}")
            print(f"disponibles: {cartas}")
            print(segundasCartas)
            carta = (input("Que carta deseas jugar?: "))
            print("")
            if carta == "robar":
                if len(cartas) < 1: #cuando las cartas se acaban se revuelven nuevamente para seguir el juego
                    cartas = nocartas(cartas)
                    print(cartas)
                    print(segundasCartas)
                robe = robar(1)
                mano[i].extend(robe)
                i+= 1
                check = False
                continue
            if carta in mano[i]:
                if "+4" in carta:
                    contador = 2
                    while True:
                        try:
                            color = str(input("Seleccione el color que desea asignar: "))
                        except:
                            print(f"{color}, no es un color valido")
                        else:
                            if color in colores:
                                break
                            else:
                                print(f"{color} no está en el juego")
                    mano[i].remove("+4")
                    segundasCartas.append("+4")
                    ultima = color
                    i+=1
                    break
                if "cambiar color" in carta:
                    cambio = str(input("Seleccione el color que desea asignar: "))
                    print("\n\n\n")
                    mano[i].remove("cambiar color")
                    segundasCartas.append("cambiar color")
                    ultima = cambio
                    break
                if  any(item in dividir(ultima) for item in dividir(carta)):
                    ultima = carta
                    mano[i].remove(carta)
                    segundasCartas.append(carta)
                    if "+2" in dividir(carta):
                        contador = 1
                    elif "saltar turno" in carta:
                        contador = 3
                    elif "reversa" in carta:
                        sentido = "izquierda"
                        break
                    i+= 1
                else:
                    print(f"No puedes jugar la carta: {carta}")
                    print(f"la ultima carta jugada fue: {ultima}\n")
            elif carta not in mano:
                print(f"No tienes la carta '{carta}' en tu mano")
                print(f"la ultima carta jugada fue: {ultima}")
            if len(mano[i - 1]) < 1:
                print(f"Felicitaciones {jugadores[i - 1].capitalize()}, ganaste!")
                sys.exit()
            if (len(jugadores) -1) < i:
                i = 0
            check = False
            break

    elif sentido == "izquierda": #sentido invertido
        i-= 1
        if i < 0:
            i =  len(jugadores) -1
        check = True
        print(listaJugadores[i], jugadores[i])
        while check:
            if contador == 1: #se ejecuta si se juega el +2
                if len(cartas) < 1: #cuando las cartas se acaban se revuelven nuevamente para seguir el juego
                    nocartas()
                    mano[i].extend(robar(2))
                    print(f"{jugadores[i].capitalize()}, el jugador anterior jugó la carta {ultima} por lo cual deberas robar {dividir(ultima[1])} y perder tu turno\n")
                    contador = 0
                    time.sleep(4)
                    check = False
                    break
                else:
                    mano[i].extend(robar(2))
                    print(f"{jugadores[i].capitalize()}, el jugador anterior jugó la carta {ultima} por lo cual deberas robar {dividir(ultima[1])} y perder tu turno\n")
                    contador = 0
                    time.sleep(4)
                    check = False
                    break
            elif contador == 2:# se ejecuta si se juega el +4
                mano[i].extend(robar(4))
                print(f"\n{jugadores[i].capitalize()}, el jugador anterior jugó la carta {carta} por lo cual deberas robar {dividir(carta[1])} y perder tu turno\n")
                contador = 0
                time.sleep(4)
                check = False
                break
            elif contador == 3:#se ejecuta si se juega saltar turno
                print(f"\n{jugadores[i].capitalize()}, el jugador anterior jugó la carta {carta} y perderas tu turno\n")
                contador = 0
                time.sleep(4)
                check = False
                break

            print(f"\n\n\nla ultima carta jugada fue: {ultima}")
            print(f"{jugadores[i].capitalize()}, tu mano es: {join(mano[i])}")
            print(f"disponibles: {cartas}")
            print(segundasCartas)
            carta = (input("Que carta deseas jugar?: "))
            print("")
            if carta == "robar":
                robe = robar(1)
                mano[i].extend(robe)
                check = False
                if len(cartas) < 1: #cuando las cartas se acaban se revuelven nuevamente para seguir el juego
                    cartas = nocartas(cartas)
                    print(cartas)
                    print(segundasCartas)
                continue
            if carta in mano[i]:
                if "+4" in carta:
                    contador = 2
                    while True:
                        try:
                            color = str(input("Seleccione el color que desea asignar: "))
                        except:
                            print(f"{color}, no es un color valido")
                        else:
                            if color in colores:
                                break
                            else:
                                print(f"{color} no está en el juego")
                    mano[i].remove("+4")
                    segundasCartas.append("+4")
                    ultima = color
                    break
                if "cambiar color" in carta:
                    cambio = str(input("Seleccione el color que desea asignar: "))
                    print("\n\n\n")
                    mano[i].remove("cambiar color")
                    segundasCartas.append("cambiar color")
                    ultima = cambio
                    break
                if  any(item in dividir(ultima) for item in dividir(carta)):
                    ultima = carta
                    mano[i].remove(carta)
                    segundasCartas.append(carta)
                    if "+2" in dividir(carta):
                        contador = 1
                    if "saltar turno" in carta:
                        contador = 3
                    if "reversa" in carta:
                        sentido = "derecha"
                        i+= 1
                        if i >= len(jugadores):
                            i= 0
                    check = False
                else:
                    print(f"No puedes jugar la carta: {carta}")
                    print(f"la ultima carta jugada fue: {ultima}\n")
            elif carta not in mano:
                print(f"No tienes la carta '{carta}' en tu mano")
                print(f"la ultima carta jugada fue: {ultima}")
            if len(mano[i]) < 1:
                print(f"Felicitaciones {jugadores[i].capitalize()}, ganaste!")
                sys.exit()


