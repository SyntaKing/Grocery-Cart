import os

#Variable Delaration
price_list = {"Apple [1 PC]" : 69, "Banana [1 PC]" : 8.75, "Mango [1 PC]" : 27, "Blueberry [125 G]" : 125, "Avocado [1 PC]" : 69, "Potato [1 KG]" : 23, "Cucumber [500 G]" : 44, "Carrot [250 G]" : 9, "Onion [1 KG]" : 32}

fruits = ["Apple [1 PC]", "Banana [1 PC]", "Mango [1 PC]", "Blueberry [125 G]", "Avocado [1 PC]"]
vegetables = ["Potato [1 KG]", "Cucumber [500 G]", "Carrot [250 G]", "Onion [1 KG]"]

cart_items = []
quantity = []
cart = [cart_items, quantity]

total = 0.0

def viewCart():
    total = 0.0
    print("")
    for i in range(len(cart_items)):
        print(f"{cart_items[i]}  x  {quantity[i]}      ₹{float(price_list[cart_items[i]])*float(quantity[i])}")
        print("-------------------")
        total += float(price_list[cart_items[i]])*float(quantity[i])
    print(f"\nCart total:               ₹{total}")

def addToCart (list_name, item: int, item_quantity: int): 
    if list_name == 'fruits':
        if fruits[int(item)-1] in cart_items:
            index = cart_items.index(fruits[int(item)-1])
            quantity[index] = str(int(quantity[index]) + int(item_quantity))
        else:
            cart_items.append(fruits[int(item)-1])
            quantity.append(item_quantity)
    elif list_name == 'vegetables':
        if vegetables[int(item)-1] in cart_items:
            index = cart_items.index(vegetables[int(item)-1])
            quantity[index] = str(int(quantity[index]) + int(item_quantity))
        else:
            cart_items.append(vegetables[int(item)-1])
            quantity.append(item_quantity)        

# Logic execution
while True:
    while True:
        choice_main_menu = None
        choice_submenu_1 = None
        choice_submenu_2 = None
        item_quantity = None
        list_name = None

        #Main Menu
        os.system('cls')
        print("-----------Grocery Cart-----------")

        #View Cart
        if len(cart_items) == 0:
            print(f"\n\n          Cart is empty!\n\n\nCart total:               ₹{total}")
        else:
            viewCart()

        print("\n1. Add Item\n2. Remove Item\n3. Checkout\n\nA. Admin Panel\nQ. Quit")
        print("__________________________________")
        choice_main_menu = input()
        while (choice_main_menu == '') or ((choice_main_menu.lower() != 'q' and choice_main_menu.lower() != 'a') and (choice_main_menu> '3' or choice_main_menu< '1')) or len(choice_main_menu) > 1:
            os.system('cls')
            print("-----------Grocery Cart-----------")
            #View Cart
            if len(cart_items) == 0:
                print(f"\n\n          Cart is empty!\n\n\nCart total:               ₹{total}")
            else:
                viewCart()
            print("\n1. Add Item\n2. Remove Item\n3. Checkout\n\nA. Admin Panel\nQ. Quit\n\nINVALID INPUT!")
            print("__________________________________")
            choice_main_menu = input()
        
        #Quit
        if choice_main_menu.lower() == 'q':
            break

        #Add Item Menu
        while choice_main_menu == '1':
            os.system('cls')
            print("-----------Grocery Cart-----------")
            print("\n             ADD ITEM")
            print("\n1. Add Fruits\n2. Add Vegetables\n\n-  Previous menu")
            print("__________________________________")
            choice_submenu_1 = input()
            while (choice_submenu_1 != '-') and (choice_submenu_1 < '1' or choice_submenu_1 > '2'):
                os.system('cls')
                print("-----------Grocery Cart-----------")
                print("\n             ADD ITEM")
                print("\n1. Add Fruits\n2. Add Vegetables\n\n-  Previous menu")
                print("\nINVALID INPUT!")
                print("__________________________________")
                choice_submenu_1 = input()

            if choice_submenu_1 == '-':
                break

            while choice_submenu_1 == '1':
                os.system('cls')
                list_name = 'fruits'
                print("-----------Grocery Cart-----------")
                print("\n             ADD ITEM\n")
                serial = 1
                for i in fruits:
                    print(f"{serial}. {i}")
                    serial += 1
                serial -= 1
                print("\n\n-  Previous menu")
                print("__________________________________")
                choice_submenu_2 = input()
                while ((choice_submenu_2.isalpha == True) or (choice_submenu_2 < '1' or choice_submenu_2 > str(serial)) or len(choice_submenu_2) != len(str(serial))) and (choice_submenu_2 != '-'):
                    os.system('cls')
                    print("-----------Grocery Cart-----------")
                    print("\n             ADD ITEM\n")
                    serial = 1
                    for i in fruits:
                        print(f"{serial}. {i}")
                        serial += 1
                    serial -= 1
                    print("\n\n-  Previous menu")
                    print("\nINVALID INPUT")
                    print("__________________________________")
                    choice_submenu_2 = input()

                if choice_submenu_2 == '-':
                    break

                else:
                    os.system('cls')
                    print("-----------Grocery Cart-----------")
                    print("\n             ADD ITEM\n")
                    print("\nEnter quantity")
                    print("__________________________________")
                    item_quantity = input()
                    while item_quantity.isdigit() != True:
                        os.system('cls')
                        print("-----------Grocery Cart-----------")
                        print("\n             ADD ITEM\n")
                        print("\nEnter quantity")
                        print("\nINVALID INPUT")
                        print("__________________________________")
                        item_quantity = input()
                    addToCart(list_name, choice_submenu_2, item_quantity)

            while choice_submenu_1 == '2':
                os.system('cls')
                list_name = 'vegetables'
                print("-----------Grocery Cart-----------")
                print("\n             ADD ITEM\n")
                serial = 1
                for i in vegetables:
                    print(f"{serial}. {i}")
                    serial += 1
                serial -= 1
                print("\n\n-  Previous menu")
                print("__________________________________")
                choice_submenu_2 = input()
                while ((choice_submenu_2.isalpha == True) or (choice_submenu_2 < '1' or choice_submenu_2 > str(serial)) or len(choice_submenu_2) != len(str(serial))) and (choice_submenu_2 != '-'):
                    os.system('cls')
                    print("-----------Grocery Cart-----------")
                    print("\n             ADD ITEM\n")
                    serial = 1
                    for i in vegetables:
                        print(f"{serial}. {i}")
                        serial += 1
                    serial -= 1
                    print("\n\n-  Previous menu")
                    print("\nINVALID INPUT")
                    print("__________________________________")
                    choice_submenu_2 = input()

                if choice_submenu_2 == '-':
                    break

                else:
                    os.system('cls')
                    print("-----------Grocery Cart-----------")
                    print("\n             ADD ITEM\n")
                    print("\nEnter quantity")
                    print("__________________________________")
                    item_quantity = input()
                    while item_quantity.isdigit() != True:
                        os.system('cls')
                        print("-----------Grocery Cart-----------")
                        print("\n             ADD ITEM\n")
                        print("\nEnter quantity")
                        print("\nINVALID INPUT")
                        print("__________________________________")
                        item_quantity = input()
                    addToCart(list_name, choice_submenu_2, item_quantity)
                    
    #Exit confirmation
    os.system('cls')
    print("-----------Grocery Cart-----------")
    print("\nPress 'Q' again to confirm\nOR\nPress any other key to go back:")
    print("__________________________________")
    choice = input()
    if choice.lower() == 'q':
        os.system('cls')
        print("Thank you for using this app!")
        break