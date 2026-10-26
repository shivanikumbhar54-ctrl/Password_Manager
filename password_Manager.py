import random
import string

passwords = {}

# Load existing passwords file safely
try:
    with open("passwords.txt", "r") as files:
        for line in files:
            if ":" in line:
                website, pwd = line.strip().split(":", 1) # Split on first colon only
                passwords[website] = pwd
except FileNotFoundError:
    pass

# Renamed to make it distinct and clear
def make_random_password():
    chars = string.ascii_letters + string.digits + "!@#$%"
    return "".join(random.choice(chars) for _ in range(8))

while True:
    print("\n----PERSONAL PASSWORDS MANAGER----")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        site = input("Enter Website : ").strip()
        pwd = input("Enter password: ").strip()

        passwords[site] = pwd

        with open("passwords.txt", "w") as file:
            for s, p in passwords.items():
                file.write(f"{s}:{p}\n")
        print("SAVED!")

    elif choice == "2":
        print("\n--- VIEW MODE ACTIVATED ---")
        if not passwords:
            print("No data found inside your password vault.")
        else:
            for site, pwd in passwords.items():
                print(f"Website: {site} | Password: {pwd}")
        input("\nPress Enter to go back to the menu...")

    # FIXED: Choice 3 now generates a password AND lets you save it directly to a site!
    elif choice == "3":
        print("\n--- GENERATE MODE ACTIVATED ---")
        new_password = make_random_password()
        print(f"Generated Password: {new_password}")
        
        save_choice = input("Do you want to save this password to a website? (yes/no): ").strip().lower()
        if save_choice == "yes" or save_choice == "y":
            site = input("Enter Website name: ").strip()
            if site:
                passwords[site] = new_password
                with open("passwords.txt", "w") as file:
                    for s, p in passwords.items():
                        file.write(f"{s}:{p}\n")
                print(f"Successfully saved to {site}!")
            else:
                print("Website name cannot be blank. Password not saved.")
        else:
            print("Password not saved.")
        
        input("\nPress Enter to go back to the menu...")

    elif choice == "4":
        print("Ok Byee..")
        break
        
    else:
        print("Invalid input! Try entering a number from 1 to 4.")
