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
q=[n]
fin = False
v = [1]*200000

def find(q: list):
    t=0
    if q[0]==k:
        return t
    while 1:
        l = list(set(q))
        nl = []
        for lv in l:
            for mv in [-1,1,lv]:
                if 0<=mv+lv<200000 and v[mv+lv]:
                    if mv + lv == k:
                        return t+1
                    nl.append(mv+lv)
                    v[mv+lv] = 0
        t += 1
        q = nl
    
print(find(q))