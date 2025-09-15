import random


def is_valid(n):
    return True if 1 <= n <= 100 else False


print("Добро пожаловать в числовую угадайку")
guessed_number = random.randint(1, 100)
total_attempts = 0

entered_number = int(input("Введите число: "))
while True:
    if is_valid(entered_number):
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
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
