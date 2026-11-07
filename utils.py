# Funciones auxiliares del juego.

import random

def get_random_word():
    """
    Leer todas las lineas de wordlist.txt y devolver una al azar
    """
    with open("wordlist.txt", "r", encoding="utf-8") as f:
        words = f.readlines()

    words = [word.strip().lower() for word in words if word.strip()]
    
    return random.choice(words)


print(get_random_word())