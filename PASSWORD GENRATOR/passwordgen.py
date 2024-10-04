import random
import string

def print_banner(text):
    """Prints a stylish banner with stars"""
    print(f"\n{'*' * 50}")
    print(f"{text.center(50)}")
    print(f"{'*' * 50}\n")

def get_password_length():
    """Prompts the user for password length and validates input"""
    while True:
        try:
            length = int(input("Enter the password length (e.g., 8, 12, 16): "))
            if length < 4:
                print("Password length should be at least 4 characters. Try again.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

def get_user_preferences():
    """Ask the user what kind of characters to include in the password"""
    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    if not (include_upper or include_lower or include_numbers or include_special):
        print("You must select at least one character type. Please try again.\n")
        return get_user_preferences()
    
    return include_upper, include_lower, include_numbers, include_special

def generate_password(length, include_upper, include_lower, include_numbers, include_special):
    """Generate a password based on user's preferences"""
    characters = ""
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    """Main function to drive the password generator"""
    print_banner("Welcome to the Super Password Generator")
    
    # Get user preferences for password generation
    length = get_password_length()
    include_upper, include_lower, include_numbers, include_special = get_user_preferences()

    # Generate the password
    password = generate_password(length, include_upper, include_lower, include_numbers, include_special)

    # Display the result
    print_banner("Your Secure Password")
    print(f"Generated Password: {password}")
    print(f"{'*' * 50}\n")

if __name__ == "__main__":
    password_generator()

    # Option to generate again
    while True:
        play_again = input("Do you want to generate another password? (y/n): ").lower()
        if play_again == 'y':
            password_generator()
        else:
            print_banner("Thanks for using the Password Generator!")
            break
