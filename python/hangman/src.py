import os
from random import sample

DEFAULT_DICTIONARY = ["python", "java", "javascript", "typescript"]
MAX_MISTAKES = 3


def display_feedback(feedback: str) -> None:
    """Display feedback to the user with indentation."""
    print(f"  {feedback}")


def prompt_guess() -> str:
    """Prompt the user for a single letter guess, validating input."""
    while True:
        guess = input("Enter your guess (one letter): ").lower()
        if len(guess) != 1:
            display_feedback("Please enter exactly one character.")
        elif not guess.isalpha():
            display_feedback("Please enter a letter (A-Z).")
        else:
            return guess


def get_word_state(word_to_guess: str, guessed_letters: list[str]) -> str:
    """Return the current state of the word with guessed letters revealed."""
    return "".join(char if char in guessed_letters else "_" for char in word_to_guess)


def display_title() -> None:
    """Display the game title."""
    print("Welcome to HANGMAN")


def display_letter_count(word_to_guess: str, guess: str) -> None:
    """Display the number of occurrences of the guessed letter in the word."""
    count = word_to_guess.count(guess)
    display_feedback(
        f"{count} {'instance' if count == 1 else 'instances'} found in the hidden word."
    )


def load_dictionary(filename: str = "dictionary.txt") -> list[str]:
    """Load a list of words from a file or use the default dictionary."""
    if not os.path.exists(filename):
        display_feedback("Dictionary file not found. Using default dictionary.")
        return DEFAULT_DICTIONARY

    try:
        with open(filename, "r", encoding="utf-8") as file:
            words = [line.strip().lower() for line in file if line.strip()]
            if not words:
                display_feedback("Dictionary file is empty. Using default dictionary.")
                return DEFAULT_DICTIONARY
            return words
    except (FileNotFoundError, UnicodeDecodeError):
        display_feedback("Error reading dictionary file. Using default dictionary.")
        return DEFAULT_DICTIONARY


def play_round(word_to_guess: str) -> bool:
    """Play one round of Hangman, returning True if the player wins."""
    guessed_letters = []
    word_state = "_" * len(word_to_guess)
    mistakes = 0

    while mistakes < MAX_MISTAKES:
        print("\nCurrent word state:", word_state)
        guess = prompt_guess()

        if guess in guessed_letters:
            display_feedback("You already guessed that letter.")
            continue

        guessed_letters.append(guess)
        if guess in word_to_guess:
            display_letter_count(word_to_guess, guess)
            word_state = get_word_state(word_to_guess, guessed_letters)
            if word_state == word_to_guess:
                display_feedback(f"Congratulations! You found the word: {word_state}")
                return True
        else:
            mistakes += 1
            display_feedback(
                f"Letter not in word. {MAX_MISTAKES - mistakes} mistakes remaining."
            )
            if mistakes == MAX_MISTAKES:
                display_feedback(f"Game over! The word was: {word_to_guess}")
                return False


def play() -> None:
    """Run the Hangman game."""
    display_title()
    dictionary = load_dictionary()
    word_to_guess = sample(dictionary, 1)[0]
    play_round(word_to_guess)


if __name__ == "__main__":
    play()
