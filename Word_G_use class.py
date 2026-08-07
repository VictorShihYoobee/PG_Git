import random
import string


def get_random_word():
    """
    Returns a random word from a predefined list.
    """
    words = [
        "python", "variable", "function", "iterator", "notebook",
        "pipeline", "dataset", "computer", "research", "analytics"
    ]
    return random.choice(words)

class WordGuessGame:
    """
    A class to represent the Word Guessing Game.
    """
    def __init__(self, max_lives=6):
        self.max_lives = max_lives
        self.secret = get_random_word()
        self.blanks = self.make_blanks(self.secret)
        self.lives = self.max_lives
        self.used = set()

    def make_blanks(self, word):
        return ["_" for _ in word]

    def prompt_for_letter(self):
        while True:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(" → Please enter a single A-Z letter.")
                continue
            if guess in self.used:
                print(" → You already tried that letter.")
                continue
            return guess

    def reveal_letters(self, letter):
        found_any = False
        for i, ch in enumerate(self.secret):
            if ch == letter and self.blanks[i] == "_":
                self.blanks[i] = letter
                found_any = True
        return found_any

def all_blanks_filled(blanks):
    """
    Checks if all blanks in the word have been filled.
    """
    return "_" not in blanks

def play_game(max_lives=6):
    """
    Plays the Word Guessing Game.
    """
    game = WordGuessGame(max_lives)
    secret = game.secret
    blanks = game.blanks
    lives = game.lives
    used = game.used

    print("\nWelcome to Word Guessing!")
    print(f"The word has {len(secret)} letters.")
    print(" ".join(blanks))

    while True:
        # Ask the user to guess a letter
        guess = game.prompt_for_letter()
        game.used.add(guess)

        # Is the guessed letter in the word?
        if game.reveal_letters(guess):
            print("\n Well done, Nice job! You found a letter.")
            print(" ".join(blanks))
            # Are all blanks filled?
            if all_blanks_filled(blanks):
                print("\n Congratulation! You guessed the word!")
                print(f"Word: {secret}")
                print("GAME OVER")
                break
        else:
            # Lose a life
            lives -= 1
            print(f"\nNope. You lose a life. Lives left: {lives}")
            print(" ".join(blanks))

            # Have they run out of lives?
            if lives <= 0:
                print("\n Out of lives & Sad story!")
                print(f"The word was: {secret}")
                print("GAME OVER")
                break

        # (loop continues to ask for another letter)


if __name__ == "__main__":
    play_game()
