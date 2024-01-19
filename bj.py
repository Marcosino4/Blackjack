import random

class Carta:
    def __init__(self, nombre, palo, valor):
        self.nombre = nombre
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.nombre}"

def calcular_puntuacion(mano):
    puntuacion = sum(carta.valor for carta in mano)
    if any(carta.nombre.startswith('As') for carta in mano) and puntuacion + 10 <= 21:
        puntuacion += 10
    return puntuacion

def mostrar_mano(mano, jugador):
    print(f"\nMano de {jugador}:")
    for carta in mano:
        print(f"  {carta}")
    print(f"Puntuación total: {calcular_puntuacion(mano)}")

manoJugador = []
manoMaquina = []
baraja = []

palos = ["bastos", "oros", "copas", "espadas"]
for palo in palos:
    for j in range(1, 11):
        if j == 1:
            baraja.append(Carta(f"As de {palo}", palo, 1))
        elif j == 8:
            baraja.append(Carta(f"Sota de {palo}", palo, 10))
        elif j == 9:
            baraja.append(Carta(f"Caballo de {palo}", palo, 10))
        elif j == 10:
            baraja.append(Carta(f"Rey de {palo}", palo, 10))
        else:
            baraja.append(Carta(f"{j} de {palo}", palo, j))

random.shuffle(baraja)

# Repartir cartas iniciales
manoJugador.append(baraja.pop())
manoMaquina.append(baraja.pop())
manoJugador.append(baraja.pop())
manoMaquina.append(baraja.pop())

# Mostrar cartas iniciales
mostrar_mano(manoJugador, "Jugador")
mostrar_mano(manoMaquina, "Máquina")

# Turno del jugador
while calcular_puntuacion(manoJugador) < 21:
    accion = input("¿Quieres tomar otra carta? (s/n): ").lower()
    if accion == 's':
        manoJugador.append(baraja.pop())
        if calcular_puntuacion(manoMaquina) < 17:
            manoMaquina.append(baraja.pop())
        mostrar_mano(manoJugador, "Jugador")
        mostrar_mano(manoMaquina, "Máquina")
    else:
        break

# Mostrar manos finales
mostrar_mano(manoJugador, "Jugador")
mostrar_mano(manoMaquina, "Máquina")

# Determinar el ganador
puntuacionJugador = calcular_puntuacion(manoJugador)
puntuacionMaquina = calcular_puntuacion(manoMaquina)

if puntuacionJugador > 21:
    print("¡Has perdido! Te has pasado de 21.")
elif puntuacionMaquina > 21:
    print("¡Has ganado! La máquina se ha pasado de 21.")
elif puntuacionJugador > puntuacionMaquina:
    print("¡Has ganado! Tu puntuación es mayor que la de la máquina.")
elif puntuacionJugador < puntuacionMaquina:
    print("¡Has perdido! La máquina tiene una puntuación mayor.")
else:
    print("¡Es un empate!")









