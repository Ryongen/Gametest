#Modulos a cargar
import random

# stats
personaje = [1, 100, 0, "nada"]
inventario = []
aventura = []

# juego


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
        return personaje,

    elif personaje[3] == "Mago":
        personaje[1] = 150
        personaje[2] = 100
        print("Has elegido Mago")
        inventario.append("Baston")
        return personaje,

    elif personaje[3] == "Asesino":
        personaje[1] = 200
        personaje[2] = 50
        print("Has elegido Asesino")
        inventario.append("Dagas")
        return personaje,
    else:
        print("Caca")
        return start(personaje)


print("Tu nivel es: ", personaje[0])
print("Tu vida es: ", personaje[1])
print("TU mana es: ", personaje[2])
print("Tu clase es: ", personaje[3])
print("Tu inventario contiene: ", inventario)

start(personaje)

print("Tu nivel es: ", personaje[0])
print("Tu vida es: ", personaje[1])
print("TU mana es: ", personaje[2])
print("Tu clase es: ", personaje[3])
print("Tu inventario contiene: ", inventario)

start(aventura)

print("Inicio:")
print("\n Tu historia comienza frente a las puertas de una gran mazmorra cuya entrada parece estar despejada.")
print("¿Qué quieres hacer?")
print("1.-Irme a casa, no es asunto mío")
print("o")
print("2.-Entrar, he nacido para la aventura!")
a = input("Elijo:")

if a == "Irme a casa, no es asunto mío"
	print("Largo nenaza!")

elif a== "Entrar, he nacido para la aventura!"
	print("Perfecto, se necesita a alguien que imparta justicia por ahí dentro")

else:
	print("Eso no vale!")
	return start(aventura)

# a = random.randint(1, 10)
# print(a)