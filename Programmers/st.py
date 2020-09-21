from collections import Counter, defaultdict
from functools import reduce

from collections import deque

import heapq as hq
# a = deque()
# a.append(1)

# print(a)

a = ["abc","abr","hhf","qsd"]
b = sorted(a, key = lambda x: tuple([x[i] for i in range(1:)]))
print(b)