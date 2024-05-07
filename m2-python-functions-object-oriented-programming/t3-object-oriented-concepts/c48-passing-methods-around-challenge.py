# Passing Methods Around Challenge

class Employee:
    """Creates an instance of Employee"""

    def __init__(self, name, annual_salary):
        self.name = name
        self.annual_salary = annual_salary

    def calculate_monthly_salary(self):
        return self.annual_salary / 12


class CustomerServiceEmployee(Employee):
    """Creates an instance of CustomerServiceEmployee"""

    def __init__(self, name, annual_salary, department):
        super().__init__(name, annual_salary)
        self.department = department

cs_manager = CustomerServiceEmployee("Kelly Johnson", 42000, "Customer Service")

kellys_monthly_salary = cs_manager.calculate_monthly_salary()

print(kellys_monthly_salary)