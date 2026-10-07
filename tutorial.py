import random
import time
import os

mini_game2 = random.randint(1, 100)

def mini():
    mini_game = random.choice(("камень", "бумага", "ножницы"))
    print("Введите (камень) или (ножницы) или (бумага)...")
    choise_pl = input("")
    print(choise_pl)
    if choise_pl == ["Камень"  or "КАМЕНЬ" or "камень" or "каменЬ"]:
        print("...")
        if mini_game == "камень":
            print("Ничья!")
            time.sleep(1.5)
        elif mini_game == "бумага":
            print("Ты проиграл:<")
            time.sleep(1.5)
        else:
            print("Ты победил!!!")
            time.sleep(1.5)

    elif choise_pl == ["Ножницы" or "НОЖНИЦЫ" or "ножницы" or "ножницЫ"]:
        print("...")
        if mini_game == "камень":
            print("Ты проиграл:<")
            time.sleep(1.5)
        elif mini_game == "бумага":
            print("Ты победил!!!")
            time.sleep(1.5)
        else:
            print("Ничья!")
            time.sleep(1.5)

    elif choise_pl == ["Бумага" or "БУМАГА" or "бумага" or "бумагА"]:
        print("...")
        if mini_game == "камень":
            print("Ты победил!!!")
            time.sleep(1.5)
        elif mini_game == "бумага":
            print("Ничья!")
            time.sleep(1.5)
        else:
            print("Ты проиграл:<")
            time.sleep(1.5)
    else:
        print("SintaxError: Это не связано с игрой!")
        time.sleep(1.5)

def mini2():
    print("Угадай число от 1 до 100!")
    Random_N = input("")
    print(Random_N)
    if Random_N == mini_game2:
        print("Ты победил!!!")
        time.sleep(0.5)
        print(f"Угаданное число: {mini_game2}")
    else:
        print("Ты не угадал:<")
        time.sleep(0.5)
        print(f"Задуманное число: {mini_game2}")

def mini_hack():
    print("Привет! Давай начнем игру!!! Эта игра называется 'симулятор взлома' суть заключается в том что на")
    time.sleep(0.1)
    print("тебя идет фейковая кибер атака, а твоя задача упрощенно защититься! Готов начать игру?")
    choice_hack = input("")
    print(choice_hack)

    if choice_hack == ["Да" or "дА" or "да" or "ДА"]:
        print("Чтобы деактивировать фейковый вирус, пропишите Delete")
        print("Начало через 3...")
        print("2...")
        print("1...")
        DELETE = input("")
        while True:
            os.system("start cmd")
            time.sleep(2)
            print(DELETE)
            if DELETE == "Delete":
                break
            else:
                return True
    elif choice_hack == ["Нет" or "нЕт" or "неТ" or "нет" or "НЕТ"]:
        print("Хорошо!:>")
        time.sleep(1.5)
    else:
        print("НЕИЗВЕСТНАЯ КОМАНДА!!!")
        return True

def no_int_menu():
    print("У вас нету интернета!")
    print("Можете сыграть в игру пока нет интернета:")
    print("Камень, ножницы, бумага")
    print("Угадай число")
    print("Симулятор взлома")
    print("Выберите 1, 2 или 3 (1 - камень ножницы бумага, 2 - угадай число, 3 - симулятор взлома)")
    choice_int_men = input("")
    if choice_int_men == "1":
        time.sleep(1)
        mini()
    elif choice_int_men == "2":
        time.sleep(1)
        mini2()
    elif choice_int_men == "3":
        time.sleep(1)
        mini_hack()
    else:
        print("Ошибка! Выберите 1, 2 или 3")
        time.sleep(1)