from random import randint


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


def prompt_difficulty() -> int:
    print("\nHere are the game difficulties:")
    print("\t1. Easy (0 - 100)")
    print("\t2. Medium (0 - 500)")
    print("\t3. Hard (0 - 1000)")
    print("\t4. Custom range")
    difficulty_id = prompt_number(prompt="Enter the difficulty you want to play:") - 1
    
    difficulties = ["Easy", "Medium", "Hard", "Custom"]
    if difficulty_id < 0 or difficulty_id >= len(difficulties): 
        display_feedback(feedback="Please enter a valid difficulty.")
        prompt_difficulty()
    else:
        print(f"\nPlaying the game in {difficulties[difficulty_id]} mode.")
        return difficulty_id


def get_number_to_guess(difficulty_id: int) -> int:
    ranges = [(0, 100), (0, 500), (0, 1000)]
    if difficulty_id < len(ranges): 
        lower_bound, higher_bound = ranges[difficulty_id]
    else:
        lower_bound = prompt_number(prompt="Enter the lower bound:")
        higher_bound = prompt_number(prompt="Enter the higher bound:")
    return randint(lower_bound, higher_bound)


def prompt_yn(prompt: str) -> str:
    user_choice = input(f"{prompt} (y/n) : ")
    if user_choice.lower() not in ["y", "n"]:
        display_feedback(feedback="Please enter a valid choice.")
        user_choice = prompt_yn(prompt=prompt)
    return user_choice


def process_play_again(again_yn: str) -> None:
    if again_yn == "y":
        play()
    else:
        display_feedback(feedback="Bye!")


def play() -> None:
    game_over = False
    display_title()
    difficulty_id = prompt_difficulty()
    to_guess = get_number_to_guess(difficulty_id=difficulty_id)

    while not game_over:
        user_guess = prompt_number(prompt="Enter your guess:")
        if user_guess < to_guess:
            display_feedback(feedback="The hidden number is higher.")
        elif user_guess > to_guess:
            display_feedback(feedback="The hidden number is lower.")
        else:
            display_feedback(feedback="Congratulations! You guessed the hidden number.")
            game_over = True
    
    again_yn = prompt_yn(prompt="Would you like to play again?")
    process_play_again(again_yn=again_yn) 


if __name__ == "__main__":
    play()