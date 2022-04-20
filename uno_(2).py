#Creacion de un juego de uno contra el computador
import random
from pprint import pprint
import sys

#Solo inclui estos numeros y colores para tener mayor control en la creacion
numeros = [1,2,3,4]
colores = ["azul", "rojo", "verde"]
cartas = []
mano = []
ultima = []
x= ""


#Aca generamos el deck de cartas
for i in range(len(numeros)):
    for a in range(len(colores)):
        x = str(numeros[i]) + " " + colores[a]
        cartas.append(x)
        #cartas.extend([x, x]) #Activar para duplicar las cartas en el mazo
#print(cartas) para conocer la mano inicial

#Funcion que indica cuantas cartas se deben robar
def robar(x):
    robar = random.sample(cartas, x)
    for i in robar:
        cartas.remove(i)
    return robar

def join(x):
    a = ", ".join(x)
    return a

"""def nombres(x):
    for i in range(x):
        jugador()= str(input("Ingresa el nombre del primer jugador: "))
        return jugador1
        if x == 2:
            return str(input(""))"""


#funcion que divide los arrays para poder buscar por numero o color
def dividir(palabra):
        palabra = list([i for i in palabra.split()])
        return palabra

#funcion para iniciar el juego
numeroJugadores = int(input("Introduce el numero de jugadores: "))
print("********Damos inicio al juego********")
primera = random.choice(cartas)
ultima = primera
print(f"La primera carta es: {ultima}")
cartas.remove(ultima)
dividir(ultima)


#se da inicio al robo de las primeras cartas por jugador
for i in range(numeroJugadores):
    mano.append(robar(3))

while True:
    for i in range(numeroJugadores): #iteracion en posicion 0 y luego 1 si son 2 jugadores
        print(f"Jugador {i +1}, tu mano es: {(join(mano[i]))}")
        carta = (input("Que carta deseas jugar?: "))
        if carta == "robar":
            robe = robar(1)
            print(f"La carta robada fue: {join(robe)}")
            print(f"\n\n\n\n\nla ultima carta jugada fue: {ultima}")
            mano[i].extend(robe)
            continue
        if carta in mano[i]:
            if  any(item in dividir(ultima) for item in dividir(carta)):
                ultima = carta
                print(f"\n\n\n\n\nla ultima carta jugada fue: {ultima}")
                mano[i].remove(carta)
            else:
                print(f"No puedes jugar la carta: {carta}")
        elif carta not in mano:
            print(f"No tienes la carta '{carta}' en tu mano")
        if len(mano[i]) < 1:
            print(f"Felicitaciones jugador {i+1}, ganaste!")
            sys.exit()
        if len(cartas) < 1:
            print("Fin del juego")
            sys.exit()

