from math_operations import MathOperations, calculate_power
from string_operations import StringOperations, count_words
from bank_system import BankAccount

def main():

    # Math Object
    math_obj = MathOperations(10,5)
    math_obj.display()

    print("Power:", calculate_power(2,3))


    print("------------------")

    # String Object
    str_obj = StringOperations("python project")
    str_obj.display()

    print("Word Count:", count_words("This is python module project"))


    print("------------------")

    # Bank Object
    account = BankAccount("Gowtham",1000)

    print("Deposit:", account.deposit(500))
    print("Withdraw:", account.withdraw(300))
    print("Balance:", account.get_balance())


if __name__ == "__main__":
    main()