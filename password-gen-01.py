import random
import string

def generate_password(length=12):
    # Define the possible characters in the password
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    all_chars = letters + digits + special_chars

    # Ensure the password has at least one letter, digit, and special character
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_chars, k=length-3)

    # Shuffle the list to ensure randomness
    random.shuffle(password)

    # Join the list to form the final password string
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    password_length = 12  # You can change the length as needed
    password = generate_password(password_length)
    print(f"Generated password: {password}")
