# Задание 5
# Напишите функцию, которая получает два списка в
# качестве параметра и возвращает список, содержащий
# элементы обоих списков.

def list_concatenation (list_1 : int, list_2 :int):
    list_3 = []
    for i in list_1:
        list_3.append(i)
    for i in list_2:
        list_3.append(i)
    print(list_3)

list_1=[0,12,8,55,6,34,18]
list_2=[14,85,10,5,18,54]
print(list_concatenation(list_1,list_2))