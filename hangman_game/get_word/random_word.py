from hangman_game.get_word.r_file import read_file
import random
def get_random_word(self):
    list_words = read_file()
    word = random.choice(list_words)
    return word