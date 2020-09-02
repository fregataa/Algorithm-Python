n,m = map(int, input().split())

def find(num: list):
    if len(num) == m:
        print(*num)
        return
    for i in range(1, n+1):
        numc = num[:]
        numc.append(i)
        find(numc)   
        
find([])



# from itertools import product
# N,M = map(int,input().split())

# prod = list(map(' '.join, product([str(i+1) for i in range(N)],repeat = M)))
# for i in prod:
#     print(i)