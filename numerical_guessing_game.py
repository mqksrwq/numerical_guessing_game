import random


def is_valid(value, n):
    if 1 <= value <= n:
        return True
    else:
        return False


print("Добро пожаловать в числовую угадайку")
user_answer = "y"
while user_answer != "n":

    total_attempts = 0
    input_line = input("Введите правую границу диапазона генератора: ")
    if not input_line.isdigit():
        print("Нужно ввести число")
        continue
    else:
        right_border = int(input_line)

    guessed_number = random.randint(1, right_border)

    while True:
        input_line = input("Введите число: ")
        if not input_line.isdigit():
            print("Нужно ввести число")
            continue
        else:
            entered_number = int(input_line)
            total_attempts += 1

        if is_valid(entered_number, right_border):
            if entered_number < guessed_number:
                print("Ваше число меньше загаданного, попробуйте еще разок")
            elif entered_number > guessed_number:
                print("Ваше число больше загаданного, попробуйте еще разок")
            else:
                print("Вы угадали, поздравляем!")
                print(f"Итоговое количество попыток: {total_attempts}")
                break
        else:
            print(f"Введите целое число от 1 до {right_border}?")

    user_answer = input("Хотите начать игру заново? (y/n): ")
    while user_answer not in "yn":
        print("Введите предложенные символы")
        user_answer = input("Хотите начать игру заново? (y/n): ")

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
