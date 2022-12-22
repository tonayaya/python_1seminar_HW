# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

in_list = list(input('Задайте список из нескольких чисел без разделителей: '))
print(in_list)
n = len(in_list)
summ_chet = 0
for i in range(0, n, 2):
    summ_chet += int(in_list[i])
summ_nechet = 0
for i in range(1, n, 2):
    summ_nechet += int(in_list[i])
print('Сумма чётных элементов: ', (summ_chet))
print('Сумма НЕчётных элементов: ', + (summ_nechet))