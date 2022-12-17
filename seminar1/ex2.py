# Задача 2
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (0,0,0), (0,0,1) и тд.

print("\nРешение задачи №2: \n")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not (x or y or z) == (not x and not y and not z):
                print(f'Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно при X = {x}, Y = {y}, Z = {z}. ')