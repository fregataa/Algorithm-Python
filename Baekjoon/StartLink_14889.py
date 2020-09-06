from itertools import combinations as c, permutations as p

n = int(input())
node = [list(map(int, input().split())) for _ in range(n)]
combs = list(c(range(n), n//2))
answer = 5000000
for i in range(len(combs)//2):
    start, link = list(p(combs[i], 2)), list(p(combs[-1-i], 2))
    s, l = 0,0
    for x,y in start:
        s += node[x][y]
    for x,y in link:
        l += node[x][y]
    answer = min(answer, abs(s-l))
    if not answer:
        break
print(answer)

# chk = [True for _ in range(n)]
# alrdy = []
# r = n//2 - 1
# count = n//2
# for i in range(r+2,n):
#     count *= i
# answer = 200
# def find(c: int):
#     if c > r:
#         global answer
#         global count
#         count -= 1
#         sn = 0
#         ln = 0
#         for i in range(n):
#             if chk[i]:
#                 for j in range(i,n):
#                     if chk[j]:
#                         sn += node[i][j] + node[j][i]
#             else:
#                 for j in range(i,n):
#                     if chk[j] == False:
#                         ln += node[i][j] + node[j][i]
#         if sn == ln:
#             print(0)
#             exit()
#         if abs(sn-ln) < answer:
#             answer = abs(sn-ln)
#         if count == 0:
#             print(answer)
#             exit()
#         return
#     for i in range(n):
#         if chk[i]:
#             chk[i] = False
#             find(c+1)
#             chk[i] = True

# find(0) 