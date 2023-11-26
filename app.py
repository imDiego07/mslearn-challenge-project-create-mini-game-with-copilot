import random

def obtener_eleccion_usuario():
    """
    Solicita al usuario que ingrese su elección y la valida.
    Devuelve la elección en minúsculas.
    """
    opciones_validas = ['rock', 'paper', 'scissors']
    while True:
        eleccion = input("Elige rock, paper o scissors: ").lower()
        if eleccion in opciones_validas:
            return eleccion
        else:
            print("Opción no válida. Por favor, elige nuevamente.")

def obtener_eleccion_computadora():
    """
    Genera aleatoriamente la elección de la computadora (rock, paper o scissors).
    """
    opciones = ['rock', 'paper', 'scissors']
    return random.choice(opciones)

def comparar_jugadas(eleccion_usuario, eleccion_computadora):
    """
    Compara la elección del usuario con la de la computadora
    y determina el resultado de la ronda.
    Devuelve 'ganó', 'perdió' o 'empató'.
    """
    if eleccion_usuario == eleccion_computadora:
        return 'empató'
    elif (eleccion_usuario == 'rock' and eleccion_computadora == 'scissors') or \
         (eleccion_usuario == 'scissors' and eleccion_computadora == 'paper') or \
         (eleccion_usuario == 'paper' and eleccion_computadora == 'rock'):
        return 'ganó'
    else:
        return 'perdió'

def jugar_ronda():
    """
    Juega una ronda del juego.
    Devuelve el resultado de la ronda.
    """
    eleccion_usuario = obtener_eleccion_usuario()
    eleccion_computadora = obtener_eleccion_computadora()

    print(f"La computadora eligió: {eleccion_computadora}")

    resultado = comparar_jugadas(eleccion_usuario, eleccion_computadora)
    print(f"Resultado de la ronda: ¡{resultado}!\n")

    return resultado

def main():
    """
    Función principal que inicia el juego.
    """
    victorias = 0
    rondas = 0

    print("Bienvenido al juego Rock, Paper, Scissors!")

    while True:
        resultado_ronda = jugar_ronda()

        if resultado_ronda == 'ganó':
            victorias += 1

        rondas += 1

        seguir_jugando = input("¿Quieres seguir jugando? (s/n): ").lower()
        if seguir_jugando != 's':
            break

    print(f"\nJuego terminado. Puntuación final:")
    print(f"Victorias: {victorias} / Rondas jugadas: {rondas}")

if __name__ == "__main__":
    main()










    




