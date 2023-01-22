# Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension


data = [12,'sadf',5643]
nums = list(filter(lambda x: type(x) == int, data))
letters = list(filter(lambda x: type(x) == str, data))
print(f" Даны начальные данные: {data}")
print(f"Вывод отдельно букв и цифр: {letters}, {nums}")