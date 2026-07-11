import random

class HangmanGame:
    def __init__(self):
        self.words = ["apple", "banana", "grapes", "mango", "kiwi"]
        self.reset()

    def reset(self):
        self.word = random.choice(self.words)
        self.guessed_letters = []
        self.max_wrong = 6
        self.wrong_guesses = 0

    def guess_letter(self, letter):
        letter = letter.lower()

        if letter in self.guessed_letters:
            return

        self.guessed_letters.append(letter)

        if letter not in self.word:
            self.wrong_guesses += 1

    def get_word(self):
        display = []

        for letter in self.word:
            if letter in self.guessed_letters:
                display.append(letter)
            else:
                display.append("_")

        return " ".join(display)

    def guesses_left(self):
        return self.max_wrong - self.wrong_guesses

    def is_won(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    def is_lost(self):
        return self.wrong_guesses >= self.max_wrong