# Milk Collection System
farmer_name = input("Enter Your Name: ")
morning_milk = float(input("Enter Morning Milk Amount: "))
eve_milk = float(input("Enter Evening Milk Amount: "))
price_per_l = float(input("Enter Price Per Litre: "))

deliveries = [morning_milk, eve_milk]

total_litres = deliveries[0] + deliveries[1]
formated_total = f"{total_litres:.2f}"

amount_pay = total_litres * price_per_l
formated_pay = f"{amount_pay:.2f}"

morning_milk = str(morning_milk)
eve_milk = str(eve_milk)
price_per_l = str(price_per_l)
formated_total = str(formated_total)
formated_pay = str(formated_pay)

farmer = {
    "Farmer ame: " : farmer_name,
    "Morning Milk Amount: " : morning_milk,
    "Evening Milk Amount: " : eve_milk,
    "Price Per Litre: " : price_per_l,
    "Total Milk: " : formated_total,
    "Total Amount Payable: " : formated_pay,
}

print(farmer)
