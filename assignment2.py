print("==========================")
print("SOKO BANK")
print("==========================")


credentials = "John"
trial = 3
balance = 0

# Login
while trial >= 0:

    enter = input(".Welcome to Soko Bank.\n Enter Your Credentials: ")

    if enter == credentials:
        print("==========================")
        print("SOKO BANK")
        print("==========================")
        print(f"Welcome Back {credentials}")
        break
    
    else:
        trial = trial - 1
        if trial > 0:
            print("==========================")
            print("SOKO BANK")
            print("==========================")
            print(f"Wrong credentials! You have {trial} tries remaining")
        else:
            print("==========================")
            print("SOKO BANK")
            print("==========================")
            print("You have been logged out!")
            break

# Bank menu
if trial > 0:
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        print("==========================")

        choice = input("Enter your choice: ")

        # Deposit
        if choice == "1":
            print("==========================")
            print("Deposit")
            print("==========================")
            amount = float(input("Enter the amount you would wish to Deposit: Ksh "))
            if amount > 0:
                balance += amount
                print(f"You have successfilly deposited Ksh {amount} into your account. Current balance is Ksh {balance}")
            else:
                print("Invalid amount")
            
        # Withdraw
        elif choice == "2":
            print("==========================")
            print("Withdraw")
            print("==========================")
            amount = float(input("Enter the amount you would wish to Withdraw: Ksh "))
            if amount <= 0:
                print("Invalid amount")
            elif amount > balance:
                print(f"You have insufficient funds. Current balance is: {balance}")
            else:
                balance -= amount
                print(f"Withdrawal of Ksh: {amount} successful. Current balance is Ksh: {balance}")

        # Balance
        elif choice == "3":
            print("==========================")
            print("Balance")
            print("==========================")
            print(f"Current balance is Ksh: {balance}")

        # Exit
        elif choice == "4":
            print(f"Thank you for banking with Soko Farm. Goodbye, {credentials}!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")
            