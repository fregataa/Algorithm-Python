import sys, heapq as hq

n, c = map(int, input().split())
h = []
for _ in range(n):
    hq.heappush(h, int(sys.stdin.readline()))

l, r = 1, h[-1]

while l<=r:
    mid = (l+r) >> 1
    modem = c - 1
    house = h[:]
    point = hq.heappop(house)
    while house:
        neigbor = hq.heappop(house)
        if neigbor - point >= mid:
            point = neigbor
            modem -= 1
        if modem == 0:
            break
    if modem > 0:
        r = mid-1
    else:
        l = mid+1

print(r)