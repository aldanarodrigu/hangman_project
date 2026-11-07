# Punto de entrada del juego. Acá está el bucle principal.
# Este archivo usa lo que hay en game.py y utils.py, sin lógica propia del juego.

from game import HangmanGame
from utils import get_random_word
from utils import get_random_word, clear_screen

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


def mostrar_estado(game):
    print("Palabra: ", game.display_progress())
    print("Letras usadas: ", game.guessed_letters)
    print("Intentos restantes: ", game.remaining_attempts())


def play():
    palabra = get_random_word()
    game = HangmanGame(palabra)


    while not game.is_won() and not game.is_lose():
        clear_screen()
        mostrar_estado(game)

        letra = ask_letter(game)

        if game.process_guess(letra):
            print("Adivinaste una letra, capo!")
        else:
            print("Le erraste :(")

        if game.is_won():
            print("Ganaste!!!!")
        
        if game.is_lose():
            print("Fin del juego. La palabra era: ", game.word)


play()
        


