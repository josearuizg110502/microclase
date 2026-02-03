import random

def escoger():
    armas= ["tijera", "papel", "piedra"]

    while True:
        pc = random.choice(armas)
        persona = input("¿piedra, papel o tijera? ").lower()

        if persona not in armas:
           print("Opción inválida")
           continue

        print(f"La opción del oponente fue {pc}")

        if persona == pc:
           print("Empatados")

        elif (persona == "piedra" and pc == "tijera") or\
             (persona == "tijera" and pc == "papel") or\
             (persona == "papel" and pc == "piedra"):
            print("Felicidades, haz ganado!")
        else:
            print("Desafortunad@, perdiste")

        mensaje= input("¿Quieres jugar otra vez? (s/n) ").lower()

        if mensaje == "si":
           continue
        elif mensaje != ("si" and "no"):
           print("Opción inválida")
           continue
        elif mensaje == "no":
           print("Ok, gracias por jugar")
           break 

escoger()