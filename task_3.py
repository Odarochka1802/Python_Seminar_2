# Задайте словарь из n чисел последовательности (1 + (1/n))^n 
# и выведите на экран их сумму.

#     *Пример:*

#     - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
#     Необходимо сложить все значения словаря и вывести  сумму 
#     на экран.
def sequence_of_numbers(n,d={},summa=0):
    for i in range(1,n+1):
        d[i]=round((1 + (1/i))**i ,2)
    print(d)
    for i in d.values():
        summa+=i
    print(summa)
    
pos=sequence_of_numbers(n:=int(input("Введите число: ")))
#в примере словарь, а в задании сумма. Вывела и то, и другое)