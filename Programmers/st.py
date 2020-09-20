from collections import Counter, defaultdict
from functools import reduce

from collections import deque

import heapq as hq
# a = deque()
# a.append(1)

# print(a)

a = [2,4,1,8,9,3]
# hq.heapify(a)
b = hq.nlargest(1,a)
a.remove(2)
print(a)
