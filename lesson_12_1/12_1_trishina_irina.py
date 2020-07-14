#1. Написати функцію-декоратор, яка підносить до квадрату значення, що повертає функція,
# до якої декоратор застосовується.
def square_value (func):
    def wrapper (num):
        return num**2
    return wrapper

@square_value
def cub_value(num):
    return num**3

print(cub_value(2))
print(cub_value(3))
print(cub_value(4))