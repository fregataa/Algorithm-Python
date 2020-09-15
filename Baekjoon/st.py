from collections import Counter

# a = [1,2,3,4]
# t = sorted(Counter(map(int, input().split())).items(), reverse=True)
# print(t)
a= [10,10,20,17,15,5,5]
b= Counter(map(int, a))
print(b.items())