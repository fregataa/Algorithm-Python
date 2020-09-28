from collections import Counter

import heapq as hq

a = []
b = [4,6,8,3,2,1,9]

for bn in b:
    hq.heappush(a, bn)

while a:
    print(hq.heappop(a))

print(a)