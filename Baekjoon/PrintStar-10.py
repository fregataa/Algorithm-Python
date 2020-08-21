n = int(input())

# def printStar(num: int, star: bool):
#     if num > 1:
#         if star:
#             a = ''.join([x+y+z for x,y,z in zip(printStar(num//3, True).split('\n'), printStar(num//3, True).split('\n'), printStar(num//3, True).split('\n'))])
#             b = ''.join([x+y+z for x,y,z in zip(printStar(num//3, True).split('\n'), printStar(num//3, False).split('\n'), printStar(num//3, True).split('\n'))])
#             return a + '\n' + b + '\n' + a
#         else:
#             f = ''.join([x+y+z for x,y,z in zip(printStar(num//3, False).split('\n'), printStar(num//3, False).split('\n'), printStar(num//3, False).split('\n'))])
#             return f + '\n' + f + '\n' + f
#     else:
#         if star:
#             return '*'
#         else:
#             return ' '

# print(printStar(n, True))


# def printer(count: int, top: bool):
#     if count == n:
#         return '***' * (n//3)
#     return '***'

# def top(count: int):
#     if count < n:
#         return top(count).split()[0] * 3
#     else:
#         return '*'

# def medium(count: int):
#     if count < n:
#         return top(count).split()[0] + '{0}'.format(' '*count) + top(count).split()[0]
#     return '{0}'

# def top(count: int):
#     return '*'*3

# def medium(count: int):
#     return '{0}{1}{0}'.format(top(count), ' '*count)

# def liner(count: int, star: bool):
#     if star:
#         if count < n:
#             return liner(count*3, True) + '\n' + liner(count*3, False) + '\n' + liner(count*3, True)
#         else:
#             return '*'*n
#     else:
#         if count < n:
#             return liner(count, False) + '\n' + liner(count, False) + '\n' + liner(count, False)
#         else:
#             return '{0}{1}{0}'.format(liner(count, True), ' '*count)

def liner(count: int):
    if count < n:
        line = liner(count*3)
        return line * 4 + (' '*(n//count//3)) + line * 4
    else:
        return '*'


answer = liner(1)
for i in range(n):
    print(answer[i*n:(i+1)*n])