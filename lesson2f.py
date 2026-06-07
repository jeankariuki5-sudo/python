# While-loop - executes a block of code a number of times based on a condition
# while (condition)
    # Block of code
    # increment

counter = 1
while counter <= 5:
    print(f"Hello {counter}")
    counter += 1


credentials = "John"
trial = 3
while trial >= 0:
    enter = input(".Welcome to Soko Farm.\n Enter Your Credentials: ")

    if enter == credentials:
        print(f"Welcome Back {credentials}")
        
        break
    
    else:
        trial = trial - 1
        if trial > 0:
            print(f"Wrong credentials! You have {trial} tries remaining")
        else:
            print("You have been logged out!")
            break

