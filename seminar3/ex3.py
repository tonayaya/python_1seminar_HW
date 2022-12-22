# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = int(input('Сколько вещественных чисел вы будете задаваь? '))
if n < 2:
    print('Надо ввести минимум 2 числа!')
    exit()
in_list = list([0] * n)
for _ in range(n):
    in_list[_] = float(input('Введите число: '))
print(in_list)
maxx = in_list[0] % 1
mini_maxx = in_list[1] % 1
for i in range(n):
    if in_list[i] % 1 !=0 and in_list[i] % 1 >= maxx:
        maxx = in_list[i] % 1
    if in_list[i] % 1 !=0 and in_list[i] % 1 <= mini_maxx:
        mini_maxx = in_list[i] % 1 
print(round((maxx - mini_maxx), 2))