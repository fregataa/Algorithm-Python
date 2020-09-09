# n = int(input())


# a = -2
# print(a/3)
# import re
# phone_book = ['19', '97674223', '195524421']
# answer = True
# p = re.compile(phone_book[0]+'2*')

# print(p.match(phone_book[0]))

from collections import Counter
from functools import reduce

nums = [1,2,3]
# print(reduce(lambda x,y: x*y, nums))

phone_book = ['1922', '197674223', '191']
l= [['yellow_hat', 'headgear'], ['blue_glasses', 'eyewear'], ['blue_hat', 'headgear']]
p = list(map(lambda y, x: x+y, phone_book, l[0]))
print(p)
# print(reduce(lambda x,y: x+y, l))
a=Counter([i for a, i in l])
b = Counter([a for a, i in l])
# print(Counter(a.keys()) + Counter(b.keys()))
# print(phone_book[-2])
# print(a[0-1])
