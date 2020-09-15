k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

maxNum = max(lines)
minv = 1
maxv = maxNum*2 + 1
while 1:
    newLine = 0
    mid = (minv + maxv)//2
    for line in lines:
        newLine += line//mid
    # newLine = sum(list(map(lambda x: x//mid, lines)))
    if newLine >= n:
        if mid == minv:
            print(mid)
            break
        minv = mid
    else:
        maxv = mid