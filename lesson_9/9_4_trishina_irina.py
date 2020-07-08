# Задание 4
# Напишите функцию, которая возвращает минимальное
# из пяти чисел. Числа передаются в качестве параметров.

def min_in_5_numbers(n1, n2, n3, n4, n5):
    min=n1
    if n2<min:
        min=n2
    elif n3<min:
        min=n3
    elif n4<min:
        min=n4
    elif n5<min:
        min=n5
    return min

print(int(min_in_5_numbers(2,7,6,-1,3)))
