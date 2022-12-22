# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите деятичное число: '))
n_out = n # используем для красивой печати
binary = []
x = n
while x >= 1:
    x = n // 2
    binary.append(n - x * 2)
    n = x
else:
    print(f'{n_out} -> ', *binary, sep='')