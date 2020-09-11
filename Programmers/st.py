from collections import Counter, defaultdict
from functools import reduce

nums = [1,2,3]
X = [[1,2],[3,4],[5,6],[7,8],[0,0],[9,9]]
y = [1,0,1,0,0,1]

print(X[y==1, 0], X[y==0, 1])
# print(reduce(lambda x,y: x*y, nums))

phone_book = ['1922', '197674223', '191']
l= [['yellow_hat', 'headgear'], ['blue_glasses', 'eyewear'], ['blue_hat', 'headgear']]
# print(Counter(a.keys()) + Counter(b.keys()))
# print(phone_book[-2])
# print(a[0-1])
