# Пользователь вводит число,
# Вам необходимо вывести число Пи с той точностью знаков после запятой,
# сколько указал пользователь(БЕЗ round())

n = int(input("Введите точность знаков после запятой числа ПИ: "))
k = 1
s = 0
for i in range (100000):
    if i % 2 == 0 :
        s += 4 / k
        k += 2
    else :
        s -= 4 / k
        k += 2
print(f"%.{n}f" % s)