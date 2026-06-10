# Create a program that calculates the salary of an employee. Name, Rate, Hour
# Also calculate bonuses
class employee:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def calc_pay(self):
        payment = self.hours * self.rate
        return payment
    
    def calc_bonus(self):
        if self.hours >= 100:
            bonus = self.calc_pay() * 5 / 100
            return  bonus
        else:
            return 0
        
    def total_pay(self):
        total_salary = self.calc_bonus() + self.calc_pay()
        return total_salary
        
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Hours: {self.hours}")
        print(f"Rate per hour: {self.rate}")
        print(f"Total Pay: {self.calc_pay()}")
        print(f"Bonus: {self.calc_bonus()}")
        print(f"Total Salary: {self.total_pay()}")

employee1 = employee("John", 20, 1000)
employee2 = employee("Mary", 110, 900)
employee1.display_info()
employee2.display_info()