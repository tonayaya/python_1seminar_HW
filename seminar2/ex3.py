# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. 
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4 [-4, -3, -2, -1, 0, 1, 2, 3,4]

from random import randint
F = 5 # const
n = int(input('n = '))
newList = []

for i in range(-n, n+1):
    newList.append(i)
print(newList)
nList = []
composition = 1

for i in range(F + 1):
    nList.append(randint(0, len(newList)))
composition *= nList[i]
print(f'произведение элементов на индексах: {nList} равно {composition}')
