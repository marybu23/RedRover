# ALEXANDR
# #1 Четное или нечетное?
#
# n = int(input("введите число: "))
#
# if n % 2 == 0:
#     print("четное")
# else:
#     print("нечетное")

# #2 Какой сегодня день?
#
# day = input("Какой сегодня день? ").lower()
#
# if day == "суббота" or day == "воскресенье" :
#     print("Сегодня выходной!")
# elif day == "среда".lower():
#         print("Мне сегодня к стоматологу в 15:30")
# else:
#     print("Сегодня обычный день")

# #3 Эхо
#
# n = int(input("Введите число: "))
# text = input("Введите текст: ")
#
# for i in range(n):
#     print(text)

#4 Сколько гласных букв?
#
# count = 0
# message = input("Введите сообщение: ")
# for i in message.lower():
#     if i in "ауеёоэыияю":
#         count += 1
# print(count)

# #5 Сумма чисел
# total = 0
#
# while True:
#     a = int(input("Введите число: "))
#     if a < 0:
#         break
#     total += a
# print(total)
#



#REVIEW OLGA


#1
#
# x = 8
# y = 25
# z = 100
#
# print (0 < x <= 40 and y >= 10) # True
# print(x + y > z or y + z > x) # True
# print(x != 50 and z % y != 0) # False
# print(x >= y or y < 200) # True
# print(not (z < 356)) # False
# print(x == 18 or y // x == 3) # True

#3
# number = int(input("Введите число: "))
# a = number // 10
# b = number % 10
# if a == b:
#     print("ДА")
# else:
#     print("НЕТ")

#4
# pass_1 = input("Введите пароль: ")
# pass_2 = input("Подтвердите пароль: ")
#
# if pass_1 == pass_2 and len(pass_1) >= 8:
#     print("Пароль принят")
# elif len(pass_1) < 8:
#     print("Пароль слишком короткий")
# else:
#     print("Пароль не принят")

#5
#
# n = int(input("Введите число: "))
# if 0 <= n < 1000:
#    if 0 <= n <= 9:
#     print("Число однозначное")
#    elif 10 <= n <= 99:
#     print("Число двузначное")
#    elif 100 <= n <= 999:
#     print("Число трехзначное")
# else:
#     print("Введите число от 0 до 999")

#6
# name = input("Введите имя: ").capitalize()
# hobby = input("Введите Ваше увлечение: ").lower()
#
# if hobby == "музыка":
#     print(f"{name}, пойдем на концерт?")
# elif hobby == "спорт":
#     print(f"{name}, пойдем в поход?")
# elif hobby == "театр":
#     print(f"{name}, пойдем в театр?")
#
# else:
#     print(f"{name}, пойдем в ресторан?")

#7
# year = int(input("Введите год: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Високосный")
# else:
#     print("Невисокосный")


#REVIEW KRISTINA

#1
# word = input("Введите слово:").lower()
# vowels = "ауоыиэяюёе"
# consonants = "бвгджзйклмнпрстфхцчшщ"
# vow_count = 0
# cons_count = 0
# for letters in word:
#     if letters in vowels:
#         vow_count += 1
#     elif letters in consonants:
#         cons_count += 1
# print(f"Гласных букв: {vow_count}, согласных букв: {cons_count}")

#2
#
# time = int(input("Введите час: "))
#
# if time >= 0  and time < 6:
#     print("Доброе утро")
# elif time >= 6 and time < 12:
#     print("Добрый день")
# elif time >= 12 and time < 18:
#     print("Добрый вечер")
# elif time >= 18 and time < 24:
#     print("Доброй ночи")
# else:
#     print("Введите корректное значение (0-23)")

#3 Программа должна вывести сумму всех чисел до этого числа включительно

#способ 1
#num = int(input("Enter the number: "))
#
# count = 0
# for i in range(1, num + 1):
#      count += i
# print(count)
#
#способ 2
# num = int(input("Enter the number: "))
# count = 0
# while num != 0:
#     count += num
#     num -= 1
# print(count)

