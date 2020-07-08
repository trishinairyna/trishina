# Задание 2
# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все четные числа
# между ними.

def even_numbers(n_1:int, n_2:int):
    for i in range (n_1+1,n_2):
        if i%2==0:
            print (i)
n_1=int(input("Enter the first number:"))
n_2=int(input("Enter the second number:"))
even_numbers(n_1,n_2)
