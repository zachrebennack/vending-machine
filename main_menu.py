import pandas as pd
from tabulate import tabulate as tb
    
def main_menu():
    menu_choice = 0
    welcome_message = "Welcome to the Virtual Vending Machine! \n"
    print(welcome_message)
    while menu_choice < 1 or menu_choice > 4:
        menu_choice = int(input("Please choose from the options below: \n1) View Inventory \n2) Deposit Money \n3) Return Change \n4) Exit \n"))
        if menu_choice == 1:
            print("You chose View Inventory\n")
            inventory_selection()
        elif menu_choice == 2:
            print("You chose Deposit Money\n")
            current_balance = deposit()
        elif menu_choice == 3:
            print("You chose Return Change\n")
        elif menu_choice == 4:
            print("Goodbye!")
            exit
        else:
            print("\nNot a valid choice.\n")

def inventory_selection():
    print("\nHere is the current inventory and item price:\n")

    # Read the CSV file into a DataFrame
    df = pd.read_csv('/home/zach/repos/vending-machine/inventory.csv')

    # Print the DataFrame as a table
    print(tb(df, headers='keys', tablefmt='fancy_grid'))

    # Get number of rows in table
    item_count = int(len(df))

    while True:
        inventory_selection = int(input("What would you like to purchase? "))
        if inventory_selection >= 0 and inventory_selection <= item_count:
            print("\n You chose: \n" + str(df.iloc[inventory_selection]) + "\n")
            is_choice = str(input("Is that correct? [y/n] "))
            if is_choice.lower == "y":
                # Going to add purchase function to complete transaction
                print("Great!")
                main_menu()
            elif is_choice.lower == "n":
                break
            else: 
                "\nTaking you back to inventory selection...\n" 
        else:
            print("Please enter a valid inventory number!")

def deposit():
    balance = 0
    while True:
        try: 
            bills = int(input("How much money in bills are you depositing? "))
            break #exit the loop if whole number entered
        except ValueError:
            print("Please enter a whole number!")
    balance += bills 
    while True:
        try: 
            quarters = int(input("How many quarters are you depositing? "))
            break #exit the loop if whole number entered
        except ValueError:
            print("Please enter a whole number!")
    balance += quarters * 0.25
    while True:
        try: 
            dimes = int(input("How many dimes are you depositing? "))
            break #exit the loop if whole number entered
        except ValueError:
            print("Please enter a whole number!")
    balance += dimes * 0.1
    while True:
        try: 
            nickels = int(input("How many nickels are you depositing? "))
            break #exit the loop if whole number entered
        except ValueError:
            print("Please enter a whole number!")
    balance += nickels * 0.05
    print("\nYou have entered $" + str(f"{balance:.2f}") + "\n")
    return balance

if __name__ == "__main__":
    main_menu()
