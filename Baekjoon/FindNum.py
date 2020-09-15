n = int(input())
a = list(map(int, input().split()))
m = int(input())
findThis = list(map(int, input().split()))

a.sort()
def binSrch(num: int):
    mini = 0
    maxi = len(a)
    if num < a[mini] or num > a[maxi-1]:
        return 0
    while 1:
        mid = (mini + maxi) // 2
        if num == a[mid]:
            return 1
        elif num > a[mid]:
            if mid == mini:
                return 0
            mini = mid
        else:
            maxi = mid
        

for i in range(m):
    print(binSrch(findThis[i]))
    