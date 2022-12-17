# Задача 5
# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

import os
os.system("cls")

first_point = list(map(int, input(
    "Введите координаты первой точки x y через пробел: ").split()))
second_point = list(map(int, input(
    "\nВведите координаты второй точки x y через пробел: ").split()))
distance = (((second_point[0] - first_point[0])**2 +
            (second_point[1] - first_point[1])**2) ** (0.5))
print(
    f"\nРасстояние между двумя точками пространства = {round(distance, 3)}\n")