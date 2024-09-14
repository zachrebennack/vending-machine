import pandas as pd
    
def main_menu():
    menu_choice = 0
    welcome_message = "Welcome to the Virtual Vending Machine! \n"
    print(welcome_message)
    while menu_choice < 1 or menu_choice > 4:
        menu_choice = int(input("Please choose from the options below: \n1) View Inventory \n2) Deposit Money \n3) Return Change \n4) Exit \n"))
        if menu_choice == 1:
            print("You chose View Inventory")
            inventory_selection()
        elif menu_choice == 2:
            print("You chose Deposit Money")
            deposit()
        elif menu_choice == 3:
            print("You chose Return Change")
        elif menu_choice == 4:
            print("Goodbye!")
        else:
            print("\nNot a valid choice.\n")

def inventory_selection():
    print("\nHere is the current inventory and item price:\n")

    # Read the CSV file into a DataFrame
    df = pd.read_csv('/home/zach/repos/vending-machine/inventory.csv')

    # Print the DataFrame as a table
    print(df)

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
            quarters = float(input("How many quarters are you depositing? "))
            break #exit the loop if whole number entered
        except ValueError:
            print("Please enter a whole number!")
    balance += quarters * 0.25
    while True:
        try: 
            dimes = float(input("How many dimes are you depositing? "))
            break #exit the loop if whole number entered
        except ValueError:
            print("Please enter a whole number!")
    balance += dimes * 0.1
    while True:
        try: 
            nickels = float(input("How many nickels are you depositing? "))
            break #exit the loop if whole number entered
        except ValueError:
            print("Please enter a whole number!")
    balance += nickels * 0.05
    print("\nYou have entered $" + str(f"{balance:.2f}") + "\n")
    main_menu()

if __name__ == "__main__":
    main_menu()
