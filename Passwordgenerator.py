import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on specified criteria."""
    character_pool = ''
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("No character types selected! Please select at least one.")

    return ''.join(random.choice(character_pool) for _ in range(length))

def main():
    print("Welcome to the Command-line Password Generator!")

    try:
        length = int(input("Enter password length: "))
        
        if length <= 0:
            print("Password length must be a positive integer.")
            return

        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid input.")

if __name__ == "__main__":
    main()