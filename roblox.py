# i = 0
# while i < 10:
#     print('Привет')
#     i += 1

# num = int(input())
# while num != -1:
#     print('Квадрат вашего чесла равен', num * num)
#     num = int(input())

# text = int(input())
# total = 0
# while text != 'stop':
#     num = int(input())
#     total += num
#     text = input()
# print('сумма чисел равна', total)

# i = 0
# total = 0
# while i < 10:
#     total += i

# i = -1
# while i > 0:
#     print('Hello world')

# count = 1
# while count < 10:
#     print('python awesome!')
#     count += 1

# i = 5
# while i <= ...:
#     print('Python awesome!')
#     i += 1

# a = input()
# t = str()
# while a != 'STOP':
#     t += '\n' + a
#     a = input()
# print(t)

# a = input()
# t = str()
# while a != 'STOP' and a != 'stop':
#     t += '\n' + a
#     a = input()
# print(t)

# a = input()
# t = 0
# while a != 'стоп' and a != 'хватит' and a != 'достаточно':
#     a = input()
#     t += 1
# print(t)

#
# x = 0
# temp = 0
# while x >= 0:
#     x = int(input())
#     temp += x
# print(temp)

monet = 0
x = int(input())
while x != 0:
    if x >= 25:
        monet += x // 25
        x %= 25
    elif x >= 10:
        monet += x // 10
        x %= 10
    elif x >= 5:
        monet += x // 5
        x %= 5
    elif x >= 1:
        monet += x // 1
        x %= 1
print(monet)