import random

def guess_number_game():
    print("Ласкаво просимо до гри 'Вгадай число'!")
    print("Я загадав число від 1 до 100. Спробуй його вгадати.")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Введи своє число: "))
            attempts += 1
            if guess < number_to_guess:
                print("Занадто мало! Спробуй ще раз.")
            elif guess > number_to_guess:
                print("Занадто багато! Спробуй ще раз.")
            else:
                print(f"Вітаю! Ти вгадав число {number_to_guess} за {attempts} спроб!")
                break
        except ValueError:
            print("Будь ласка, введи коректне число.")

if __name__ == "__main__":
    guess_number_game()