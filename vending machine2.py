#ASCII art representing the name of application

print("""
██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝""")
# List of menu items
menu_list = [
    {"code": 1, "name": 'PEPSI', "price": 3},
    {"code": 2, "name": 'PRINGLES', "price": 4},
    {"code": 3, "name": 'ICED TEA', "price": 2.50},
    {"code": 4, "name": 'WATER', "price": 1},
    {"code": 5, "name": 'TWIX', "price": 3},
    {"code": 6, "name": 'CHEESEBALL CHIPS', "price": 5},
    {"code": 7, "name": 'OMAN CHIPS', "price": 2},
    {"code": 8, "name": 'STRAWBERRY MILK', "price": 2}
]

# It prints out the dictionary like a menu
menu_dict = {
    "1 PEPSI": "3 AED",
    "2 PRINGLES": "4 AED",
    "3 ICED TEA": "2.50 AED",
    "4 WATER": "1 AED",
    "5 TWIX": "3 AED",
    "6 CHEESEBALL CHIPS": "5 AED",
    "7 OMAN CHIPS": "2 AED",
    "8 STRAWBERRY MILK": "2 AED"
}

def food():
    # Displays a message by welcoming the user
    print('\t**\t WELCOME TO THE VENDING MACHINE \t**')
    print('      *   * BELOW IS THE GIVEN MENU *     *')
    for item, price in menu_dict.items():
        print(f" {item:10}, {price}")
    print()  # It prints out the dictionary like a menu

def place_order():
    # this is defining the place order system
    while True:
        food()
        # Asking the user to enter the amount
        print('=======================================\n')
        AED = float(input('Enter your Amount: '))
        print('=======================================\n')
        if AED <= 0:
            # If the amount is less than 0, it prints a message saying 'invalid amount'
            print('=====================================\n')
            print('YOU HAVE NOT ENTERED A VALID AMOUNT....please re-enter')
            print('===========================================\n')
            print('YOU HAVE ENTERED,', AED)  # Displays a message saying you have entered...AED
            continue

        # Asking the user to pick the item
        item_choice = int(input("Choose your item code: "))
        if item_choice <= 0 or item_choice > 8:
            # If the user inputs an item code more than 8 or less than 1, it shows a message "INVALID CODE"
            print('INVALID ITEM CODE...Please enter a valid item code')
            continue

        for z in menu_list:
            if item_choice == z['code']:
                if AED < z['price']:
                    print('=======================================\n')
                    print('YOU DON’T HAVE ENOUGH AED TO BUY THIS PRODUCT')
                    print('=======================================\n')
                else:
                    # Deducting price from AED or perform other necessary actions
                    AED -= z['price']
                    
                    # Display the item the user picked
                    print('=======================================')
                    print(f"You picked {z['name']}\n")
                    
                    # Dispenses the desired item using the tray
                    print('=======================================')
                    print("You will now receive your item through the dispense tray\n")
                    
                    # Thank the user for using the vending machine
                    print('=======================================')
                    print("Thank you for using the VENDING MACHINE :)\n")
                    print('=======================================')
                
                # Exiting the loop after finishing the order
                break

        break  # Exit the while loop after finishing the order

place_order()
