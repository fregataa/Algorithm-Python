import sys
sys.setrecursionlimit(10**8)    # IMPORTANT !!
tc = int(input())
cmap = []
group = []
gidx = 0

def find(posX: int, posY: int, idx: int):
    if cmap[posY][posX]:
        cmap[posY][posX] = 0
        if len(group) > idx:
            group[idx] += 1
        else:
            group.append(1)
        if posX > 0:
            find(posX-1, posY, idx)
        if posX < len(cmap[posY]) - 1:
            find(posX+1, posY, idx)
        if posY > 0:
            find(posX, posY-1, idx)
        if posY < len(cmap) - 1:
            find(posX, posY+1, idx)

for t in range(tc):
    m, n, k = map(int, sys.stdin.readline().split())
    cmap = [[0 for i in range(m)] for j in range(n)]
    group = [1]
    gidx = 0
    for k0 in range(k):
        a, b = map(int, sys.stdin.readline().split())
        cmap[b][a] = 1
    for i in range(n):
        for j in range(m):
            if cmap[i][j]:
                find(j, i, gidx)
                gidx += 1
    print(len(group))


# import sys
# tc = int(input())

# for t in range(tc):
#     m, n, k = map(int, sys.stdin.readline().split())
#     a, b = map(int, sys.stdin.readline().split())
#     cmap = [[[a, b]]]
#     answer = 1
#     for k0 in range(k-1):
#         a, b = map(int, sys.stdin.readline().split())
#         flag = True
#         for g in cmap:
#             for x, y in g:
#                 if abs(x-a) + abs(y-b) < 2:
#                     g.append([a,b])
#                     if flag:
#                         flag = False
#                     else:
#                         answer -= 1
#                     break
#         if flag:
#             cmap.append([[a,b]])
#             answer += 1
            
#     print(answer)

