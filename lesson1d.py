# lists -  a collection of related items.
# Uses square brackets
# To access items indexing is used starting from index 0 [0]

farmers = ["John", "Mary", "Peter", "Jane", "Samuel"]
print(farmers)
print(type(farmers))
print(farmers[0])
print(farmers[2])

print("==============================================")

# Negative indexing(picking from last)
print(farmers[-1])
print(farmers[-2])

print("==============================================")

# slicing - end index is not included
print(farmers[1:4])
print(farmers[2:])
print(farmers[:4])

print("==============================================")

# Chrcking length
print(len(farmers))

print("==============================================")

# Checking existing items
print("John" in farmers)
print("Ann" in farmers)

print("==============================================")

# methods
#adds at the end
farmers.append("David")
print(farmers)

#adds at any index
farmers.insert(1, "Grace")  
print(farmers)

# Removes first instance of a value
farmers.remove("Mary")
print(farmers)

# Removes values at and index. Automatically removes the last one if not specified
farmers.pop(0)
print(farmers)

# Sort - ascending
farmers.sort()
print(farmers)

# Reverse order - descending
farmers.reverse()
print(farmers)