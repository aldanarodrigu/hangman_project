# Contiene la clase HangmanGame con el estado y la lógica del juego.
# Esta clase no habla con el jugador, solo decide

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

    def process_guess(self, letter):
        if letter in self.guessed_letters:
            return False

        self.guessed_letters.append(letter)

        if letter not in self.word:
            self.errors += 1
            return False

        return True

    def remaining_attempts(self):
        return self.max_errors - self.errors
