def prompt_guess() -> None:
    user_guess = input("Enter your guess: ")
    if len(user_guess) > 1:
        print("Please enter one character.")
        user_guess = prompt_guess()
    return user_guess


def display_word_state(to_guess: str, guessed_characters: list) -> None:
    for char in to_guess:
        if char in guessed_characters:
            print(char, end="")
        else:
            print("_", end="")
    print()


WORD_TO_GUESS = "hangman"
hp = 7
correct_guesses = []

while hp:
    user_guess = prompt_guess()
    if user_guess not in WORD_TO_GUESS:
        print("The hidden does not contain the specified character.")
        hp = hp - 1
    else:
        correct_guesses.append(user_guess)
        display_word_state(to_guess=WORD_TO_GUESS, guessed_characters=correct_guesses)
