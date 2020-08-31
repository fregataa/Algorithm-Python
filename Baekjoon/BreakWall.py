import sys
from collections import deque
s = sys.stdin
n, m = map(int, s.readline().split())
q=deque()
q.append([1,0,0])
graph = [[-1] *(m+2)]
for _ in range(n):
    graph.append([-1] + list(s.readline().rstrip('\n')) + [-1])
graph.append([-1] * (m+2))
visited = [[[-1]*m for _ in range(n)] for _ in range(2)]
visited[1][0][0] = 0

def bfs():
    while q:
        wall, x,y = q.popleft()
        v = visited[wall][x][y]
        if (x,y) == (n-1,m-1):
            return v+1
        for a,b in ((x+1,y), (x,y+1), (x,y-1), (x-1,y)):
            if graph[a+1][b+1] == -1 or visited[wall][a][b] != -1:
                continue
            w = wall
            if graph[a+1][b+1] == '1':
                if wall:
                    w=0
                else:
                    continue
            visited[w][a][b] = v+1
            q.append([w,a,b])
    return -1
        
print(bfs())



# for i in graph:
#     print(i)

for i in visited:
    print()
    for j in i:
        print(j)



# graph = [list(s.readline().rstrip('\n')) for _ in range(n)]
# visit = [[-1]*(m+2)]
# visit.append(([-1]+[0]*m+[-1])*n)
# visit.append([-1]*(m+2))
# print(visit)
# def bfs():
#     count = 0
#     while q:
#         y,x,wall = q.popleft()
#         if (y,x) == (n,m):
#             return graph[y][x]+1
#         for a,b in ((y+1,x), (y-1,x), (y,x+1), (y,x-1)):
#             if graph[a][b] != -1:
#                 if graph[a][b] == '1':
#                     if wall:    
#                         q.append([a,b,0])   
#                     else:
#                         continue
#                 else:
#                     q.append([a,b,wall])
#                 graph[a][b] = int(graph[y][x]) + 1

#         if wall:
#             graph[y][x] = -1

        
#         count += 1
#         if count > 600:
#             print()
#             for i in graph:
#                 print(i)
#             print()
#         if count > 700:
#             break
#     return -1 
# print(bfs())

# for i in graph:
#     print(i)

# for i in visit:
#     print(i)


# import sys
# from collections import deque
# s = sys.stdin
# n, m = map(int, s.readline().split())
# q=deque()
# q.append([1,1,1])
# graph = [[-1] *(m+2)]
# for _ in range(n):
#     graph.append([-1] + list(s.readline().rstrip('\n')) + [-1])
# graph.append([-1] * (m+2))
# visit = [[0]*m]*n

# def bfs():
#     while q:
#         y,x,wall = q.popleft()
#         if (y,x) == (n,m):
#             return
#         for a,b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
#             pass
