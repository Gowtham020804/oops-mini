
def logger(func):
    def wrapper():
        print("Function execution started")
        func()
        print("Function execution finished")
    return wrapper

@logger
def greet():
    print("Hello, welcome to Python!")

greet()