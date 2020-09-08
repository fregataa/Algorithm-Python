clothes = [['yellow_hat', 'headgear'], ['blue_glasses', 'eyewear'], ['blue_hat', 'headgear']]

# item = {}

# for x, i in clothes:
#     if i in item:
#         item[i] += 1
#     else:
#         item[i] = 1

# n=1
# for i in item:
#     n *= item[i]+1

# answer = n-1

from functools import reduce
from collections import Counter

answer = reduce(lambda x,y: x*y, [a+1 for a in Counter([item for n, item in clothes]).values()]) - 1
print(answer)
