# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1

lst = []
lst_2 = []
num = int(input("Cколько цифр хотите внести в список: "))
for i in range(num):
    ind = int(input(f"Введите {i+1} число: "))
    lst.append(ind)
for j in lst:
    if lst.count(j) < 2:
        lst_2.append(j)
print(f"Список вводимых чисел: {lst}")
print(f"Список неповторяющихся элементов вводимых чисел: {lst_2}")