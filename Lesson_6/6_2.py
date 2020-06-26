# Задание 2
# Пользователь вводит с клавиатуры два числа (нача-
# ло и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне. Нужно вывести на экран:
# 1. Все числа диапазона;
# 2. Все числа диапазона в убывающем порядке;
# 3. Все числа, кратные 7;
# 4. Количество чисел, кратных 5.

start=int(input("Enter the first number:"))
finish=int(input("Enter the second number:"))

for i in range (start,finish):
    print (i)
print("*****************")

for i in reversed (range (start,finish)):
    print (i)
print("*****************")

for i in range(start,finish):
    if i%7==0:
        print (i)
print("*****************")

count=0
for i in range (start,finish):
    if i%5==0:
        count+=1
print (count)