# Constructor with params
class farmer:
    def __init__(self, name, litres, price):
        self.name = name
        self.litres = litres
        self.price = price

    def calculate_payment(self):
        payment = self.litres * self.price
        return payment
    
    def display_info(self):
        print(f"Farmer name: {self.name}")
        print(f"Collected litres: {self.litres}")
        print(f"Price Per Litre: {self.price}")
        print(f"Payment Ksh: {self.calculate_payment()}")

farmer1 = farmer("John", 50, 45)
farmer1.display_info()