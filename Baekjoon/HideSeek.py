# from collections import deque
# n,k = map(int, input().split())
# t = 0
# q=deque()
# q.append([n,t])

# while n != k:
#     n, t = q.popleft()
#     m = [-1, 1, n]      
#     for i in m:
#         if 0<=i+n<=100000:
#             q.append([i+n, t+1])
    
# print(t)

n,k = map(int, input().split())
t=0
q=[n]
fin = False

while 1:
    l = list(set(q))
    q = []
    for lv in l:
        m = [-1,1,lv]
        for mv in m:
            if 0<=mv+lv<140000:
                q.append(mv+lv)
                if mv + lv == k:
                    fin = True
        if fin:
            break
    t += 1
    if fin:
        break
print(t)