# strings -  sequence of characters enclosed in ""/ ''
message = 'Welcome to Django'
print(message)

print("==============================================")

# length
print(len(message))

print("==============================================")

# Convert to uppercase
print(message.upper())

print("==============================================")

# Convert to lowercase
print(message.lower())

print("==============================================")

# Capitalize
print(message.title())

print("==============================================")

# replace text
print(message.replace("Django", "Python"))

print("==============================================")

# Accessing characters using indexes
print(message[0])

print("==============================================")

# slicing
print(message[:7])

print("==============================================")

# concatenation
greetings = "Good"
time = "Morning"
print(greetings + " " + time)
