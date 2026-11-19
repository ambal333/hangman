from hangman_game.render.gallows import draw_gallows
from hangman_game.get_word.random_word import get_random_word


class Hangman:
    __ATTEMPTS = 8

    def __init__(self):
        self.__fault = 0

    @staticmethod
    def __open_letter(word, guessed_letters):
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

        try:
            while True:
                user_input = input(
                    "Начать новую игру? Введите да или нет: ").lower()
                if user_input == 'нет':
                    break
                elif user_input == 'да':

                    word = get_random_word().upper()
                    if not word:
                        print('Слова не найдены')
                        break
                    print(f"угадайте слово\nдлина слова: {len(word)} букв")
                    print("*" * len(word))
                    guessed_letters = set()
                    letters = ""

                    while '*' in letters or not letters:
                        user_letter = input("Введите букву: ").upper()

                        if len(user_letter) > 1:
                            print('Введите одну букву')
                            continue

                        if (user_letter not in russian_letter or
                                not user_letter.isalpha()):
                            print('Введите русскую букву')
                            continue

                        if user_letter in guessed_letters:
                            print('Вы уже вводили данную букву')
                            continue

                        guessed_letters.add(user_letter)
                        print(f'Введенные буквы: {''.join(guessed_letters)}')

                        if user_letter in word:
                            print('Вы угадали')
                        else:
                            self.__fault += 1
                            print('Вы не угадали')
                            print(draw_gallows(self.__fault))

                        letters = self.__open_letter(word, guessed_letters)
                        print(letters)

                        if self.__fault >= self.__ATTEMPTS:
                            print(f'Вы проиграли, загаданное слово: {word}')
                            break

                    if self.__fault != self.__ATTEMPTS:
                        print('Вы отгадали слово')

                    resume_game = input('Хотите сыграть еще раз?').lower()
                    if resume_game != 'да':
                        print('Хорошего дня')
                        break
                else:
                    print('такой команды нет')

        except FileNotFoundError:
            print('Файл со словами не найден')

