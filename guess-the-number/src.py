from random import randint

def display_title():
    print("Welcome to GUESS-THE-NUMBER")

def prompt_difficulty():
    print("\nHere are the game difficulties:")
    print("\t1. Easy (0 - 100)")
    print("\t2. Medium (0 - 500)")
    print("\t3. Hard (0 - 1000)")
    print("\t4. Custom range")
    difficulty_id = int(input("Enter the difficulty you want to play: ")) - 1
    
    difficulties = ["Easy", "Medium", "Hard", "Custom"]
    if difficulty_id < 0 or difficulty_id >= len(difficulties): 
        print("Please enter a valid difficulty.")
        prompt_difficulty()
    else:
        print(f"\nPlaying the game in {difficulties[difficulty_id]} mode.")
        return difficulty_id

def get_number_to_guess(difficulty_id: int):
    ranges = [(0, 100), (0, 500), (0, 1000)]
    
    if difficulty_id < len(ranges): 
        lower_bound, higher_bound = ranges[difficulty_id]
    else:
        lower_bound = int(input("Enter the lower bound: "))
        higher_bound = int(input("Enter the higher bound: "))
    return randint(lower_bound, higher_bound)

game_over = False
display_title()
difficulty_id = prompt_difficulty()
to_guess = get_number_to_guess(difficulty_id=difficulty_id)

while not game_over:
    user_guess = int(input("Enter your guess: "))
    if user_guess < to_guess:
        print("  The hidden number is higher.")
    elif user_guess > to_guess:
        print("  The hidden number is lower.")
    else:
        print("  Congratulations! You guessed the hidden number.")
        game_over = True