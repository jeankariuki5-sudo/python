# Functions with parameters
def sum (a,b):
    sum = a + b
    print(f"The sum of {a} and {b} is: {sum}")

sum(9, 76)

print("===========================================")

# Functions without parameters(input from the terminal)
def sum2 ():
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))
    sum = a + b
    print(f"The sum of {a} and {b} is: {sum}")

sum2()