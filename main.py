# import math
#
# print(f"{'x':>8} {'sin(x)':>10}")
# print("-" * 20)
#
# for i in range(11):
#     x = i * math.pi / 10
#     y = math.sin(x)
#     print(f"{x:8.4f} {y:10.4f}")

# n = int(input("Введите N: "))
#
# sum_numbers = 0
# product = 1
# sum_squares = 0
#
# for i in range(1, n + 1):
#     sum_numbers += i
#     product *= i
#     sum_squares += i ** 2
#
# print(f"Сумма: {sum_numbers}")
# print(f"Произведение (N!): {product}")
# print(f"Сумма квадратов: {sum_squares}")


# n = int(input("Введите N: "))
#
# a, b = 0, 1
#
# print(f"Первые {n} чисел Фибоначчи:")
#
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
#
# print()

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)
# print(fib(10))

# n = int(input("Введите число: "))
# original = n
# factors = []
#
# divisor = 2
# while divisor * divisor <= n:
#     while n % divisor == 0:
#         factors.append(divisor)
#         n //= divisor
#     divisor += 1
#
# if n > 1:
#     factors.append(n)
#
# print(f"{original} = {' * '.join(map(str, factors))}")

# n = int(input("Введите число: "))
# original = n
#
# count = 0
# total = 0
# product = 1
# reversed_num = 0
#
# while n > 0:
#     digit = n % 10
#     count += 1
#     total += digit
#     product *= digit
#     reversed_num = reversed_num * 10 + digit
#     n //= 10
#
# print(f"Количество цифр: {count}")
# print(f"Сумма цифр: {total}")
# print(f"Произведение цифр: {product}")
# print(f"Перевёрнутое число: {reversed_num}")

# text = input("Введите строку: ")
# if text == text[::-1]:
#     print("Палиндром")
# else:
#     # видимо забыли
#     print('Не палиндром')

n = 5

# Прямоугольник
# print("Прямоугольник:")
# for i in range(n):
#     print("*" * n)
#
# # Треугольник
# print("\nТреугольник:")
# for i in range(1, n + 1):
#     print("*" * i)
#
# # Ёлочка
# print("\nЁлочка:")
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))
#
# # Ромб
# print("\nРомб:")
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))


# import random
# print('Игра «Быки и коровы»')
# print('Пробуй угадать число мое 1000-9999')
# compN = random.randint(1000, 9999)
#
#
#
# def countCow(num, compNum):
#     bulls = countBull(num, compNum)
#
#     num_list = list(str(num))
#     comp_list = list(str(compNum))
#
#     for i in range(3, -1, -1):
#         if num_list[i] == comp_list[i]:
#             num_list.pop(i)
#             comp_list.pop(i)
#
#     cows = 0
#     for digit in num_list:
#         if digit in comp_list:
#             cows += 1
#             comp_list.remove(digit)
#
#     return cows
#
# def countBull(num, compNum):
#     c = 0
#     for i in range(len(str(num))):
#         if str(num)[i] == str(compNum)[i]:
#             c += 1
#     return c
#
#
# while True:
#     while True:
#         try:
#             num = int(input('Введите число:'))
#             if len(str(num)) == 4:
#                 break
#             else:
#                 print('число нужно из диапазона 1000-9999')
#         except:
#             print('Что-то не то вы ввели')
#
#     if num == compN:
#         print('красава, угадал, число было: ' + str(compN))
#         break
#     else:
#         print('быков(цифра на своём месте): ' + str(countBull(num, compN)))
#         print('Коров(цифра есть, но не на своём месте): ' + str(countCow(num, compN)))


# def getFact(n):
#     factorial = 1
#     for i in range(1, n+1):
#         factorial *= i
#     return factorial
#
#
# accuracy = float(input('Введите точность (например, 0.0001): '))
# e = 1
# i = 1
# while True:
#     nw = 1 / getFact(i)
#     if nw < accuracy:
#         break
#     e += nw
#     i += 1
#
# print(e)


# lst = list(map(int,input('Введите числа через пробел: ').split(' ')))
#
# for _ in range(len(lst)):
#     for i in range(len(lst) - 1):
#         if lst[i] > lst[i+1]:
#             lst[i + 1], lst[i] = lst[i], lst[i + 1]
# print(lst)

# print('Перевод числа из десятичной системы в двоичную и обратно')
# n = int(input('Какое число желаете перевести в 2 сс: '))
#
# def from10to2(n):
#     res = ''
#     if n == 0:
#         return '0'
#     while n > 0:
#         res += str(n % 2)
#         n //= 2
#     return res[::-1]
#
# def from2to10(n):
#     res = 0
#     power = 0
#     for digit in reversed(str(n)):
#         if digit == '1':
#             res += 2 ** power
#         power += 1
#     return res
#
# print(from10to2(n), from2to10(int(from10to2(n))))


# print(f"{'x':^5} | {'y':^5}")
# print('-'*14)
# for x in range(-5, 6):
#     y = str(x**2 - 2*x + 1)
#     print(f"{x:^5} | {y:^5}")

# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# n = 20
#
#
# def getMidl(lst, target):
#     if not lst:
#         return -1
#
#     midl = len(lst) // 2
#
#     if lst[midl] == target:
#         return target
#     elif target < lst[midl]:
#         return getMidl(lst[:midl], target)
#     else:
#         return getMidl(lst[midl + 1:], target)
#
#
# print(getMidl(lst, n))
