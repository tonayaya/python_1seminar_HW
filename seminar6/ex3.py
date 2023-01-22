# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def amount(number):
    s = sum(map(int, number.replace('.', '').replace('-', '')))
    return s


number = input('Введите число: ')
print(f'Сумма цифр: {amount(number)}')
