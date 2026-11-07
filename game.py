# Contiene la clase HangmanGame con el estado y la lógica del juego.
#  esta clase no habla con el jugador, solo decide

class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.errors = 0
        self.max_errors = 6

    def display_progress(self):
        progress = ""

        for letter in self.word:
            if letter in  self.guessedletters:
                progress += letter 
            else:
                progress += ""
        return progress