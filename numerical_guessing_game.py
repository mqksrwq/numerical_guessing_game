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
    right_border = int(input("Введите правую границу диапазона генератора: "))
    guessed_number = random.randint(1, right_border)
    entered_number = int(input("Введите число: "))
    while True:
        if is_valid(entered_number, right_border):
            if entered_number < guessed_number:
                total_attempts += 1
                print("Ваше число меньше загаданного, попробуйте еще разок")
            elif entered_number > guessed_number:
                total_attempts += 1
                print("Ваше число больше загаданного, попробуйте еще разок")
            else:
                total_attempts += 1
                print("Вы угадали, поздравляем!")
                print(f"Итоговое количество попыток: {total_attempts}")
                break
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")

        entered_number = int(input("Введите число: "))
    user_answer = input("Хотите продолжить игру? (y/n): ")

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
