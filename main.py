import os

#Variable Delaration
inventory_fruits = {"Apple" : 69, "Banana" : 8.75}

items = []
quantity = []
cart = [items, quantity]

total = 0

# Logic execution
while True:
    while True:
        #Main Menu
        os.system('cls')
        print("-----------Grocery Cart-----------")
        if len(items) == 0:
            print(f"\n\n          Cart is empty!\n\n\nTotal amount: ₹{total}")
        print("\n1. Add Item\n2. Remove Item\n3. Checkout\n\nA. Admin Panel\nQ. Quit\n__________________________________")
        choice = input()
        while (choice == '') or ((choice.lower() != 'q' and choice.lower() != 'a') and (choice> '3' or choice< '1')) or len(choice) > 1:
            os.system('cls')
            print("-----------Grocery Cart-----------")
            if len(items) == 0:
                print(f"\n\n          Cart is empty!\n\n\nTotal amount: ₹{total}")
            print("\n1. Add Item\n2. Remove Item\n3. Checkout\n\nA. Admin Panel\nQ. Quit\n\nINVALID CHOICE!\n__________________________________")
            choice = input()
        
        #Quit
        if choice.lower() == 'q':
            break

    #Exit confirmation
    os.system('cls')
    print("-----------Grocery Cart-----------")
    print("\nPress 'Q' again to confirm\nOR\nPress any other key to go back:\n__________________________________")
    choice = input()
    if choice.lower() == 'q':
        os.system('cls')
        print("Thank you for using this app!")
        break