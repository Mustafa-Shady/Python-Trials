import time

# Print a welcome message
print(">>>>>>>>>>>>>>> Welcome to Kebda Shop <<<<<<<<<<<<<<<<\n")

# Initialize the products dictionary with some default values
products = {
    "Kebda" : 25,
    "Sogo2" : 20,
    "Kofta" : 23,
    "Burger" : 35,
    "Zinger" : 30
}

# Admin mode function
def admin_mode():
    # Ask for the admin password
    password_attempts = 0  # Keep track of the number of password attempts
    while password_attempts < 3:
        password = input("Enter password: ")
        if password == Password:
            # If the password is correct, allow the admin to perform various actions
            print("\n1- Add a product")
            print("2- Remove a product")
            print("3- Edit price of a product")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                # Add a new product to the dictionary, or update the price if it already exists
                name = input("Enter the name of the product: ")
                price = int(input("Enter the price of the product: "))
                if name in products:
                    print("\nProduct already exists. Updating price...")
                products[name] = price
                print("\nProduct added/updated successfully!")
            elif choice == 2:
                # Remove an existing product from the dictionary
                name = input("Enter the name of the product: ")
                if name in products:
                    del products[name]
                    print("\nProduct removed successfully!")
                else:
                    print("\nProduct not found.")
            elif choice == 3:
                # Edit the price of an existing product
                name = input("Enter the name of the product: ")
                if name in products:
                    new_price = int(input("Enter the new price of the product: "))
                    products[name] = new_price
                    print("\nPrice updated successfully!")
                else:
                    print("\nProduct not found.")
            else:
                print("\nInvalid choice.")
            break  # Exit the loop if the admin entered the correct password
        else:
            print("\nInvalid password.")
            password_attempts += 1
            if password_attempts == 3:
                # If the admin entered the wrong password three times, lock the system for 5 minutes
                print("\nToo many incorrect password attempts. System locked for 5 minutes.")
                for i in range(5):
                    print("Time remaining:", 5 - i, "minutes")
                    time.sleep(60)
                password_attempts = 0  # Reset the password attempts counter

# Show products function
def show_products():
    # Iterate over the products dictionary and print each key-value pair
    print("\nProducts:")
    for name, price in products.items():
        print(name, "-", price)
    # Ask the user if they want to buy a product
    choice = input("\nDo you want to buy a product? (y/n) ")
    if choice.lower() == "y":
        buy_product()

# Buy a product function
def buy_product():
    # Ask the user for the name of the product they want to buy
    name = input("\nEnter the name of the product: ")
    if name in products:
        # If the product is found, ask for the quantity and calculate the total price
        price = products[name]
        print("Price:", price)
        quantity = int(input("Enter the quantity: "))
        total = price * quantity
        print("Total:", total)
        # Add the purchase to the bill
        global bill  # Use the 'global' keyword to modify the global variable
        bill.append((name, quantity, total))
    else:
        print("\nProduct not found.")

# Remove a product from the bill function
def remove_product():
    # Ask the user for the name of the product they want to remove
    name = input("\nEnter the name of the product to remove: ")
    removed = False
    for i in range(len(bill)):
        if bill[i][0] == name:
            # If the product is found, remove it from the bill and set the 'removed' flag to True
            del bill[i]
            removed = True
            print("\nProduct removed successfully!")
            break
    if not removed:
        print("\nProduct not found.")

# Print bill function
def print_bill():
    # Print the bill for the customer
    print("\nBill:")
    total = 0
    for name, quantity, price in bill:
        print(name, "x", quantity, "=", price)
        total += price
    print("Total:", total)

# Main loop
Password = "0000"
bill = []
flag = True
while flag:
    # Ask the user what action they want to take
    mode = int(input("\nPlease Enter \n1- for Admin Mode\n2- to show the products\n3- buy a product\n4- remove a product\n5- print bill\n6- exit "))
    if mode == 1:
        admin_mode()
    elif mode == 2:
        show_products()
    elif mode == 3:
        buy_product()
    elif mode == 4:
        remove_product()
    elif mode == 5:
        print_bill()
    elif mode == 6:
        # Exit the program
        flag = False
        print("\nGoodbye!")
    else:
        print("\nInvalid choice.")
    # Add a 1-second delay before the next iteration of the loop
    time.sleep(1)
    