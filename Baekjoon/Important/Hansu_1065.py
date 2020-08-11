n = int(input())

allNum = [x+1 for x in range(n)]

def numChecker(num: str, index: int):
    if index >= len(num)-1:
        return
    
    if int(num[index])*2 != int(num[index+1]) + int(num[index-1]) and int(num) in allNum:
        allNum.remove(int(num))
    else:
        numChecker(num, index+1)

for i in range(1, n+1):
    numChecker(str(i), 1)

print(len(allNum))



# hansu = []
# count = 0

# def appender(num: str, plus: int):
#     global count
#     lastNum = int(num[len(num)-1])
#     if lastNum + plus > 9 or lastNum + plus < 0:
#         return
#     newNum = int(num + str(lastNum + plus))
#     if newNum <= n:
#         hansu.append(newNum)
#         count += 1
#         appender(str(newNum), plus)

# for i in range(1, 10):
#     if i <= n:
#         hansu.append(i)
#         count += 1
#     for j in range(-9, 10):
#         appender(str(i), j)

# print(count)



# for i in range(1, 10):
#     if i > n:
#         break
#     hansu.append(i)
#     count += 1
#     for j in range(-9, 10):
#         num = [str(i)]
#         index = i
#         while 1:
#             index += j
#             if index > 9 or index < 0 or n < int(''.join(num) + str(index)):
#                 break
#             num.append(str(index))
#             hansu.append(int(''.join(num)))
#             count += 1
        
#         num = [str(i)]
#         index = i

# print(count)