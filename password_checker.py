import string

def check_password_strength(password):
    if len(password) < 8:
        return "Weak (Password length must be at least 8 characters)"
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    
    score = sum([has_upper, has_lower, has_digit, has_symbol])
    
    if score == 4 and len(password) >= 12:
        return "Strong (Password meets all security criteria)"
    elif score >= 3:
        return "Medium (Consider adding more character variety or length)"
    else:
        return "Weak (Does not meet complexity standards)"

if __name__ == "__main__":
    print("--- Password Strength Checker ---")
    print("Type 'exit' to stop the program.\n")
    
    while True:
        user_password = input("Enter a password to check: ")
        if user_password.lower() == 'exit':
            print("Exiting program... Good luck!")
            break
            
        result = check_password_strength(user_password)
        print(f"Result: {result}\n" + "-"*40)