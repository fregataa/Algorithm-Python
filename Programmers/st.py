from collections import Counter, defaultdict, deque
from functools import reduce

import heapq as hq
# a = deque()
# a.append(1)

# print(a)

# a = ["abc","abr","hhf","qsd"]
# b = sorted(a, key = lambda x: tuple([x[i] for i in range(1:)]))
# print(b)

s = 'abcd12345'
# print(s[0:len(s)+1])

# for i in range(0,8,1):
#     print(i)

# w = [1, 5, 6, 10]
# q = deque([w])
# print(q)
# a = q.popleft()
# print(a)

# a= 123.655

# b ='%.2f' % a
# print(b)


# for bn in b:
#     hq.heappush(a, bn)

# while a:
#     print(hq.heappop(a))

# c = list(map(lambda x: x, zip(a,b)))
# print(c)

l = [[1,2,3], [4,5,6], [7,8,9]]

lr = list(zip(*l[::-1]))

# print(lr)

a = 3.301
# print(a+0.001)

h = 23
m = 59
s = 59.999

t = h*3600 + m*60 + s
print(t)
print(t-0.1)