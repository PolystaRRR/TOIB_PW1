import random
import string
from string import digits, punctuation, ascii_letters  # алфавит


def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        user_input = input("Введите длину пароля (по умолчанию 8, должно быть не меньше 8): ")
        if user_input.strip() == "":
            length = 8
            break
        elif user_input.isdigit() and int(user_input) >= 8:
            length = int(user_input)
            break
        else:
            print("Пожалуйста, введите целое число не меньше 8 или оставьте пустым для использования стандартной длины!")

    print(f"Сгенерированный пароль: {generate_random_password(length)}")