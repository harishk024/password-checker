import random
import string

# -------------------------------
# PASSWORD STRENGTH CHECKER
# -------------------------------

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak ❌"
    elif score == 3 or score == 4:
        return "Medium ⚠️"
    else:
        return "Strong ✅"


# -------------------------------
# PASSWORD GENERATOR
# -------------------------------

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# -------------------------------
# MAIN PROGRAM
# -------------------------------

def main():
    print("🔐 Password Tool")
    print("1. Check Password Strength")
    print("2. Generate Password")

    choice = input("Choose option (1/2): ")

    if choice == "1":
        user_password = input("Enter your password: ")
        result = check_password_strength(user_password)
        print("Password Strength:", result)

    elif choice == "2":
        length = int(input("Enter password length: "))
        new_password = generate_password(length)
        print("Generated Password:", new_password)

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
