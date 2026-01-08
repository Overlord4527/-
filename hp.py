# def a(n):
#     x = list()
#     for i in range(1, n + 1):
#         if n % i == 0:
#             x.append(i)
#     return x
# n = int(input())
# print(a(n))


# def a(x1, x2, y1, y2):
#     x3 = (x1 + x2) / 2
#     y3 = (y1 + y2) / 2
#     return x3, y3
# x1, x2 = int(input()), int(input())
# y1, y2 = int(input()), int(input())
# print(a(x1,x2, y1,y2))

# def quick_merge(list1, list2):
#     result = []
#     p1 = 0
#     p2 = 0
#     while p1 < len(list1) and p2 < len(list2):
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else:
#             result.append(list2[p2])
#             p2 += 1
#     if p1 < len(list1):
#         result += list1[p1:]
#     else:
#         result += list2[p2:]
#     return result
# print(quick_merge([12,56,53],[56,4574745,43534]))

def blablabla(x):
    if x == str():
        print(x,)