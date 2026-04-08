class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance     # private variable

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance