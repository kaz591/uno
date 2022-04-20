#Creacion de un juego de uno contra el computador
import random

#Solo inclui estos numeros y colores para tener mayor control en la creacion
numeros = [1,2,3,4]
colores = ["azul", "rojo"]
cartas = []
x= ""

#Funcion que genera el mazo del juego
def deck():
    for i in range(len(numeros)):
        for a in range(len(colores)):
            x = str(numeros[i]) + " " + colores[a]
            cartas.append(x)
    return cartas
            # Activar para duplicar las cartas en el mazo   cartas.extend([x, x])
    #print(cartas) para conocer la mano inicial

deck()
#Funcion que indica cuantas cartas se deben robar
def robar(x):
    inicial = []
    inicial = random.sample(cartas, x)
    for i in inicial:
        cartas.remove(i)
    a =  ", ".join(inicial)
    print(f"Tu mano inicial es: {a}")
    dividir(a)
    return inicial

#funcion que divide los arrays para poder buscar por numero o color
def dividir(palabra):
        palabra = list([i for i in palabra.split()])
        print(palabra)
        return palabra

#funcion para iniciar el juego

print("********Damos inicio al juego********")
primera = random.choice(cartas)
print(f"La primera carta es: {primera}")
cartas.remove(primera)
dividir(primera)


empezar = robar(3)

while True:
    jugar = (input("Que carta deseas jugar?: "))
    if jugar in empezar:
        print(f"Si puedes jugar la carta {jugar}")
        break
    else:
        print(f"No tienes la carta '{jugar}' en tu mano")


"""while True:
    dividir()"""


