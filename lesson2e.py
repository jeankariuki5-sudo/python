# loop in a list

farmers = ["Mary", "John", "Peter", "Ian", "Jane"]

for farmer in farmers:
    print(farmer)

print("==================================")


collections = [20.5, 30.9, 24.6, 16.4, 13.5, 23.4, 12.0]

print("==================================")

for collection in collections:
        print(collection)

print("==================================")

sum = 0
count = 0
for collection in collections:
      sum += collection
      count += 1
      average = sum / count

print(f"Total: {sum}")
print(f"Average: {average:.2f}")