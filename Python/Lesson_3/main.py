#BOOL TYPE "True", "False"
# a = True
# b = False
#
# print(a, b)

# a = 1 > 2 # False

# print(a)

# print(5 > 3) # True
# print(5 < 3) # False
# print(5 >= 3) # True
# print(5 <= 3) # False
# print(5 == 3) # False
# print(5 != 3) # True

# print("abc" == "abc") # True
# print("hello" == "HELLO") # False
# print("hello" != "HELLO") # True
#
# print("hello" != "abc") # True

# a = len("Hello") # 5
# print(a)


#СРАВНЕНИЕ ДЛИННЫ
# resoult = len("Hello") > 3 # True

# print(resoult)


#СРАВНЕНИЕ БЕЗ УЧЕТА РЕГИСТРА
# a = "hello" == "HELLO".lower() # True

# print(a)


#ВХОЖДЕНИЕ ПОДСТРОКИ В СТРОКУ
# print("abc" in "ABChelloabc") # True
#
# print("abc" in "ABChello") # False


#СОСТОИТ ЛИ СТРОКА ИЗ ЦИФР
# print("Hello".isdigit()) # False
# print("123".isdigit()) # True


#СОСТОИТ ЛИ СТРОКА И З СИМВЛОВ В НИЖНЕ РЕГИСТРЕ
# print("aCbcdr".islower()) # False



#ФУНКЦИЯ "if"
#
# age = 21
#
# if age >= 18:
#     print("....")
#     print("Доступ есть!")
#     print(".....")
#
# else:
#     print("....")
#     print("Доступ запрещен!")
#     print("....")
#
# print("Продолжение")

#ФУНКЦИЯ "elif"
# age = 15
#
# if age <= 12:
#     print("Ребенок")
# elif age <= 17:
#     print("Подросток")
# else:
#     print("Взрослый")
#
# print("Продолжение")

# улсловия "AND"
# age = 21
# is_citizen = True
#
# if age >=18 and is_citizen == True:
#     print("Вы можете голосовать")
# else:
#     print("Вы не можете голосовать")

# условия "OR"
# age = 74
# is_student = False
#
# if age >= 65 or is_student == True:
#     print("Вам положена скидка!")
# else:
#     print("Скидки не будет :(")

#УПРОЩЕНИЕ
# 1, 45, -2, -1, "abc", True, ... -> True
# False, 0, "", None, ... -> False

# a = 23
#
# if a:
#     print("a is true")

# age = 74
# is_student = False
#
# if age >= 65 or is_student:
#     print("Вам положена скидка!")
# else:
#     print("Скидки не будет :(")

# count = 0
#
# if count:
#     print(f"На вашем счету {count}")
# else:
#     print("У вас нет денег")


# ЦИКЛЫ (ПОВТОР написания) ИТЕРАЦИЯ
# Повтори это кусок кода 10 раз
# print("--------")
# print("Hello world")
# print("--------")
#
# for i in range(10):
#     print("--------")
#     print("Hello world")
#     print("--------")
#
# print("Продолжение")

# "123213"
# "Hello world"

# Возьми каждую БУКВУ из слово "ЯБЛОКО" и выполни с ней следующий код:
#   print(БУКВА)

# for letter in "ЯБЛОКО":
#     print(letter)

# (0, 1)
#
# for i in range(2):
#     print("-------")
#     print(i)
#     print("-------")
#
#
# for letter in "ЯБЛОКО":
#     print("-------")
#     print(letter)
#     print("-------")
#
# for letter in "ЯБЛОКО":
#     print(f"Текущая буква {letter}")
#     if letter == "О":
#         print("Нашел букву О!")

# numbers = range(10) # (0, 1, 2, ... 9)
#
# for i in numbers: # (0, 1, 2, ... 9)
#     print(i)
#
#
# numbers = range(10)
#
# for i in numbers:
#     if i == 5:
#         print("Я нашел пятерку!")
#
#     print(i)

#ЕСЛИ ПРОСТО ПОВТОРИТЬ НЕСКОЛЬКО РАЗ
# for i in range(10):
#      print("-------")
#      print("Hello world")
#      print("-------")
#
# counter = 0
#
# for letter in "ЯБЛОКО":
#     print(f"Текущая буква {letter}")
#     if letter == "О":
#         print("Нашел букву О!")
#         counter += 1
#
# print(counter)

#Чтобы цикл ПЕРЕСТАЛ ПРОВЕРЯТЬ (перебирать) каждый символ используем "break"

# password = "2132*de3434"
#
# for c in password:
#     print(c)
#
#     if c == "*":
#         print("Найден запрещенный символ!")
#         break
# print("Продолжение")

# Если нужно ИГНОРИРОВАТЬ какой-то символ "continue"
# message = "Hello, World!"
#
# for c in message:
#     if c == "!":
#         continue
#
#     print(c)

# ЦИКЛ "while"

# n = 10
#
# while n > 0:
#     print(n)
#
#     n -= 1

# n = 10
#
# while n > 0:
#     print(n)
#
#     if n == 5:
#         break
#
#     n -= 1
#
# while 1 == 1 (True)
#     print("Hello World") # бесконечно
#
# while True:
#     message = input("Enter a message: ")
#
#     if message == "exit":
#         break
#
#     print(message)