# 1) Напишите программу,
# которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input(' Введите число:  \n'))
list =[]
for i in range(1,num+1):
    number_to_list = 1
    for j in range(1,i+1):
        number_to_list *= j
    list.append(number_to_list)
print(list)