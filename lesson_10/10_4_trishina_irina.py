# Задание 4
# Напишите функцию, удаляющую из списка целых
# некоторое заданное число. Из функции нужно вернуть
# количество удаленных элементов.

list=[2,3,10,13,16,5,8,18,24,53,6,5,19,5,19,24,8,53,5,5,6]

def del_number (num:int):
    new_list=[]
    count=0
    i=0
    while i<len(list):
        if list[i]==num:
            new_list.append(list[i])
            del list[i]
            count+=1
        else:
            i+=1
    return count

print(del_number(5))
print(del_number(2))
print(del_number(24))
