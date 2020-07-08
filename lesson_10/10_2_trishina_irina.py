# Задание 2
# Напишите функцию для нахождения минимума в
# списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.

def min_of_list_items(list:int):
    min=list[0]
    for i in list:
        if min>i:
            min=i
    return min
list=[1,-54,2,32,-1,19,-14,5,6,-55,8]
print(min_of_list_items(list))