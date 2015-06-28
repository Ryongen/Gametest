# Modulos a cargar
import random

# stats
personaje = [1, 100, 0, "nada"]
inventario = []
aventura = []
direccion = 0
mapa = 100
historial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] #El numero total de mapas por ahora (aunque es un apaño ya explicare porque)
# Funciones

# Eleccion de clase


def start(personaje):
    print("Que desea ser usted")
    print("\n 1.- Guerrero")
    print("\n 2.- Mago")
    print("\n 3.- Asesino")
    print("\n Elige tu clase:")

    personaje[3] = input()
    if personaje[3] == "Guerrero":
        personaje[1] = 250
        print("Has elegido guerrero")
        inventario.append("Mandoble")
        return personaje

    elif personaje[3] == "Mago":
        personaje[1] = 150
        personaje[2] = 100
        print("Has elegido Mago")
        inventario.append("Baston")
        return personaje

    elif personaje[3] == "Asesino":
        personaje[1] = 200
        personaje[2] = 50
        print("Has elegido Asesino")
        inventario.append("Dagas")
        return personaje
    else:
        print("Caca")
        return start(personaje)

# Empieza la aventura


def aventure(mapa):
    print("Inicio:")
    print(
        "\n Tu historia comienza frente a las puertas de una gran mazmorra cuya entrada parece estar despejada.")
    print("\n ¿Qué quieres hacer?")
    print("\n 1.-Irme a casa, no es asunto mío")
    print("\n o")
    print("\n 2.-Entrar, he nacido para la aventura!")

    direccion = eval(input())
    if direccion == 1:
        print("\n Largo nenaza!")
        mapa = random.randint(1, 9) #hace roll entre 1 y 9 siendo 10 el destino final que es la ciudad y asi que no salga el destino final al comenzar el juego
        return (mapa)

    elif direccion == 2:
        print(
            "\n Perfecto, se necesita a alguien que imparta justicia por ahí dentro")
        mapa = random.randint(11, 19) #Lo mismo que antes siendo 20 el final de la mazmorra 
        return mapa

    else:
        print("\n Eso no vale!")
        return aventure(mapa)

# Mapas

def Mapas(mapa, historial):
    print("\n Has llegado a: ")
    if mapa == 1:
        print("un Lago")
        historial.remove(1) #Quita el mapa 1 de la seleccion de mapas que pueden salir
        mapa = random.randint(historial[0], historial[9]) #Hace un roll (random) entre la posicion 1 del historial y la 10 
        return (mapa) #Devuelve el valor mapa y acaba la funcion 
    elif mapa == 2:
        print("un Bosque")
        historial.remove(2)
        mapa = random.randint(historial[0], historial[9])
        return (mapa)
    elif mapa == 3:
        print("un pepe")
        historial.remove(3)
        mapa = random.randint(historial[0], historial[9])
        return (mapa)
    elif mapa == 4:
        print("una planicia")
        historial.remove(4)
        mapa = random.randint(historial[0], historial[9])
        return (mapa)
    elif mapa == 5:
        print("una montaña")
        historial.remove(5)
        mapa = random.randint(historial[0], historial[9])
        return (mapa)
    elif mapa == 6:
        print("un rio")
        historial.remove(6)
        mapa = random.randint(historial[0], historial[9])
        return (mapa)
    elif mapa == 7:
        print("una casa abandonada")
        historial.remove(7)
        mapa = random.randint(historial[0], historial[9])
        return (mapa)
    elif mapa == 8:
        print("una playa")
        historial.remove(8)
        mapa = random.randint(historial[0], historial[9])
        return (mapa)
    elif mapa == 9:
        print("unas ruinas")
        historial.remove(9)
        mapa = random.randint(historial[0], historial[9])
        return (mapa)
    elif mapa == 10:
        print("la ciudad")
        historial.remove(10)
        mapa = random.randint(historial[0], historial[9])
        return (mapa)

    


# Juego

print("Tu nivel es: ", personaje[0])
print("Tu vida es: ", personaje[1])
print("TU mana es: ", personaje[2])
print("Tu clase es: ", personaje[3])
print("Tu inventario contiene: ", inventario)

start(personaje) #Elige el personaje 

print("Tu nivel es: ", personaje[0])
print("Tu vida es: ", personaje[1])
print("TU mana es: ", personaje[2])
print("Tu clase es: ", personaje[3])
print("Tu inventario contiene: ", inventario)

mapa = aventure(mapa) # para que la variable Mapa sea el desenlace de la funcion aventura

print("Te quedan por visitar: ", historial)
print(" mapa elegido:", mapa)
mapa = Mapas(mapa, historial) # Otra vez para que la variable mapa ahora sea el desenlace de la funcion mapas

print("Te quedan por visitar: ", historial)
print(" mapa elegido:", mapa)

# a = random.randint(1, 10)
# print(a)
