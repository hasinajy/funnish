from random import randint

def display_difficulties():
    pass

game_over = False
to_guess: int = randint(0, 100)
print("Welcome to GUESS-THE-NUMBER")

while not game_over:
    user_guess = int(input("Enter your guess: "))
    if user_guess < to_guess:
        print("The hidden number is higher.")
    elif user_guess > to_guess:
        print("The hidden number is lower.")
    else:
        print("Congratulations! You guessed the hidden number.")
        game_over = True