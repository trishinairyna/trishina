# Задание 5
# Напишите функцию, которая возвращает произве-
# дение чисел в указанном диапазоне. Границы диапазона
# передаются в качестве параметров. Если границы диапа-
# зона перепутаны (например, 5 — верхняя граница, 25 —
# нижняя граница), их нужно поменять местами.

def dob_start_end(start:int,end:int):

        if start>end:
            end,start=start,end
        rez = 1
        for i in range (start,end+1):
            rez*=i
        return rez

print(dob_start_end(3,8))
print(dob_start_end(10,3))
