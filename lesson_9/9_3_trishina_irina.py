# Задание 3
# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны ква-
# драта, символ и переменную логического типа:
# ■■ если она равна True, квадрат заполненный;
# ■■ если False, квадрат пустой.

def square_filling (a:int, symvol:str, b:bool):
    if b==1:
        for i in range(a):
            print(symvol*a)
    elif b==0:
        for i in range(a):
            if i==0 or i==a-1:
                print(symvol * a)
            else:
                print(symvol+(a-2)*" "+symvol)

print(square_filling(5,"+",1))
print(square_filling(5,"-",0))
