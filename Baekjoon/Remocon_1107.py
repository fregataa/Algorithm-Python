# n = input().rstrip('\n')
# m = int(input())
# l = list(map(int, input().split()))
# nl = [x for x in range(10) if x not in l]*2
# answer = 0
# def chker(idx: int, cnt: int, plus: bool):
#     if idx + cnt < 0 or idx + cnt > 9:
#         if plus:
#             return 10
#         else:
#             return -10  
#     if idx + cnt in nl:
#         return cnt
#     if plus:
#         return chker(idx, cnt+1, plus)
#     else:
#         return chker(idx, cnt-1, plus)

# if n != '100':
#     num = ['', '']
#     if len(l) == 10:
#         num = [[1,0,0], [1,0,0]]
#     else:
#         answer = len(n)
#         flag = False
#         for c in n:
#             ic = int(c)
#             if ic in l:
#                 if flag:
#                     num[0]+= str(9 + chker(9, 0, False))
#                     num[1]+= str(chker(0, 0, True))
#                 else:
#                     left = chker(ic, 0, False)
#                     right = chker(ic, 0, True)
#                     if left + right > 0:
#                         num[0]+= str(ic+left)
#                         num[1]+= str(ic+left)
#                     elif left + right < 0:
#                         num[0]+= str(ic+right)
#                         num[1]+= str(ic+right)
#                     else:
#                         flag = True
#                         num[0]+= str(ic+left)
#                         num[1]+= str(ic+right)
#             else:
#                 num[0]+= str(ic)
#                 num[1]+= str(ic)
#     answer += min(abs(int(n) - int(num[0])), abs(int(n) - int(num[1])))
# print(answer)

# n = input().rstrip('\n')
# m = int(input())
# l = list(map(int, input().split()))
# nl = [x for x in range(10) if x not in l]
# answer = 0
# count = abs(int(n) - 100)
# if n != '100':
#     if len(l) == 10:
#         num = ['100', '100']
#     else:
#         num = ['', '']
#         for i, c in enumerate(n):
#             flag = False
#             ic = int(c)
#             if ic in l:
#                 for nv in range(10):
#                     if ic + nv in nl:
#                         flag = True
#                         num[0] += str(ic+nv)
#                         for _ in range(i+1, len(n)):
#                             num[0] += str(nl[0])
#                     if ic - nv in nl:
#                         flag = True
#                         num[1] += str(ic-nv)
#                         for _ in range(i+1, len(n)):
#                             num[1] += str(nl[len(nl)-1])
#                     if flag:
#                         break
#             if flag:
#                 break
#             else:
#                 num[0] += c
#                 num[1] += c
#         answer = len(n)
#     if num[0] == '':
#         answer += abs(int(n)-int(num[1]))
#     elif num[1] == '':
#         answer += abs(int(n)-int(num[0]))
#     else:
#         answer += min(abs(int(n)-int(num[0])), abs(int(n)-int(num[1])))

# print(min(answer, count))




n = input().rstrip('\n')
m = int(input())
l = []
if m != 0:
    l = input().split()
answer = abs(int(n) - 100)

if len(l) != 10:
    count = [0,0]
    while 1:
        a=0
        for c in count:
            num = int(n) + c
            if num < 0:
                continue
            a=0
            for cn in str(num):
                a+=l.count(cn)
            if a==0:
                print(min(answer, len(str(num)) + abs(c)))
                break
        if a==0:
            break
        count[0] -= 1
        count[1] += 1
else:
    print(answer)


#     count = 0
#     while 1:
#         if int(n)+count <= 500000:
#             flag = True
#             n0 = str(int(n)+count)
#             for nv in n0:
#                 if nv in l:
#                     flag = False
#             if flag: 
#                 count += len(n0)
#                 break
#         if int(n)-count >= 0:
#             flag = True
#             n1 = str(int(n)-count)
#             for nv in n1:
#                 if nv in l:
#                     flag = False
#             if flag: 
#                 count += len(n1)
#                 break
#         count += 1

#     print(min(answer, count))
# else:
#     print(answer)