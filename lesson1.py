# Задание 1.1
# a = 310
# b = 7
# c = a % b
# print("Остаток от деления 310 на 7 равен:", c)

# Задание 1.2
# name = input("Введите ФИО: ")
# fac = input("Введите название своего факультет: ")
# course = input("Введите номер курса: ")
# age = input("Введите возраст: ")
# print(f"{name} {fac} {course} курс {age}")

# Задание 2
# time = int(input("Введите время в секундах: "))
# h = time // 3600
# m = (time - h * 3600) // 60
# s = time % 60
# if h <= 9:
#     h = str(0) + str(h)
# if m <= 9:
#     m = str(0) + str(m)
# if s <= 9:
#     s = str(0) + str(s)
# print(f"Время в формате чч:мм:сс {h}:{m}:{s}")

# Задание 3
# n = int(input("Введите число n: "))
# sum = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
# print("Сумма чисел n+nn+nnn =", sum)

# Задание 4
# num = abs(int(input("Введите целое положительное число: ")))
# max = num % 10
# while num > 0:
#     num = num // 10
#     if num % 10 > max:
#         max = num % 10
#         if num > 9:
#             continue
#         else:
#             print("Самая большая цифра в числе: ", max)
#         break

# Задание 5
# pr = float(input("Введите прибыль компании: "))
# cos = float(input("Введите издержки компании: "))
# if pr < cos:
#     print("Компания работает в убыток")
# elif pr == cos:
#     print("Компания работает в ноль")
# else:
#     rent = round(pr / cos, 2)
#     print(f"Компания работает с прибылью. Рентабельность равна {rent}")
#     empl = int(input("Введите количество сотрудников, работающих в фирме: "))
#     x = round(pr / empl, 2)
#     print("Прибыль фирмы в расчёте на одного сотрудника равна: ", x)

# Задание 6
# a = int(input("Введите результат первого дня (км): "))
# b = int(input("Введите цель (км): "))
# d = 1
# while a < b:
#     a = a * 1.1
#     d += 1
# print(f"Цель по бегу будет достигнута на {d} день")
