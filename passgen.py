import string
import secrets
import sys

# character sets
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = "!@#$%^&*()-_=+"

def make_password(length=12):
    # pool with all allowed characters
    all_chars = lower + upper + digits + symbols
    
    # pick random characters securely
    password = "".join(secrets.choice(all_chars) for _ in range(length))
    return password

def check_strength(pwd):
    # basic scoring system
    score = 0
    if len(pwd) >= 10:
        score += 1
    if any(c in upper for c in pwd):
        score += 1
    if any(c in digits for c in pwd):
        score += 1
    if any(c in symbols for c in pwd):
        score += 1

    if score == 4:
        return "Strong"
    elif score >= 2:
        return "Medium"
    return "Weak"

def main():
    print("=== Simple Password Tool ===")
    print("1. Generate password")
    print("2. Check password strength")
    print("3. Exit")
    
    choice = input("Pick an option (1-3): ").strip()
    
    if choice == "1":
        user_len = input("Password length (press enter for 12): ").strip()
        length = int(user_len) if user_len.isdigit() else 12
        new_pwd = make_password(length)
        print(f"Your password: {new_pwd}")
        print(f"Strength: {check_strength(new_pwd)}")
        
    elif choice == "2":
        test_pwd = input("Enter a password to check: ").strip()
        print(f"Strength: {check_strength(test_pwd)}")
        
    elif choice == "3":
        print("Bye!")
        sys.exit(0)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()