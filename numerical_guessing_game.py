import random

alphabet_ru = [
    "Добро пожаловать в числовую угадайку",
    "Введите правую границу диапазона генератора: ",
    "Нужно ввести число",
    "Введите число: ",
    "Ваше число меньше загаданного, попробуйте еще разок",
    "Ваше число больше загаданного, попробуйте еще разок",
    "Вы угадали, поздравляем!",
    "Итоговое количество попыток: ",
    "Введите целое число от 1 до ",
    "Хотите начать игру заново? (y/n): ",
    "Введите предложенные символы",
    "Спасибо, что играли в числовую угадайку. Еще увидимся...",
]

alphabet_en = [
    "Welcome to the number guessing game",
    "Enter the upper bound for the number generator: ",
    "You need to enter a number",
    "Enter a number: ",
    "Your number is lower than the target, try again",
    "Your number is higher than the target, try again",
    "You guessed it, congratulations!",
    "Total number of attempts: ",
    "Enter an integer from 1 to ",
    "Want to start a new game? (y/n): ",
    "Enter the suggested characters",
    "Thank you for playing the number guessing game. See you again...",
]


def is_valid(value, n):
    if 1 <= value <= n:
        return True
    else:
        return False


current_alph = ""
input_line = input("Select language (en/ru): ")
if input_line == "en":
    current_alph = alphabet_en
elif input_line == "ru":
    current_alph = alphabet_ru

print(current_alph[0])
user_answer = "y"
while user_answer != "n":

    total_attempts = 0
    input_line = input(current_alph[1])
    if not input_line.isdigit():
        print(current_alph[2])
        continue
    else:
        right_border = int(input_line)

    guessed_number = random.randint(1, right_border)

    while True:
        input_line = input(current_alph[3])
        if not input_line.isdigit():
            print(current_alph[2])
            continue
        else:
            entered_number = int(input_line)
            total_attempts += 1

        if is_valid(entered_number, right_border):
            if entered_number < guessed_number:
                print(current_alph[4])
            elif entered_number > guessed_number:
                print(current_alph[5])
            else:
                print(current_alph[6])
                print(current_alph[7], total_attempts)
                break
        else:
            print(current_alph[8], right_border)

    user_answer = input(current_alph[9])
    while user_answer not in "yn":
        print(current_alph[10])
        user_answer = input(current_alph[9])

print(current_alph[11])
