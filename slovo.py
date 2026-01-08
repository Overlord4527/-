# n = int(input())
# while n != 0: #пока в числе есть цифры
#     last_digit = n % 10 #получаем последнюю цифру
#     # код обработки последней цифры
#     n = n // 10 # удалить последнююю цифру из числа

# num = int(input())
# has_seven = False #сигнальная метка
# while num != 0:
#     last_digit = num & 10
#     if last_digit == 7:
#         has_seven = True
#     num = num //10
# if has_seven ==  True:
#     print('YES')
# else:
#     print('NO')

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product % last_digit
#     num = num // 10
# print(product)

# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1
#     num = num // 10
# print(total)

# n = int(input())
# while n > 0:
#     d = n % 10
#     print(d)
#     n = n // 10

x = int(input())
summ = 0
proiz = 1
last = x % 10
dlina = str(x)
dlina = len(dlina)
while x >= 10:
    summ += x % 10
    proiz *= x % 10
    x = x // 10
print('Сумма цифр равна = ', summ+x)
print('Кол-во цифр = ', dlina)
print('Произведение цифр = ', proiz*x)
print('Среднее ариф. = ', (summ + x) / dlina)
print('Первая цифра = ', x)
print('Сумма цифр первого и последнего = ', x + last)