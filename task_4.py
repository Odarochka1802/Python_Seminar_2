# Задайте список из N элементов, заполненных числами из 
# промежутка [-N, N]. Найдите произведение элементов на указанных 
# позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n=abs(int(input("Введите число: ")))
l=[i for i in range(-n,n+1)]
print(f"Наш список {l}")
pr=1
with open(r"C:\Users\odark\OneDrive\Desktop\python\seminar_1\seminar_2\file.txt","r",encoding="utf-8") as file:
    for line in file:

        if (a:=int(line.strip())) <len(l):
            print(f"На позиции l[{a}] находится цифра {l[a]}")
            pr*=l[a]
        else:
            print(f"Позиция {a} за пределами списка!")
print(f"Произведение всех чисел на выбраных позициях = {pr}")


# Вот позиции с файла
# 4
# 3
# 7
# 2