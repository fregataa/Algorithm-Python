import sys
from collections import deque
n, m = map(int, input().split())
q = deque([[0, 0, 1]])
maze = [list(map(int, sys.stdin.readline().rstrip('\n'))) for i in range(n)]
# maze = [[*map(int, input())] for _ in[0]*n]

while 1:
    posy, posx, cost = q.popleft()
    if 0 <= posx < m and 0 <= posy < n and maze[posy][posx]:
        if posy == n-1 and posx == m-1:
            print(cost)
            break
        maze[posy][posx] = 0
        q.append([posy, posx-1, cost+1])
        q.append([posy, posx+1, cost+1])
        q.append([posy-1, posx, cost+1])
        q.append([posy+1, posx, cost+1])

        # if posx > 0 and maze[posy][posx-1]:
        #     q.append([posy, posx-1, cost+1])
        # if posx < m-1 and maze[posy][posx+1]:
        #     q.append([posy, posx+1, cost+1])
        # if posy > 0 and maze[posy-1][posx]:
        #     q.append([posy-1, posx, cost+1])
        # if posy < n-1 and maze[posy+1][posx]:
        #     q.append([posy+1, posx, cost+1])
