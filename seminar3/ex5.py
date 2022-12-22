# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите целое число: '))
list_fibonachchi = [0] * (2 * k +1)
list_fibonachchi[k+1] = 1
list_fibonachchi[k+2] = 1
for i in range((k + 3), (k*2+1)):
    list_fibonachchi[i] = list_fibonachchi[i-1] + list_fibonachchi[i-2]
for i in range((k - 1), -1, -1):
    list_fibonachchi[i] = list_fibonachchi[i+2] - list_fibonachchi[i+1]
print(list_fibonachchi)