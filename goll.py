# for minutes in range(60):
#     for seconds in range(60):
#         print(minutes, ':', seconds)

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)

# for i in range(3):
#     for j in range(3):
#         print(i, j)

# for i in range(3):
#     for j in range(3):
#         if i == j:
#             break
#         print(i, j)

# for i in range(3):
#     for j in range(3):
#         if i == j:
#             continue
#         print(i, j)

# for i in range(1, 4):
#     for j in range(3, 6):
#         print(i, j)

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# n = int(input())
# if n <= 0:
#     print('не больше нуля')
# for i in range(n):
#     if n >= 10:
#         print('меньше нуля')
#         break
#     for b in range(3):
#         print(n, end=" ")
#     print(sep=" ")

# n = int(input())
# if n <= 9:
#     for a in range(n):
#         for i in range(1, 5):
#             print(a + 1, end=' ')
#         print()
# else:
#     print('err')

# n = int(input())
# if n <= 9:
#     for i in range(1, 10):
#         for j in range(1, 10):
#             print(i, '+', j, '=', i + j)
#         print()
# else:
#     print('err')

# a = int(input())
# for i in range(1, a+1):
#     for j in range(i):
#         print(i , end='')
#     print()

# total = 0
# for x in range(1, 65):
#     for y in range(1, 60):
#         if 12 * x + 13 * y == 777:
#             total += 1
#             print('x =', x, 'y =', y)
# print('общее количество натуральных решений =', total)

# x = int(input())
# y = int(input())
# for i in range(y):
#     for j in range(x):
#         print('⭐', end='')
#     print()

# n = int(input())
# for i in range(n):
#     print(' ⭐ '* (n - i))

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i * j : 4}', end= '')
    print(sep= '\n')



