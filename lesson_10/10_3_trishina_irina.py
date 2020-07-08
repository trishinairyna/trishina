# Задание 3
# Напишите функцию, определяющую количество про-
# стых чисел в списке целых. Список передаётся в качестве
# параметра. Полученный результат возвращается из функции.


def number_of_primes_in_list (list:int):
    simpl_list=[]
    count=0
    for i in list:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            simpl_list.append(i)
            count+=1
    return count
list=[2,8,14,54,6,9,7,5]
print(number_of_primes_in_list(list))