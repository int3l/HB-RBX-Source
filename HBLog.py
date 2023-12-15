import os
import msvcrt  # For Windows OS
from colorama import init, Fore, Style

init(autoreset=True)  # Initialize colorama

# Function to add a new account
def add_account(username, password, database):
    if username in database:
        print("Username already exists. Please choose another one.")
    else:
        database[username] = password
        print("Account added successfully!")
        return True  # Return True to hide options

# Function to display all accounts in green color with numbers
def display_accounts(database):
    if not database:
        print("No accounts found.")
    else:
        print(Fore.GREEN + "***** ACCOUNT LIST *****")
        for i, (username, password) in enumerate(database.items(), start=1):
            print(f"{i}- Username: {Fore.GREEN}{username.ljust(20)}{Style.RESET_ALL} Password: {Fore.GREEN}{password}{Style.RESET_ALL}")
        print("************************" + Style.RESET_ALL)

# Function to get masked input
def get_masked_input(prompt):
    print(prompt, end='', flush=True)

    password = ""
    while True:
        key = ord(msvcrt.getch())

        if key == 13:  # Enter key pressed
            print()
            break
        elif key == 8:  # Backspace key pressed
            if password:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        else:
            char = chr(key)
            password += char
            print('*', end='', flush=True)

    return password

# Function to load accounts from a file
def load_accounts(filename):
    accounts = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                username, password = line.strip().split(':')
                accounts[username] = password
    except FileNotFoundError:
        pass  # If file doesn't exist, proceed with an empty dictionary
    return accounts

# Function to save accounts to a file
def save_accounts(filename, database):
    with open(filename, 'w') as file:
        for username, password in database.items():
            file.write(f"{username}:{password}\n")

# Database filename
database_file = "accounts.txt"

# Load accounts from the file
user_database = load_accounts(database_file)

# Example usage:
while True:
    print("\n1. Add Account")
    print("2. Display Account List")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        new_username = input("Enter new username: ")
        new_password = get_masked_input("Enter password: ")
        if add_account(new_username, new_password, user_database):
            save_accounts(database_file, user_database)
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear console after adding an account

    elif choice == '2':
        display_accounts(user_database)

    elif choice == '3':
        save_accounts(database_file, user_database)  # Save before exiting
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
