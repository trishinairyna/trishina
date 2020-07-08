# Задание 6
# Напишите функцию, которая считает количество
# цифр в числе. Число передаётся в качестве параметра. Из
# функции нужно вернуть полученное количество цифр.
# Например, если передали 3456, количество цифр будет 4.

def number_of_digits (num:int):
    count=0
    while num>0:
        num//=10
        count=count+1
    return count

number=int(input("Enter the number: "))
print(number_of_digits(number))