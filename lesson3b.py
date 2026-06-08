def totcollection():
    totcol = morning + evening
    return totcol

def collect(morning, evening):
    totcol = totcollection(morning, evening)
    collection = {
        "Name" : name,
        "Location" : location,
        "TotalMilk": totcol
    }
    print(collection)

name = input("Your Name: ")
location = input("Your Location: ")
morning = int(input("Your Morning Collecton: "))
evening = int(input("Your evening Milk: "))