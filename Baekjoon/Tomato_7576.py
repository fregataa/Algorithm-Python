import sys
from collections import deque
s = sys.stdin
m,n = map(int, s.readline().split())
box = []
mday = 0
q = deque()

for i in range(n):
    line = list(map(int, s.readline().split()))
    for j in range(m):
        if line[j] == 1:
            q.append([j,i,0])
    box.append(line)

while q:
    posx, posy, day = q.popleft()
    if 0 <= posx < m and 0 <= posy < n and box[posy][posx] != -1:
        box[posy][posx] = -1
        if day > mday:
            mday = day
        q.append([posx-1,posy, day+1])
        q.append([posx+1,posy, day+1])
        q.append([posx,posy-1, day+1])
        q.append([posx,posy+1, day+1])

for i in box:
    if i.count(0): 
        mday = -1
        break

print(mday)
