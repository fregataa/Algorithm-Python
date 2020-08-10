import sys

n, x = map(int, sys.stdin.readline().split())

# numbers = list(map(int, sys.stdin.readline().split()))
numbers = sys.stdin.readline().split()
result = []

for i in numbers:
    if int(i) < x:
        result.append(i)

print(result)