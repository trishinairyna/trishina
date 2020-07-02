# Задание 1
# Два списка целых заполняются случайными числами.
# Необходимо:
# 1-1Сформировать третий список, содержащий элементы
# обоих списков;
# 1-2 Сформировать третий список, содержащий элементы
# обоих списков без повторений;
# 1-3 Сформировать третий список, содержащий элементы
# общие для двух списков;
# 1-4 Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
# 1-5 Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из
# списков.


list_1=[2,3,4,5,6,-5,7,8,9]
list_2=[1,5,8,11,0,15]


#1-1
list_3=[]
for i in list_1:
    list_3.append(i)
for i in list_2:
    list_3.append(i)
print(list_3)

#1-2
list_3=[]
for i in list_1:
    if i not in list_3:
        list_3.append(i)
for i in list_2:
    if i not in list_3:
        list_3.append(i)
print(list_3)

#1-3
list_3=[]
for i in list_1:
    if i in list_2:
        list_3.append(i)
print(list_3)

#1-4
list_3=[]
for i in list_1:
    if i not in list_2:
        list_3.append(i)
for i in list_2:
    if i not in list_1:
        list_3.append(i)
print(list_3)

#1-5
list_3=[]
min_1=list_1[0]
max_1=list_1[0]
for i in list_1:
    if min_1<i:
        min_1=i
    if max_1 > i:
        max_1 = i
list_3.append(min_1)
list_3.append(max_1)
min_2=list_2[0]
max_2=list_2[0]
for i in list_2:
    if min_2<i:
        min_2=i
    if max_2 > i:
        max_2 = i
list_3.append(min_2)
list_3.append(max_2)
print(list_3)
