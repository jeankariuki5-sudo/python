# dictionary - stores items/values as key value pairs
# We use curly-braces and access items using the key(using square brackets [])

student = {
    "name" : "John",
    "age": 13,
    "course" : "Software Engineering",
    "languages" : "Tailwind css"
}
print(student)
print(student["name"])
print(student["course"])
print(student["age"])
print(student["languages"])

# Add item
student["email"] = "john@gmail.com"
print(student)

# updating
student["age"] = 30
print(student)

# keys
student.keys()
print(student)