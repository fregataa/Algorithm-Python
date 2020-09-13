from collections import Counter, defaultdict
from functools import reduce

# a = [[1], [2], [6]]
# b = a + [[4], [5]]
# c = b + [[6], [7]]

a = [{2,1}, {1,3}, {5,4}]
b = {1,2}

if b in a:
    print('b in a')
else:
    print('npoe')