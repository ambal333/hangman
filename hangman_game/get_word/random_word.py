import random

from hangman_game.get_word.r_file import read_file


def get_random_word():
    list_words = read_file()
    word = ''

    if list_words:
        word = random.choice(list_words)

    return word
