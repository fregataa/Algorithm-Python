from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
max = 0
for i in list(combinations(cards,3)):
    a = sum(i)
    if a > max and a <= m:
        max = a
print(max)    

# for i, iv in enumerate(cards):
#     for j, jv in enumerate(cards):
#         if j <= i:
#             continue
#         for k, kv in enumerate(cards):
#             if k <= j:
#                 continue
#             if iv+jv+kv > max and iv+jv+kv <= m:
#                 max = iv+jv+kv

# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             if cards[i] + cards[j] + cards[k] > max and cards[i] + cards[j] + cards[k] <= m:
#                 max = cards[i] + cards[j] + cards[k]
# print(max)

