# Модуль 3. Циклы.
# Часть 1
# Задание 1
# Пользователь вводит с клавиатуры два числа (нача-
# ло и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне по следующему правилу: если
# число кратно 7, его надо выводить на экран.

start=int(input("Enter the first number:"))
finish=int(input("Enter the second number:"))

for i in range(start,finish):
    if i%7==0:
        print (i)