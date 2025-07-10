import os

#Item Declaration
inventory_fruits = {"Apple" : 69, "Banana" : 8.75}
cart = []

# Logic execution
while True:
    os.system('cls')
    #Main Menu
    while True:
        print("-------Grocery Cart-------")
        print("\n1. View Cart\n2.Add Item\n3.Remove Item\nQ. Quit program\n__________________________")
        choice = input()
        if choice.lower() == 'q':
            break
    
    #Exit confirmation
    os.system('cls')
    print("Press 'Q' again to confirm:\n__________________________")
    choice = input()
    if choice.lower() == 'q':
        os.system('cls')
        print("Thank you for using this app!")
        break