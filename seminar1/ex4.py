# задача 4
# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

print("\nРешение задачи №4: \n")
n = int(input('Введите номер четверти: '))
if n < 1 or n > 4:
    print('Пожалуйста, повторите ввод (неверный номер четверти)')
elif n == 1:
    print('x > 0 и y > 0')
elif n == 2:
    print('x < 0 и y > 0')
elif n == 3:
    print('x < 0 и y < 0')
elif n == 4:
    print('x > 0 и y < 0')
else:
    print('На координатной плоскости 4 четверти')