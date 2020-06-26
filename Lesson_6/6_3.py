# Задание 3
# Пользователь вводит с клавиатуры два числа (начало
# и конец диапазона). Требуется проанализировать все числа
# в этом диапазоне. Вывод на экран должен проходить по
# правилам, указанным ниже.
# Если число кратно 3 (делится на 3 без остатка) нужно
# вывести слово Fizz. Если число кратно 5 нужно выве-
# сти слово Buzz. Если число кратно 3 и 5 нужно вывести
# Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести
# само число.

start=int(input("Enter the first number:"))
finish=int(input("Enter the second number:"))

for i in range (start,finish):
    if i%3==0:
        print ("Fizz")
print ("*****************")
for i in range(start, finish):
    if i%5==0:
        print ("Buzz")
print ("*****************")
for i in range(start, finish):
    if (i%3==0 & i%5==0):
        print ("Fizz Buzz")
print ("*****************")
for i in range(start, finish):
    if (i%3!=0 & i%5==0):
        print (i)