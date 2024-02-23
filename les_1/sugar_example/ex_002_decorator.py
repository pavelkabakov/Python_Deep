# Без синтаксического сахара:

def my_decorator(func):
    def wrapper():
        print("Что-то происходит перед вызовом функции.")
        func()
        print("Что-то происходит после вызова функции.")
    return wrapper

def say_hello():
    print("Привет, мир!")

say_hello = my_decorator(say_hello)

# С синтаксическим сахаром:

@my_decorator
def say_hello():
    print("Привет, мир!")

