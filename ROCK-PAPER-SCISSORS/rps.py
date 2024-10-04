import random

CHOICES = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
WINNING_COMBOS = {
    'r': 's',  # Rock beats Scissors
    'p': 'r',  # Paper beats Rock
    's': 'p'   # Scissors beats Paper
}

def print_banner(text):
    """Prints a banner with stars for emphasis"""
    print(f"\n{'*' * 40}")
    print(f"{text.center(40)}")
    print(f"{'*' * 40}\n")

def get_player_choice():
    """Get valid user input and return it"""
    while True:
        print("Your Options:")
        print(" [R]ock")
        print(" [P]aper")
        print(" [S]cissors")
        print("-" * 40)
        player_choice = input('Make your choice: ').lower()
        if player_choice in CHOICES:
            return player_choice
        print("Invalid choice. Please select 'R', 'P', or 'S'.\n")

def get_computer_choice():
    """Randomly select from available choices for the computer"""
    return random.choice(list(CHOICES.keys()))

def print_winner(player_choice, computer_choice):
    """Determine and print the winner with a formatted output"""
    print("\n" + "=" * 40)
    print(f"Player chose: {CHOICES[player_choice]}")
    print(f"Computer chose: {CHOICES[computer_choice]}")
    print("=" * 40)

    if player_choice == computer_choice:
        print_banner("It's a DRAW!")
    elif WINNING_COMBOS[player_choice] == computer_choice:
        print_banner("Congratulations! You WIN!")
    else:
        print_banner("Computer WINS! Better luck next time.")

def play_game():
    """Play a single round of Rock-Paper-Scissors"""
    print_banner("Welcome to Rock-Paper-Scissors!")
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print_winner(player_choice, computer_choice)

if __name__ == "__main__":
    while True:
        play_game()
        print("-" * 40)
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print_banner("Thanks for playing!")
            break
