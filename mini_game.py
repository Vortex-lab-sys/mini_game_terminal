import random
import time
import os

mini_game2 = random.randint(1, 100)

def mini():
    mini_game = random.choice(("камень", "бумага", "ножницы"))
    print("Введите (камень) или (ножницы) или (бумага)...")
    choise_pl = input("")
    print(choise_pl)
    if choise_pl.lower() == "камень":
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

    elif choise_pl.lower() == "ножницы":
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

    elif choise_pl.lower() == "бумага":
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
    Random_N = int(input(""))
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

    if choice_hack.lower() == "да":
        print("Чтобы деактивировать фейковый вирус, пропишите Delete")
        print("Начало через 3...")
        print("2...")
        print("1...")
        
        while True:
            DELETE = input("")
            os.system("start cmd")
            time.sleep(2)
            print(DELETE)
            if DELETE == "Delete":
                break
            else:
                print("Неизвестная команда")
    elif choice_hack.lower() == "нет":
        print("Хорошо!:>")
        time.sleep(1.5)
    else:
        print("НЕИЗВЕСТНАЯ КОМАНДА!!!")
        
def calculator():
    print("Введите + - * или /")
    minus = input("")
    time.sleep(1)
    print("Введите 1 число:")
    One_number = int(input(""))
    time.sleep(1)
    print("Введите 2 число:")
    two_number = int(input(""))
    plus_num = One_number + two_number
    minus_num = One_number - two_number
    umno_num = One_number * two_number
    ras_num = One_number / two_number
    time.sleep
    if minus == "+":
            print(f"Итоговое число: {plus_num}")
            time.sleep(1.5)
            no_int_menu()
    elif minus == "-":
            print(f"Итоговое число: {minus_num}")
            time.sleep(1.5)
            no_int_menu()
    elif minus == "*":
            print(f"Итоговое число: {umno_num}")
            time.sleep(1.5)
            no_int_menu()
    elif minus == "/":
            print(f"Итоговое число: {ras_num}")
            time.sleep(1.5)
            no_int_menu()
    else:
            print("Ошибка!")
            time.sleep(0.7)
            calculator()

def no_int_menu():
    print("У вас нету интернета!")
    print("Можете сыграть в игру пока нет интернета:")
    print("Камень, ножницы, бумага")
    print("Угадай число")
    print("Симулятор взлома")
    print("Выберите 1, 2 или 3 (1 - камень ножницы бумага, 2 - угадай число, 3 - симулятор взлома)")
    choice_int_men = int(input(""))
    if choice_int_men == 1:
        time.sleep(1)
        mini()
    elif choice_int_men == 2:
        time.sleep(1)
        mini2()
    elif choice_int_men == 3:
        time.sleep(1)
        mini_hack()
    else:
        print("Ошибка! Выберите 1, 2 или 3")
        time.sleep(1)