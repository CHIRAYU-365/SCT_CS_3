import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    print(f"Password Strength: {strength}")
    print("Criteria Met:")
    print(f" - Minimum Length (8+): {'✔' if length_criteria else '✘'}")
    print(f" - Uppercase Letter: {'✔' if upper_criteria else '✘'}")
    print(f" - Lowercase Letter: {'✔' if lower_criteria else '✘'}")
    print(f" - Digit: {'✔' if digit_criteria else '✘'}")
    print(f" - Special Character: {'✔' if special_criteria else '✘'}")

# Example usage
password = input("Enter your password: ")
check_password_strength(password)
