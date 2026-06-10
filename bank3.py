class Account:
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance

    def Deposit(self):
        print("===========================")
        print("Deposit")   
        print("===========================")

        amount = float(input("Enter the amount You would wish to deposit: Ksh "))
        
        if amount > 0:
            self.balance += amount
            print(f"Ksh {amount} has been successfully deposited to your account. Current balance Ksh: {self.balance}")
        else:
            print ("Invalid amount")
            
    def Withdraw(self):
        print("===========================")
        print("Withdraw")
        print("===========================")

        amount = float(input("Enter the amount you would wish to withdraw: Ksh "))

        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Ksh {amount} has successfully been withdrawn from your account. Current Balance Ksh:{self.balance}")

    def Check_balance(self):
        print("===========================")
        print("Check balance")
        print("===========================")

        print(f"Current balance: Ksh {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = [
            Account("John", "jon123", 5000),
            Account("Mary", "mary123", 1200),
            Account("Peter", "peter123", 0)
        ]

        self.logged_in = None

    def Find_account(self, username):
        for account in self.accounts:
            if account.username == username:
                return account
    
    def Create_account(self):
        print("===========================")
        print("Create an Account")
        print("===========================")

        user_name = input("Choose a username: ")

        user_exist = False
        for account in self.accounts:
            if account.username == user_name:
                user_exist = True

        if user_exist:
            print("Username already exists. Try a different username")
        else:
            password = input("Choose a password:")
            new_account = Account(user_name, password, 0)
            self.accounts.append(new_account)
            print(f"Your account has been created. Welcome {user_name}!")
            self.logged_in = user_name
        
    def Login(self):
        print("===========================")
        print("Login")
        print("===========================")

        trial = 3

        while trial > 0:
            user_name = input("Enter your Username: ")
            password = input("Enter your password: ")

            for account in self.accounts:
                if account.username == user_name and account.password == password:
                    self.logged_in = user_name
                    break

            if self.logged_in:
                print(f"Welcome Back, {self.logged_in}")
                break
            else:
                trial -=1
                if trial > 0:
                    print(f"Wrong credentials. You have {trial} trials remaining")
                else:
                    print("Too many Failed attempts. You have been logged out")

bank = Bank()

while True:
    if bank.logged_in is None:
        print("===========================")
        print("SOKO BANK")
        print("===========================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        print("===========================")

        option = input("Enter Your Choice: ")

        if option == "1":
            bank.Create_account()

        elif option == "2":
            bank.Login()

        elif option == "3":
            print("Thank you for choosing Soko Bank. Good bye!")
            break

        else:
            print("Invalid choice. Please pick 1, 2 or 3")

    else:
        current_acc = bank.Find_account(bank.logged_in)

        print("==========================")
        print(f"SOKO BANK | {bank.logged_in}")
        print("==========================")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        print("==========================")

        choice = input("Enter your choice: ")

        if choice == "1":
            current_acc.Deposit()

        elif choice == "2":
            current_acc.Withdraw()

        elif choice == "3":
            current_acc.Check_balance()

        elif choice == "4":
            print(f"Thank you for choosing Soko Bank. Good bye, {bank.logged_in}!")
            break

        else:
            print("Invalid choice. Please pick 1, 2, 3 or 4")