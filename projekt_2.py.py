"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

Simulace hry Bulls and Cows

author: Petr Vrba
email: pvrba01@gmail.com
discord: petrv_95056
"""
import random

def greet_user():
    """Vypíše úvodní text."""
    print("""
    ---------------------------------------------
     Hi there!
    I've generated a random 4 digit number for you.
Let's play a bulls and cows game. 
    ---------------------------------------------
    """)

def generate_secret_number():
    digits = list(range(1, 10)) + [0]  
    random.shuffle(digits)
    secret_number = digits[0:4]
    while secret_number[0] == 0: 
        random.shuffle(digits)
        secret_number = digits[0:4]
    return ''.join(map(str, secret_number))

def is_valid_guess(guess):
    """Check if your guess is correct."""
    if len(guess) != 4:
        return "Your guess must have exactly 4 numbers."
    if not guess.isdigit():
        return "Your guess must contain only numbers."
    if len(set(guess)) != 4:
        return "Your guess must contain only unique numbers = the numbers must not repeat."
    if guess[0] == '0':
        return "Your guess must not start with zero."
    return None

def evaluate_guess(guess, secret):
    bulls = sum(1 for g, s in zip(guess, secret) if g == s)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows

def play_game():
    greet_user()
    secret_number = generate_secret_number()

    while True:
        guess = input("Zadejte svůj tip: ")
        validation_error = is_valid_guess(guess)
        if validation_error:
            print(validation_error)
            continue

        bulls, cows = evaluate_guess(guess, secret_number)
        print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")

        if bulls == 4:
            print("Correct, you've guessed the right number.")
            break

if __name__ == "__main__":
    play_game()
