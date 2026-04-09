class Employee:

    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        print("Base salary:", self.base_salary)


class Developer(Employee):

    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        total = self.base_salary + self.bonus
        print(self.name, "Developer Salary:", total)


class Manager(Employee):

    def __init__(self, name, base_salary, allowance):
        super().__init__(name, base_salary)
        self.allowance = allowance

    def calculate_salary(self):
        total = self.base_salary + self.allowance
        print(self.name, "Manager Salary:", total)


# Workflow function (Polymorphism)
def process_salary(employee):
    employee.calculate_salary()


# Objects
dev1 = Developer("Rahul", 50000, 10000)
mgr1 = Manager("Anita", 70000, 20000)

employees = [dev1, mgr1]

for emp in employees:
    process_salary(emp)