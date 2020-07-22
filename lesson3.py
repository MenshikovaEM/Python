# # Task 1 Реализовать функцию, принимающую два числа и выполняющую их деление.
# def my_func():
#     try:
#         num1 = int(input("Введите первое число: "))
#         num2 = int(input("Введите второе число: "))
#         answ = num1 / num2
#     except ZeroDivisionError:
#         print("На ноль делить нелья")
#     return answ
#
# answ = my_func()
# print("Результат деления: ", round(answ, 2))

## Task 2 Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя. Именованные аргументы.
# def my_func(name, surname, year, city, email, telephone):
#     print(f"name - {name}; surname - { surname}; year - { year }; city - { city }; email - { email }; telephone- { telephone }")
#
# my_func(name = "Ekaterina", surname = "Menshikova", year = "1997", city = "Moscow", email = "123@mail.ru", telephone = "+79255915036")

# #Task 3 Реализовать функцию, которая принимает три позиционных аргумента, сумма наибольших двух.
# def my_func(num1, num2, num3):
#     if num1 <= num3 and num1 <= num2:
#         return num2 + num3
#
#     elif num2 <= num3 and num2 <= num1:
#         return num1 + num3
#     else:
#         return num1 + num2
#
# result = my_func(23, 10, 47)
# print("Сумма двух наибольших чисел: ", result)

## Task 4 Программа принимает действительное пол число x и целое отр число y. Возведение x в степень y.
# def my_func(x, y):
#     try:
# 	    result = x ** (y)
#     except ValueError:
#         print("Ошибка значений")
#     return result
#
# result = my_func(2, -5)
# print("Результат возведение x в степень y: ", round(result, 2))

# # Task 6 Реализовать функцию. Первую букву слова в заглавную
# def my_func(*args):
#     result = input("Введите слово: ")
#     print(result.title())
#     return
#
# my_func()
