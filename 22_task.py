
    # Задача 22: Даны два неупорядоченных набора целых чисел 
    # (может быть, с повторениями). 
    # Выдать без повторений в порядке возрастания все те числа, 
    # которые встречаются в обоих наборах.
    # Пользователь вводит 2 числа. 
    # n - кол-во элементов первого множества. 
    # m - кол-во элементов второго множества. 
    # Затем пользователь вводит сами элементы множеств.

n = int(input('Введите кол-во элементов первого множества: '))
lst_n = [input(f'Введите {i} элемент: ') for i in range(1, n+1)]
print(lst_n)

m = int(input('Введите кол-во элементов второго множества: '))
lst_m = [input(f'Введите {i} элемент: ') for i in range(1, m+1)]
print(lst_m)

for i in sorted(lst_n):
    if i in lst_n and i in lst_m:
        print(i)
