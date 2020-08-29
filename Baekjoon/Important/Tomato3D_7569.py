# import sys
# s = sys.stdin
# m,n,h = map(int, s.readline().split())
# size = m*n*h
# # movy = [-n, 0, -1, 0, 1, n]
# # movx = movy[1:5]
# # print(movx)
# mov = [-(m*n), -m, -1, 1, m, m*n]
# # mov = []
# box = [0 for _ in range(m*n*h)]
# day = -1
# q = []
# for i in range(n*h):
#     line = s.readline().split()
#     for j in range(m):
#         if line[j] == '1':
#             box[i*m+j] = 1
#             q.append([j, i])
#         elif line[j] == '-1':
#             box[i*m+j] = -1

# while q:
#     l = []
#     for i in q:
#         x, y = i
#         pos = m*y + x
#         box[pos] = -1
#         for p in mov:
#             np = pos + p
#             if ((p == 1 or p == -1) and (np)//m != y) or np < 0 or np >= size:
#                 continue
#             if box[np] == 0:
#                 l.append([np%m, np//m])
#     q = l[:]
#     day += 1
    
# if box.count(0):
#     day = -1
# print(day)


import sys
from collections import deque
s = sys.stdin
m,n,h = map(int, s.readline().split())
movx = (-1, 1, 0, 0, 0, 0) 
movy = (0, 0, -1, 1, 0, 0)
movz = (0, 0, 0, 0, -1, 1)

box = [[list(map(int, s.readline().split())) for _ in range(n)] for _ in range(h)]
mday = 0
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append([i, j, k])  # page, y, x
    
while q:
    z, y, x = q.popleft()
    d = box[z][y][x]
    if d > mday:
        mday = d
    for i in range(6):
        zp, yp, xp = movz[i],movy[i],movx[i]
        if 0 <= z+zp < h and 0 <= x+xp < m and 0 <= y+yp < n and box[z+zp][y+yp][x+xp] == 0:
            q.append([z+zp, y+yp, x+xp])
            box[z+zp][y+yp][x+xp] = d + 1
    box[z][y][x] = -1
    

for i in box:
    for j in i:
        if j.count(0):
            mday = 0
            break
print(mday-1)
            