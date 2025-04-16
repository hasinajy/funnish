from random import randint


DIFFICULTIES = ["Easy (0 - 100)", "Medium (0 - 500)", "Hard (0 - 1000)", "Custom Range"]
RANGES = [(0, 100), (0, 500), (0, 1000)]


def display_feedback(feedback: str) -> None:
    print(f"  {feedback}")


def prompt_number(prompt: str) -> int:
    try:
        return int(input(f"{prompt} "))
    except ValueError:
        display_feedback(feedback="Please enter a valid number.")
        return prompt_number(prompt=prompt)


def display_title() -> None:
    print("Welcome to GUESS-THE-NUMBER")


def quit() -> None:
    display_feedback(feedback="Bye!")
    exit(0)


def list_difficulties() -> None:
    print("\nHere are the game difficulties:")
    for index, difficulty in enumerate(DIFFICULTIES):
        print(f"\t{index + 1}. {difficulty}")
    print("\t0. Quit")


def prompt_difficulty() -> int:
    list_difficulties()
    difficulty_id = prompt_number(prompt="Enter the difficulty you want to play:") - 1
    
    if difficulty_id == -1:
        quit()
    elif difficulty_id < -1 or difficulty_id >= len(DIFFICULTIES): 
        display_feedback(feedback="Please enter a valid difficulty.")
        difficulty_id = prompt_difficulty()
    else:
        print(f"\nPlaying the game in {DIFFICULTIES[difficulty_id]} mode.")
    return difficulty_id


def get_number_to_guess(difficulty_id: int) -> int:
    if difficulty_id < len(RANGES): 
        lower_bound, higher_bound = RANGES[difficulty_id]
    else:
        lower_bound = prompt_number(prompt="Enter the lower bound:")
        higher_bound = prompt_number(prompt="Enter the higher bound:")
    return randint(lower_bound, higher_bound)


def prompt_yn(prompt: str) -> str:
    user_choice = input(f"\n{prompt} (y/n) : ")
    if user_choice.lower() not in ["y", "n"]:
        display_feedback(feedback="Please enter a valid choice.")
        user_choice = prompt_yn(prompt=prompt)
    return user_choice


def process_play_again(again_yn: str) -> None:
    if again_yn == "y":
        print()
        play()
    else:
        quit()


def play() -> None:
    display_title()
    
    guess_count = 0
    game_over = False
    difficulty_id = prompt_difficulty()
    to_guess = get_number_to_guess(difficulty_id=difficulty_id)

    while not game_over:
        user_guess = prompt_number(prompt="Enter your guess:")
        guess_count = guess_count + 1
        if user_guess < to_guess:
            display_feedback(feedback="The hidden number is higher.")
        elif user_guess > to_guess:
            display_feedback(feedback="The hidden number is lower.")
        else:
            display_feedback(feedback=f"Congratulations! You guessed the hidden number in {guess_count} attempts.")
            game_over = True
    
    again_yn = prompt_yn(prompt="Would you like to play again?")
    process_play_again(again_yn=again_yn) 


if __name__ == "__main__":
    play()