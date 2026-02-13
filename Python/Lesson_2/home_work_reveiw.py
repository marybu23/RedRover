# #class work
# a = int(input())
# b = int(input())
# c = int(input())
# print((a+b+c)/3)
from itertools import count

# celsius = int(input("Введите температуру в С°: "))
# f = float((9/5 * celsius) + 32)
# print(f"{f} F")

# a = int(input())
# print(a ** 2)

# a = int(input("Введите целое число: "))
# b = float(input("Введите дробное число: "))
#
# c = a + b
# d = a - b
# e = a * b
# f = a // b
# g = a % b
#
# print(f" sum: {c}\n diff: {d}\n mul: {e}\n int_div: {f}\n float_div: {g}")

#HOME WORK

# dollars = int(input("How many dollars do you have?: "))
# rate = float(input("Enter the rate: "))
# print(f"При {dollars} долларах по курсу {rate} получится {dollars * rate} рублей")


# #1 вариант (сложный пробный)
# apples = int(input("Сколько килограмм яблок вы хотите купить? "))
# pears = int(input("Сколько килограмм груш вы хотите купить? "))
# bananas = int(input("Сколько килограмм бананов вы хотите купить? "))
# apples_price = 100
# pears_price = 150
# bananas_price = 70
# sale = 0.2 #20%
#
# print (f"Яблоки: цена без скидки {apples * apples_price} руб., скидка {(apples * apples_price)  * sale} руб., итоговая цена  {(apples * apples_price) - ((apples * apples_price) * sale)} руб.\n"
#        f"Груши: цена без скидки {pears * pears_price} руб., скидка {(pears * pears_price) * sale} руб., итоговая цена {(pears * pears_price) - ((pears * pears_price) * sale)} руб.\n"
#        f"Бананы: цена без скидки {bananas * bananas_price} руб., скидка {(bananas * bananas_price) * sale} руб., итоговая цена {(bananas * bananas_price) - ((bananas * bananas_price) * sale)} руб.\n"
#        f"Общая сумма после скидок: {((apples * apples_price) - ((apples * apples_price)  * sale)) + ((pears * pears_price) - ((pears * apples_price) * sale)+((bananas * bananas_price) - ((bananas * bananas_price) * sale)))}")

#2 вариант (проще)

# apples = int(input("Сколько килограмм яблок вы хотите купить? "))
# pears = int(input("Сколько килограмм груш вы хотите купить? "))
# bananas = int(input("Сколько килограмм бананов вы хотите купить? "))
# apples_price = 100
# pears_price = 150
# bananas_price = 70
# sale = 0.2 #20%
#
# #Яблоки
# apples_count = apples * apples_price
# apples_sale = apples_count * sale
# apples_total = apples_count - apples_sale
#
# #Груши
# pears_count = pears * pears_price
# pears_sale = pears_count * sale
# pears_total = pears_count - pears_sale

# #Бананы
# bananas_count = bananas * bananas_price
# bananas_sale = bananas_count * sale
# bananas_total = bananas_count - bananas_sale
#
# print(f"Яблоки: цена без скидки {apples_count} руб., скидка {apples_sale} руб., итоговая цена {apples_total}\n"
#       f"Груши: цена без скидки {pears_count} руб., скидка {pears_sale} руб., итоговая цена {pears_total}\n"
#       f"Бананы: цена без скидки {bananas_count} руб., скидка {bananas_sale} руб., итоговая цена {bananas_total}\n"
#       f"Общая сумма после скидок: {apples_total + pears_total + bananas_total}")


# name = input("Enter your name: ").capitalize()
# age = int(input("Enter your age: "))
#
# print(f"Привет, {name}! Через год тебе будет {age + 1}.")

# food = input("Какую еду вы выбрали? ")
# price = int(input("Цена? "))
# count = int(input("Cколько? "))
#
# print(f"Вы заказали {food} в количесвте {count}. \nИтоговая стоимость: {price * count}.")


#REVIEW другое H/W
# print("Я програмирую Python каждый день! \n" * 10)

# a = input("Введите имя любимого человека: ").capitalize()
# c = int(input("Ведите количество повторений: "))
# for i in range(c):
#     print (a)

#14 * 3 + 2 : 20 - 17 * 16 + (126,9 + 103)

# print(14 * 3 + 2 / 20 - 17 * 16 + (126.9 + 103))

# salary = int(input("Введите ваш оклад: "))
# salary_fail = salary - (salary * 0.2)
#
# salary_success = salary + (salary * 0.05)
# print(f"Ваш оклад составляет {salary} руб.\nПри успешном успехе вы получите {salary_success} руб.\nПри фейловых ситуациях ваша зарплата составит {salary_fail}.")

#Пирожок
# k = int(input("рублей "))
# m = int(input("копеек "))
# n = int(input("Сколько пирожков вы хотите купить? "))
# total = (k * 100 + m) * n
# rub = total // 100
# kop = total % 100
# print(f"Сумма к оплате: {rub} рублей {kop} копеек")