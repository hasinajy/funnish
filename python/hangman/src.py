from random import sample


def prompt_guess() -> None:
    user_guess = input("Enter your guess (one character): ")
    if len(user_guess) > 1:
        print("Please enter one character.")
        user_guess = prompt_guess()
    return user_guess


def get_word_state(to_guess: str, guessed_characters: list) -> str:
    word_state = ""
    for char in to_guess:
        if char in guessed_characters:
            word_state = word_state + char
        else:
            word_state = word_state + "_"
    return word_state


def display_title() -> None:
    print("Welcome to HANGMAN")


def play() -> None:
    WORD_DICTIONARY = ["python", "java", "javascript", "typescript"]
    MAX_MISTAKES = 3

    current_mistakes = 0
    word_to_guess = sample(population=WORD_DICTIONARY, k=1)[0]
    guessed_characters = []
    current_word_state: str = "_" * len(word_to_guess)

    display_title()

    while current_mistakes < MAX_MISTAKES:
        print("The current word state:", current_word_state)
        user_guess = prompt_guess()
        if user_guess in guessed_characters:
            print("You have already guessed the given character.")
        elif user_guess in word_to_guess:
            guessed_characters.append(user_guess)
            current_word_state = get_word_state(
                to_guess=word_to_guess, guessed_characters=guessed_characters
            )
            if current_word_state == word_to_guess:
                print("Congratulations! You found the hidden word:", current_word_state)
                break
        else:
            current_mistakes = current_mistakes + 1
            print("The given character is not found in the hidden word.")
            if current_mistakes == MAX_MISTAKES:
                print("Max mistakes reached. Try again next time!")


if __name__ == "__main__":
    play()
