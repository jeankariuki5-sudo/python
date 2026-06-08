# Functions without parameters(input from the terminal)
# def sum2 ():
#     a = int(input("Enter num1: "))
#     b = int(input("Enter num2: "))
#     sum = a + b
#     print(f"The sum of {a} and {b} is: {sum}")

# sum2()

print("===========================================")

# Functions with parameters
def sum (a,b):
    sum = a + b
    print(f"The sum of {a} and {b} is: {sum}")
    return sum

print(sum(9, 76))


# Funtions with Return
def sum3 (c, d):
    ans = c + d
    return ans

print(sum3(60, 30))
result = sum3(60, 30)
print(result)

