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
