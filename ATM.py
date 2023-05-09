# Define customer data
Custmer1 = {
    "ID": "ALAA",
    "PASS": "0101",
    "Amount": 1000000
}

Custmer2 = {
    "ID": "MOSTAFA",
    "PASS": "1010",
    "Amount": 1000000
}

Custmer3 = {
    "ID": "SHADY",
    "PASS": "1001",
    "Amount": 1000000
}

# Define the available operations and currencies
operation = ("Withdraw", "Deposit", "Display Information")
currency = ("KWD", "LE", "USD", "EUR")
flagcontrol = ("NO", "YES")

# Set the number of login tries
Tries = 3

# Starting the program
while Tries > 0:
    flag = 1
    id = input("Please Enter Your Name ID: ")

    # Check if the ID is valid
    if id == Custmer1["ID"]:
        while flag == 1 and Tries > 0:
            print(Tries, "Tries Left")
            ps = input("Please Enter Your Account Password: ")

            # Check if the password is valid
            if ps == Custmer1["PASS"]:
                Tries = 3
                while flag == 1 and Tries > 0:
                    op = input("Please enter operation type (Withdraw/Deposit/Display Information): ")

                    # Withdraw operation
                    if op == operation[0]:
                        print("Withdrawing>>>>")
                        w = int(input("Please Enter the USD amount to Withdraw: "))
                        if w <= Custmer1["Amount"]:
                            Custmer1["Amount"] -= w
                        else:
                            print("Balance is not enough")

                    # Deposit operation
                    elif op == operation[1]:
                        print("Depositing<<<<<")
                        cur = input("Please enter deposit currency KWD/LE/USD/EUR are supported  ")
                        if cur == currency[0]:  # KWD
                            dep = input("Please enter deposit in Kuwaiti Dinar currency: ")
                            dep = int(dep)
                            Custmer1["Amount"] = Custmer1["Amount"] + dep * 3
                        elif cur == currency[1]:  # LE
                            dep = input("Please enter deposit in Egyptian Bound currency: ")
                            dep = int(dep)
                            Custmer1["Amount"] = Custmer1["Amount"] + dep / 30
                        elif cur == currency[2]:  # USD
                            dep = input("Please enter deposit in Unitid State Dollar currency: ")
                            dep = int(dep)
                            Custmer1["Amount"] += dep
                        elif cur == currency[3]:  # EUR
                            dep = input("Please enter deposit in Euro currency: ")
                            dep = int(dep)
                            Custmer1["Amount"] += dep
                        else:
                            print("Currency not Accepted")

                    # Display information operation
                    elif op == operation[2]:
                        print("Name: ", Custmer1["ID"])
                        print("Amount in USD: ", Custmer1["Amount"])
                    else:
                        print("Invalid Operation")

                    # Check if the user wants to do another operation
                    ex = input("Do another operation YES/NO?  ")
                    if ex == flagcontrol[1]:
                        flag = 1
                    elif ex == flagcontrol[0]:
                        flag = 0

            else:
                print("Invalid Password")
                Tries -= 1

    elif id == Custmer2["ID"]:
        while flag == 1 and Tries > 0:
            print(Tries, "Tries Left")
            ps = input("Please Enter Your Account Password: ")
            if ps == Custmer2["PASS"]:
                Tries = 3
                while flag == 1 and Tries > 0:
                    op = input("Please enter operation type (Withdraw/Deposit/Display Information): ")
                    if op == operation[0]:
                        print("Withdrawing>>>>")
                        w = int(input("Please Enter the USD amount to Withdraw: "))
                        if w <= Custmer2["Amount"]:
                            Custmer2["Amount"] -= w
                        else:
                            print("Balance is not enough")
                    elif op == operation[1]:
                        print("Depositing<<<<<")
                        cur = input("Please enter deposit currency KWD/LE/USD/EUR are supported  ")
                        if cur == currency[0]:  # KWD
                            dep = input("Please enter deposit in Kuwaiti Dinar currency: ")
                            dep = int(dep)
                            Custmer2["Amount"] = Custmer2["Amount"] + dep * 3
                        elif cur == currency[1]:  # LE
                            dep = input("Please enter deposit in Egyptian Bound currency: ")
                            dep = int(dep)
                            Custmer2["Amount"] = Custmer2["Amount"] + dep / 30
                        elif cur == currency[2]:  # USD
                            dep = input("Please enter deposit in Unitid State Dollar currency: ")
                            dep = int(dep)
                            Custmer2["Amount"] += dep
                        elif cur == currency[3]:  # EUR
                            dep = input("Please enter deposit in Euro currency: ")
                            dep = int(dep)
                            Custmer2["Amount"] += dep
                        else:
                            print("Currency not Accepted")
                    elif op == operation[2]:
                        print("Name: ", Custmer2["ID"])
                        print("Amount in USD: ", Custmer2["Amount"])
                    else:
                        print("Invalid Operation")
                    ex = input("Do another operation YES/NO?  ")
                    if ex == flagcontrol[1]:
                        flag = 1
                    elif ex == flagcontrol[0]:
                        flag = 0
            else:
                print("Invalid Password")
                Tries -= 1
    elif id == Custmer3["ID"]:
        while flag == 1 and Tries > 0:
            print(Tries, "Tries Left")
            ps = input("Please Enter Your Account Password: ")
            if ps == Custmer3["PASS"]:
                Tries = 3
                while flag == 1 and Tries > 0:
                    op = input("Please enter operation type (Withdraw/Deposit/Display Information): ")
                    if op == operation[0]:
                        print("Withdrawing>>>>")
                        w = int(input("Please Enter the USD amount to Withdraw: "))
                        if w <= Custmer3["Amount"]:
                            Custmer3["Amount"] -= w
                        else:
                            print("Balance is not enough")
                    elif op == operation[1]:
                        print("Depositing<<<<<")
                        cur = input("Please enter deposit currency KWD/LE/USD/EUR are supported  ")
                        if cur == currency[0]:  # KWD
                            dep = input("Please enter deposit in Kuwaiti Dinar currency: ")
                            dep = int(dep)
                            Custmer3["Amount"] = Custmer3["Amount"] + dep * 3
                        elif cur == currency[1]:  # LE
                            dep = input("Please enter deposit in Egyptian Bound currency: ")
                            dep = int(dep)
                            Custmer3["Amount"] = Custmer3["Amount"] + dep / 30
                        elif cur == currency[2]:  # USD
                            dep = input("Please enter deposit in Unitid State Dollar currency: ")
                            dep = int(dep)
                            Custmer3["Amount"] += dep
                        elif cur == currency[3]:  # EUR
                            dep = input("Please enter deposit in Euro currency: ")
                            dep = int(dep)
                            Custmer3["Amount"] += dep
                        else:
                            print("Currency not Accepted")
                    elif op == operation[2]:
                        print("Name: ", Custmer3["ID"])
                        print("Amount in USD: ", Custmer3["Amount"])
                    else:
                        print("Invalid Operation")
                    ex = input("Do another operation YES/NO?  ")
                    if ex == flagcontrol[1]:
                        flag = 1
                    elif ex == flagcontrol[0]:
                        flag = 0
            else:
                print("Invalid Password")
                Tries -= 1
    else:
        print("Invalid Customer ID")
        

print("Card Blocked")