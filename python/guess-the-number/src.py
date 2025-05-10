from random import randint

DIFFICULTY_RANGES = {
    "Easy (0 - 100)": (0, 100),
    "Medium (0 - 500)": (0, 500),
    "Hard (0 - 1000)": (0, 1000),
    "Custom Range": None,
}


def display_feedback(feedback: str) -> None:
    """Display feedback to the user with consistent formatting."""
    print(f"  {feedback}")


def prompt_number(prompt: str) -> int:
    """Prompt the user for a number and validate input."""
    while True:
        try:
            return int(input(f"{prompt} "))
        except ValueError:
            display_feedback("Please enter a valid number.")


def display_title() -> None:
    """Display the game title."""
    print("\n=== Welcome to GUESS-THE-NUMBER ===")


def list_difficulties() -> None:
    """Display available difficulty options."""
    print("\nGame difficulties:")
    for index, difficulty in enumerate(DIFFICULTY_RANGES, 1):
        print(f"\t{index}. {difficulty}")
    print("\t0. Quit")


def prompt_difficulty() -> tuple[int, str]:
    """Prompt user to select a difficulty and return its index and name."""
    while True:
        list_difficulties()
        choice = prompt_number("Enter the difficulty you want to play:")
        if choice == 0:
            display_feedback("Bye!")
            exit(0)
        if 1 <= choice <= len(DIFFICULTY_RANGES):
            difficulty = list(DIFFICULTY_RANGES.keys())[choice - 1]
            print(f"\nPlaying in {difficulty} mode.")
            return choice - 1, difficulty
        display_feedback("Please enter a valid difficulty.")


def get_number_to_guess(difficulty_id: int, difficulty: str) -> int:
    """Generate a random number to guess based on the difficulty."""
    if DIFFICULTY_RANGES[difficulty] is not None:
        lower_bound, higher_bound = DIFFICULTY_RANGES[difficulty]
    else:
        lower_bound = prompt_number("Enter the lower bound:")
        higher_bound = prompt_number("Enter the higher bound:")
        if lower_bound >= higher_bound:
            display_feedback("Lower bound must be less than higher bound.")
            return get_number_to_guess(difficulty_id, difficulty)
    return randint(lower_bound, higher_bound)


def prompt_yes_no(prompt: str) -> bool:
    """Prompt the user for a yes/no choice and return a boolean."""
    while True:
        choice = input(f"\n{prompt} (y/n): ").lower()
        if choice in ["y", "n"]:
            return choice == "y"
        display_feedback("Please enter 'y' or 'n'.")


def play_round(number_to_guess: int) -> bool:
    """Run the guessing loop for a single round and return whether to play again."""
    guess_count = 0
    while True:
        guess = prompt_number("Enter your guess:")
        guess_count += 1
        if guess < number_to_guess:
            display_feedback("The hidden number is higher.")
        elif guess > number_to_guess:
            display_feedback("The hidden number is lower.")
        else:
            display_feedback(
                f"Congratulations! You guessed the number in {guess_count} attempts."
            )
            break
    return prompt_yes_no("Would you like to play again?")


def play() -> None:
    """Initialize and manage game rounds."""
    while True:
        display_title()
        difficulty_id, difficulty = prompt_difficulty()
        number_to_guess = get_number_to_guess(difficulty_id, difficulty)
        if not play_round(number_to_guess):
            break
    display_feedback("Thanks for playing!")


if __name__ == "__main__":
    play()
