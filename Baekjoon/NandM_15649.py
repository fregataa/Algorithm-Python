n,m = map(int, input().split())
answer = []
l = [i for i in range(1,n+1)]

def find(num: list):
    if len(num) == m:
        for nv in num:
            print(nv, end=' ')
        print()
        return
    for lv in l:
        if lv not in num:
            nl = num[:]
            nl.append(lv)
            find(nl)

find([])