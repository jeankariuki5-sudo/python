users =[
    {"Username" : "John", "Password" : "john123", "Balance": 5000},
    {"Username" : "Mary", "Password" : "mary123", "Balance": 1200},
    {"Username" : "Peter", "Password" : "peter123", "Balance": 0}
]

logged_in = None

def deposit(account):
    print("==========================")
    print("Deposit")
    print("==========================")

    amount = float(input("Enter the amount You would wish to Deposit: Ksh "))
    if amount > 0:
        current_acc["Balance"] += amount
        return f"Ksh {amount} has successfully deposited into your account. Current balance Ksh: {current_acc["Balance"]}"
    else:
       return "Invalid amount"

def withdraw(account):
    print("==========================")
    print("Withdraw")
    print("==========================")

    amount = float(input("Enter the amount your wold wish to withdraw: Ksh "))
    if amount <= 0:
        return "Invalid amount"
    elif amount > current_acc["Balance"]:
        return "Insufficient Funds"
    else:
        current_acc["Balance"] -= amount
        return f"Ksh {amount} has succesfully been withdrawn fron your account. Current balance Ksh {current_acc["Balance"]}"



# Welcome Menu
while True:
    if logged_in is None:
        print("==========================")
        print("SOKO BANK")
        print("==========================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        print("==========================")

        option = input("Enter Your Choice: ")

        # Creating account
        if option == "1":
            print("==========================")
            print("Create an Account")
            print("==========================")

            user_name = input("Choose a username: ")

            user_exist = False
            for account in users:
                if account["Username"] == user_name:
                    user_exist = True
            if user_exist:
                print("Username already exists. Try a different username")
            else:
                password = input("Choose a password: ")
                new_account = {"Username" : user_name, "Password" : password, "Balance" : 0}
                users.append(new_account)
                print(f"Your account has been created. Welcome {user_name}!")
                logged_in = user_name

        # login
        elif option == "2":
            print("==========================")
            print("Login")
            print("==========================")

            trial = 3

            while trial > 0:
                user_name = input("Enter your Username: ")
                password = input("Enter your password: ")

                for account in users:
                    if account["Username"] == user_name and account["Password"] == password:
                        logged_in = user_name
                        break

                if logged_in:
                    print(f"Welcome Back, {logged_in}")
                    break
                else:
                    trial -=1
                    if trial > 0:
                        print(f"Wrong credentials. You have {trial} trials remaining")
                        break
                    else:
                        print("Too many Failed attempts. You have been logged out")

        # Exit
        elif option == "3":
            print("Thank You for choosing Soko Bank. Good bye!")
            break
    
        else:
            print("Invalid choice. Please select 1, 2 or 3")

    # Banking menu
    else:
        current_acc = None
        for account in users:
            if account["Username"] == logged_in:
                current_acc = account
                 

        print("==========================")
        print(f"SOKO BANK | {logged_in}")
        print("==========================")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        print("==========================")

        choice = input("Enter your choice: ")

        # Deposit
        if choice == "1":
            depo = deposit(current_acc)
            print(depo)

        # Withdraw
        elif choice == "2":
            wth = withdraw(current_acc)
            print(wth)

        # Check balance
        elif choice == "3":
            print("==========================")
            print("Balance")
            print("==========================")

            print(f"Current Balance: Ksh {current_acc["Balance"]}")

        # Exit
        elif choice == "4":
            print("==========================")
            print("SOKO BANK")
            print("==========================")

            print(f"Good Bye, {logged_in}")
            break

        else:
            print("Invalid choice. Please select 1,2,3 or 4")