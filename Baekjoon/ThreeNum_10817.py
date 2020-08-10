numList = list(map(int, input().split()))

numList.remove(max(numList))
numList.remove(min(numList))

print(numList[0])

# a,b,c = map(int, input().split())
# if a > b:
#     if b > c:
#         print(b)
#     else:
#         if a < c:
#             print(a)
#         else:
#             print(c)
# else:
#     if b > c:
#         if a > c:
#             print(a)
#         else:
#             print(c)
#     else:
#         print(b)