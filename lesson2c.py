# if-elif-else - allows more then one condition
# The esle block gets excecuted only when all the conditions have failed

# if condition:
    # block of code
# elif condition 2:
    # block of code
# elif condition 3:
    # block of code
# else:
    # default block of code

litres = 65
if litres >= 100:
    print("premium farmer")
elif litres >= 50:
    print("regular farmer")
else:
    print("small scale farmer")

num = 0
if num == 0:
    print(f"{num} is zero")
elif num > 0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is a negative number")
