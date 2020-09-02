n,k = map(int, input().split())
r={n: 1}
v=[1]*100001
v[n] = 0

def find(n: int):
    loop = True
    t=0
    route=0
    q=[n]
    while loop:
        l=[]
        vl=[]
        for qv in q:
            for mv in [-1,1,qv]:
                if 0<=qv+mv<100001 and v[qv+mv]:
                    if qv+mv in r:
                        r[qv+mv] += r[qv]
                    else:
                        r[qv+mv] = r[qv]
                        l.append(qv+mv)
                    if qv+mv == k:
                        route = r[qv+mv]
                        loop = False
                    vl.append(qv+mv)
        for vlv in vl:
            v[vlv]=0
        t += 1
        q=l
    print(t)
    print(route)

if n==k:
    print('0\n1')
else:
    find(n)
    