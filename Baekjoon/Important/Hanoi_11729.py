
def hanoi(a, b, c, count):
    if count < 1:
        return
    hanoi(a, c, b, count-1)
    print(a, b)
    hanoi(c, b, a, count-1)

k = int(input())
print(2**k - 1)
hanoi(1, 3, 2, k)

# def change(a: int, b: int, t: list):
#     l = []
#     for i in t:
#         x, y = i
#         if i[0] == a:
#             x = b
#         if i[0] == b:
#             x = a
#         if i[1] == a:
#             y = b
#         if i[1] == b:
#             y = a
#         l.append([x, y])
#     return l

# def hanoi(f: list, count: int):
#     if count < 2:
#         return f
#     else:
#         n = change(2,3,f)
#         n.append([1, 3])
#         n += change(1,2,f)
#         return hanoi(n, count-1)

# k = int(input())
# answer = hanoi([[1, 3]], k)
# print(len(answer))
# for i in answer:
#     print(i[0], i[1])
