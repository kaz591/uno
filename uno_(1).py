#Creacion de un juego de uno contra el computador
import random
from pprint import pprint

#Solo inclui estos numeros y colores para tener mayor control en la creacion
#incluir +2, +4 y cambio de color
#incluir cartas especiales
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
        # Activar para duplicar las cartas en el mazo   cartas.extend([x, x])
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

#funcion que divide los arrays para poder buscar por numero o color
def dividir(palabra):
        palabra = list([i for i in palabra.split()])
        return palabra

#funcion para iniciar el juego
print("********Damos inicio al juego********")
primera = random.choice(cartas)
ultima = primera
print(f"La primera carta es: {ultima}")
cartas.remove(ultima)
dividir(ultima)

#determina la cantidad de cartass para iniciar el juego
mano = robar(3)

while len(cartas) > 1:
    print(f"Tu mano es: {(join(mano))}")
    carta = (input("Que carta deseas jugar?: "))
    if carta == "robar":
        robar(1)
        mano.extend(robar(1))
        continue
    if carta not in mano:
        print(f"No tienes la carta '{carta}' en tu mano")
    elif carta in mano:
        juego_ini = dividir(carta)
        if  any(item in dividir(ultima) for item in dividir(carta)):
            ultima = carta
            print(f"\nla ultima carta jugada fue: {ultima}")
            mano.remove(carta)
            if len(mano) < 1:
                print("Felicitaciones, ganaste!")
                break
        else:
            print(f"No puedes jugar la carta: {carta}")
print("Fin del juego")
