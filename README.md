# Juego del Ahorcado

Juego del ahorcado para la consola, hecho en Python. El jugador tiene que adivinar un título de película oculto, letra por letra, antes de cometer 6 errores. Las palabras se eligen al azar de un archivo de texto.

## Reglas

- La computadora elige un título al azar y lo muestra oculto con guiones bajos (`_`).
- El jugador ingresa **una letra por turno**.
- Solo se aceptan letras: números, símbolos o más de un carácter se rechazan y se vuelve a pedir.
- No se puede repetir una letra que ya se usó.
- Si la letra está en la palabra, se revela en todas las posiciones donde aparece.
- Si la letra no está, se suma un error.
- **Con 6 errores, se pierde** y se muestra la palabra.
- **Si se completan todas las letras antes, se gana.**
- Los caracteres que no son letras (espacios, guiones) se muestran desde el principio y no cuentan para ganar ni para perder.
- Las mayúsculas se toman como minúsculas: `M` y `m` son la misma letra.

Después de cada intento se muestra el progreso de la palabra, las letras usadas y los intentos que quedan.

## Requisitos

- Python 3.8 o superior.
- No hace falta instalar librerías: solo se usan los módulos `random` y `os`, que vienen con Python.

## Cómo ejecutarlo

1. Abrir una terminal dentro de la carpeta `hangman_project/`.
2. Ejecutar:

```bash
python3 main.py
```

En Windows puede ser `python main.py`.

> Es importante ejecutarlo desde dentro de la carpeta del proyecto: si no, Python no encuentra `wordlist.txt` ni los otros archivos.

## Ejemplo de partida

```
Palabra: _ _ _ _ _ _ - _ _ _
Letras usadas:
Intentos restantes: 6
Ingrese una letra: s
Adivinaste una letra, capo!

Palabra: s _ _ _ _ _ - _ _ _
Letras usadas: s
Intentos restantes: 6
Ingrese una letra: z
Le erraste :(

Palabra: s _ _ _ _ _ - _ _ _
Letras usadas: s, z
Intentos restantes: 5
Ingrese una letra: 6
Debe ingresar una letra.
```

## Estructura del proyecto

```
hangman_project/
│
├── main.py         # Bucle del juego: pide letras y muestra mensajes
├── game.py         # Clase HangmanGame: estado y reglas del juego
├── utils.py        # Funciones auxiliares
├── wordlist.txt    # Lista de títulos, uno por línea
└── README.md       # Este archivo
```

### `main.py`
Es el punto de entrada y el único archivo que habla con el jugador.
- `ask_letter(game)`: pide una letra y la valida (un solo carácter, que sea letra y que no se haya usado). Repite hasta recibir una entrada válida.
- `mostrar_estado(game)`: muestra la palabra, las letras usadas y los intentos restantes.
- `play()`: elige la palabra, crea el juego y ejecuta el bucle hasta que el jugador gana o pierde.

### `game.py`
Contiene la clase `HangmanGame`, que guarda el estado de la partida. No usa `input()`: solo decide.

| Atributo | Qué guarda |
|---|---|
| `word` | La palabra a adivinar |
| `guessed_letters` | Todas las letras que intentó el jugador |
| `max_errors` | Errores permitidos (6) |
| `errors` | Errores cometidos |

| Método | Qué hace |
|---|---|
| `display_progress()` | Devuelve la palabra con las letras adivinadas y `_` en las que faltan |
| `process_guess(letter)` | Guarda la letra; devuelve `True` si está en la palabra, o suma un error y devuelve `False` |
| `remaining_attempts()` | Devuelve cuántos intentos quedan |
| `is_won()` | `True` si se adivinaron todas las letras |
| `is_lost()` | `True` si se llegó al máximo de errores |

### `utils.py`
- `get_random_word()`: lee `wordlist.txt`, limpia las líneas, descarta las vacías y devuelve una palabra al azar en minúscula.
- `clear_screen()`: limpia la pantalla de la consola (funciona en Windows, Linux y Mac).

### `wordlist.txt`
Un título por línea, en minúscula. Se pueden usar espacios y guiones (por ejemplo `spider-man` o `el padrino`). Para agregar palabras, solo hay que sumar líneas al archivo.

## Decisiones técnicas

- **Se guardan todas las letras, también las incorrectas**, en `guessed_letters`. Así se puede avisar cuando el jugador repite una letra y mostrar todas las que usó.
- **Todo se pasa a minúscula** con `.lower()`, para que mayúsculas y minúsculas cuenten como la misma letra.
- **Los caracteres que no son letras se revelan con `isalpha()`**, tanto al mostrar el progreso como al comprobar si se ganó.
- **Cada archivo tiene un solo propósito**: `game.py` decide, `main.py` habla con el jugador y `utils.py` tiene funciones de apoyo.
- **El archivo se lee en `utf-8`**, para que la ñ se lea correctamente.

## Autores

- Aldana Rodriguez
- Bruno Castro
- Estela Barreto
