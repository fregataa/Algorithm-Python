from collections import deque
n,k = map(int, input().split())
t = 0
q=deque()
q.append([n,t])

while n != k:
    n, t = q.popleft()
    m = [-1, 1, n]      
    for i in m:
        if 0<=i+n<=100000:
            q.append([i+n, t+1])
    
print(t)