#4 Напишите программу, которая в последовательности натуральных чисел
# определяет максимальное число, кратное 5.
#
#
# n = int(input("Enter a count: "))
# max_num = 0
# for i in range(n):
#     num = int(input("Enter a number: "))
#     if num % 5 == 0 and num > max_num:
#         max_num = num
# print(f"Максимальное число: {max_num}")

#HOME WORK
#1
# apple_count = int(input("Введите количество яблок: "))
# banana_count = int(input("Введите количество бананов: "))
# sum = apple_count + banana_count
# if apple_count + banana_count > 10:
#     print(f"Many fruits {sum}")
# else:
#     print(f"Few fruits {sum}")

#or
# apple_count = int(input("Введите количество яблок: "))
# banana_count = int(input("Введите количество бананов: "))
# if (apple_count + banana_count) > 10:
#     print(f"Many fruits")
# else:
#     print(f"Few fruits")

#2
#
# book_title = input("Введите название книги: ")
# pages = int(input("Введите колличество страниц: "))
# if pages > 300:
#     print(f"{book_title} is a long book")
# elif 100 <= pages <= 300:
#     print(f"{book_title} is a medium book")
# else:
#     print(f"{book_title} is a short book")

#3
# shirt_count = int(input("Enter a shirt count: "))
# price_per_shirt = int(input("Enter a price per shirt: "))
# pants_count = int(input("Enter a pants count: "))
# price_per_pants = int(input("Enter a price per pants: "))
#
# total_price = shirt_count * price_per_shirt + pants_count * price_per_pants
# if total_price > 100:
#     print("Big shopping")
# else:
#     print("Small shopping")

#4 КАЛЬКУЛЯТОР
# numbers = input("Введите числа: ")
# actions = "+-/*"
# action = ""
# num1 = ""
# num2 = ""
# for i in numbers: # Перебираем все элементы введенной строки
#     if i not in actions: # Проверяем не введен ли символ из actions
#         if not action: # Проверяем первое число или второе
#             num1 += i
#         else:
#             num2 += i
#     else:
#         action = i
# if action not in actions: print("Неизвестная операция")
# elif not num1 or not num2: print("Ошибка ввода")
# else:
#     num1 = int(num1)
#     num2 = int(num2)
#     if action == "+": print(f"Результат: {num1 + num2}")
#     elif action == "-": print(f"Результат: {num1 - num2}")
#     elif action == "*": print(f"Результат: {num1 * num2}")
#     elif action == "/": print(f"Результат: {num1 / num2}")

#EXTRA TASK
#
#1
# username = input("Enetr username: ")
# password = input("Enter password: ")
# if username == "admin" or password == "1234":
#     print("Access granted")
# else:
#     print("Access denied")

#2
# n = int(input("Enter a number: "))
# step = int(input("Enter a step: "))
# for i in range(1, n, step):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     else:
#         print(i)

#3 Создайте переменные friend1_score, friend2_score, friend3_score
# значения которых определяются через ввод данных с клавиатуры.
# Выведите имя друга с наибольшим результатом.

#4
# friend1 = input("Введите имя 1 друга: ")
# friend1_score = int(input("Введите счет 1 друга: "))
# friend2 = input("Введите имя 2 друга: ")
# friend2_score = int(input("Введите счет 2 друга: "))
# friend3 = input("Введите имя 3 друга: ")
# friend3_score = int(input("Введите счет 3 друга: "))
#
# if friend1_score > friend2_score and friend1_score > friend3_score:
#     print(f"Победу одержал {friend1}")
# elif friend2_score > friend1_score and friend2_score > friend3_score:
#     print(f"Победу одержал {friend2}")
# elif friend3_score > friend1_score and friend3_score > friend2_score:
#     print(f"Победу одержал {friend3}")
# else:
#     print("Победила дружба")