# Punto de entrada del juego. Acá está el bucle principal.
# Este archivo usa lo que hay en game.py y utils.py, sin lógica propia del juego.

from game import HangmanGame

def ask_letter(game):
    while True:
        letra = input("Ingrese una letra: ").lower()

        if len(letra) != 1:
            print("Debe ingresar solo una letra.")
        elif not letra.isalpha():
            print("Debe ingresar una letra.")
        elif letra in game.guessed_letters:
            print("Ya usaste esta letra. Proba con otra.")
        else:
            return letra
