from collections import Counter
n = int(input())
cards = Counter(list(map(int, input().split())))
m = int(input())
guess = list(map(int, input().split()))

for g in guess:
    print(cards[g])