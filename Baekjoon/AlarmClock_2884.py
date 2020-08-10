a,b = map(int, input().split())

t = a*60 + b - 45
print(t//60%24, t%60)

# if b < 45:
#     if a == 0:
#         a = 23
#     else:
#         a -= 1
#     b += 15
# else:
#     b -= 45

# print(a, b)

