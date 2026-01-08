# result = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         break
#     result += num
# print(result)

# num = int(input())
# flag = True
# for i in range(2, num):
#     if num % i == 0:
#         flag = False
#         break
# if flag == True:
#     print('число простое')
# else:
#     print('число составное')

# n = int(input())
# flag = False
# while n != 0:
#     last_digit = n % 10
#     if last_digit == 7:
#         flag = True
#     n //= 10
# if flag == True:
#     print('число', n, 'содержит цифру 7')
# else:
#     print('число', n, 'не содержит цифру 7')

# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break

# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)

# mult = 1
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     if i % 9 == 0:
#         break
#     mult *= i
# print(mult)

# a = int(input())
# b = int(input())
# z = 0
# while a > 0 or b > 0:
#     z += 1
#     if a % z == 0 and b % z == 0:
#         break
# print(z)

# x = int(input())
# y = int(input())
# z = 1
# while x > 0 and y > 0:
#     z += 1
#     if z % x == 0 and z % y == 0:
#         break
# print(z)

# x = int(input())
# y = int(input())
# z = 1
# while x > 0 and y > 0:
#     z += 1
#     if x % z == 0 and y % z == 0:
#         break
# print(z)
#
# x = int(input())
# for i in range(1, x+1):
#     if 5 <= i <= 9:
#         continue
#     if 17 <= i <= 37:
#         continue
#     if 78 <= i <= 87:
#         continue
# print(i)

# a = 1
# for i in range(1, 1000):
#     if i % 2 == 1:
#         a = a + 1
# print(a)

# n = input()
# a = 0
# for i in range(n):
#     a = a * i
# print(a)

# n = int(input())
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(factorial)

# a = -2
# b = 1
# c = 0
# while a != -1:
#     a = input()
#     if a >= 7:
#         b = b + a
#     c = c + 1
# print(c / b)

a = int(input())
b = 0
c = 0
while a != -1:
    if a > 7:
        b = b + a
        c = c + 1
    a = int(input())
print(c / b)




