import random
import string

def generate_password(length=12):

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    password = []
    password.append(random.choice(lowercase_letters))
    password.append(random.choice(uppercase_letters))
    password.append(random.choice(digits))
    password.append(random.choice(special_characters))

    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    password_str = ''.join(password)
    
    return password_str

def main():
    print("Welcome to Advanced Password Generator!")
    length = int(input("Enter the length of the password you want to generate: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
