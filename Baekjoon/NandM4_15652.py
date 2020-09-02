n,m = map(int, input().split())

def find(num: list, c: int):
    if len(num) == m:
        print(*num)
        return
    for i in range(c, n+1):
        numc = num[:]
        numc.append(i)
        find(numc, i)

find([], 1)