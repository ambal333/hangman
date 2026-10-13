from pathlib import Path
import random
from hangman_game.render.gallows import draw_gallows


class Hangman:
    def __init__(self):
        self.fault = 0
        self.resume = 0

    @staticmethod
    def read_file():
        words = []
        try:
            path = Path("./words/russian_words")
            with path.open("r", encoding="utf-8") as f:
                for line in f:
                    words.append(line.strip())
        except FileNotFoundError:
            return f"файла не существует"
        return words

    def random_word(self):
        list_words = self.read_file()
        word = random.choice(list_words)
        return word

    @staticmethod
    def open_letter(word, guessed_letters):
        guessed_letters_list = []
        for i in word:
            if i in guessed_letters:
                guessed_letters_list.append(i)
            else:
                guessed_letters_list.append("*")
        letters = "".join(guessed_letters_list)
        return letters

    def start_game(self):
        russian_letter = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ"
        while True:
            user_input = input("Начать новую игру? Введите да или нет: ").lower()
            if user_input == "да":
                while True:
                    self.fault = 0
                    word = self.random_word().upper()
                    print(f"угадайте слово\nдлина слова: {len(word)} букв")
                    print("*" * len(word))
                    guessed_letters = []
                    letters = ""
                    while True:
                        user_letter = input("Введите букву: ").upper()
                        if user_letter.isalpha() and user_letter in russian_letter:
                            if user_letter not in guessed_letters:
                                guessed_letters.append(user_letter)
                                print(f"введенные буквы: {' '.join(guessed_letters)}")
                            else:
                                print("вы уже вводили эту букву")
                                print(f"введенные буквы: {' '.join(guessed_letters)}")
                                continue
                            if user_letter in word:
                                print("вы угадали")
                            else:
                                print("вы не угадали")
                                self.fault += 1
                                print(draw_gallows(self.fault))
                            if self.fault == 7:
                                print(f"Вы проиграли. Загаданное слово: {word}")
                            letters = self.open_letter(word, guessed_letters)
                            print(letters)
                        elif user_letter.isdigit():
                            print("введите букву, а не цифру")
                            continue
                        elif user_letter not in russian_letter:
                            print("введите русскую букву")
                            continue
                        if "*" not in letters or self.fault == 7:
                            if self.fault == 7:
                                print("Вы проиграли, хотите сыграть еще раз?")
                            else:
                                print("Вы угадали слово, хотите сыграть еще раз?")
                            break
                    while True:
                        resume_game = input("Введите Да/Нет: ").lower()
                        if resume_game == "да":
                            self.fault = 0
                            self.resume = 1
                            break
                        elif resume_game == "нет":
                            print("хорошего дня")
                            self.resume = 0
                            break
                        else:
                            print("ответьте да или нет")
                    if self.resume == 0:
                        break
            if self.resume == 0:
                break

            elif user_input == "нет":
                print("Досвидания")
                break

            else:
                print("Такой команды нет")
