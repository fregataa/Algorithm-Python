n,m = map(int, input().split())

def find(num: list, c: int):
    if len(num) == m:
        for nv in num:
            print(nv, end=' ')
        print()
        return
    if len(num) < m:
        nl = num[:]
        nl.append(c)
        find(nl, c+1)
    if n-c >= m-len(num):
        find(num, c+1)
    
find([], 1)