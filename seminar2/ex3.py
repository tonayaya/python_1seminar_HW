# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. 
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4 [-4, -3, -2, -1, 0, 1, 2, 3,4]

num = int(input('Введите целое число: \n'))
list = []
for i in range(-num, num+1):
    list.append(i)
import random
index_list  = []
while len(index_list)<5:
    index_list.append(random.randint(0,num * 2 + 1))
product = 1
for j in range(len(index_list)):
    product *= list[index_list[j]]
print(index_list)
print(list)
print(product)