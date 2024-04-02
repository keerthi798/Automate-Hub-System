import random
import string

# def generate_registration_number():
#     # Generate a random registration number
#     letters = string.ascii_uppercase
#     digits = ''.join(random.choices(string.digits, k=4))
#     return ''.join(random.choices(letters, k=3)) + digits

def generate_registration_number():
    # Generate a random registration number following the format "KL<random_letters><random_digits>"
    letters = string.ascii_uppercase
    digits = ''.join(random.choices(string.digits, k=4))
    random_letters = ''.join(random.choices(letters, k=2))
    return f"KL{random_letters}{digits}"