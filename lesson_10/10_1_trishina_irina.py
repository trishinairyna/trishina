# Задание 1
# Напишите функцию, вычисляющую произведение
# элементов списка целых. Список передаётся в качестве па-
# раметра. Полученный результат возвращается из функции.

def products_of_list_items(list:int):
    prod=1
    for i in list:
        prod*=i
    return prod
list=[1,2,3,5,6,8]
print(products_of_list_items(list))