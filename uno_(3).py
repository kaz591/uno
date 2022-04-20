#Creacion de un juego de uno contra el computador
import random
import sys
import snoop

#Solo inclui estos numeros y colores para tener mayor control en la creacion
numeros = [1,2,3,4,"+2"]
colores = ["azul", "rojo", "verde"]
especiales = ["+2", "+4", "cambio de color", "saltar turno", "invertir orden"]
cartas = []
segundasCartas = []
mano = []
ultima = []
jugadores = []
x= ""

#Aca generamos el deck de cartas
for i in range(len(numeros)):
    for a in range(len(colores)):
        x = str(numeros[i]) + " " + colores[a]
        cartas.append(x)
        random.shuffle(cartas)
print(cartas)
        #cartas.extend([x, x]) #Activar para duplicar las cartas en el mazo

"""def robar(x):
    robar = random.sample(cartas, x)
    for i in robar:
        cartas.remove(i)
    return robar"""
#Funcion que indica cuantas cartas se deben robar
def robar(x):
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

@snoop
def shuffle(list):
    random.shuffle(list)
    #cartas = list.copy()
    print(cartas)
    print(segundasCartas)
    return cartas

#funcion que divide los arrays para poder buscar por numero o color
def dividir(palabra):
        palabra = list([i for i in palabra.split()])
        return palabra

while True:
    try:
        numeroJugadores = int(input("Introduce el numero de jugadores: "))
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

keep = True
while keep:
    for i in range(numeroJugadores): #iteracion en posicion 0 y luego 1 si son 2 jugadores
        check = True
        while check:
            print(f"{jugadores[i].capitalize()}, tu mano es: {join(mano[i])}")
            carta = (input("Que carta deseas jugar?: "))
            if carta == "robar":
                robe = robar(1)
                print(f"\n\n\n\n\n\nla ultima carta jugada fue: {ultima}")
                mano[i].extend(robe)
                check = False
                if len(cartas) < 1: #cuando las cartas se acaban se revuelven nuevamente para seguir el juego
                    print("Se acabaron las cartas, vamos a revolverlas nuevamente \n Brrrrrrrrr \n BRRRRRR")
                    cartas = segundasCartas.copy()
                    shuffle(cartas)
                    segundasCartas.clear()
                    print(f"Cartas revueltas.\nLa ultima carta jugada fue: {ultima}")
                continue
            if carta in mano[i]:
                if  any(item in dividir(ultima) for item in dividir(carta)):
                    ultima = carta
                    print(f"\n\n\n\n\nla ultima carta jugada fue: {ultima}")
                    mano[i].remove(carta)
                    segundasCartas.append(carta)
                    print(cartas)
                    print(segundasCartas)
                    check = False
                else:
                    print(f"No puedes jugar la carta: {carta}")
                    print(f"la ultima carta jugada fue: {ultima}")
            elif carta not in mano:
                print(f"No tienes la carta '{carta}' en tu mano")
                print(f"la ultima carta jugada fue: {ultima}")
            if len(mano[i]) < 1:
                print(f"Felicitaciones {jugadores[i].capitalize()}, ganaste!")
                sys.exit()


