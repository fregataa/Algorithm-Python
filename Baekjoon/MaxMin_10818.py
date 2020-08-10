import sys
n = int(input())
numList = list(map(int, sys.stdin.readline().split()))

print(min(numList), max(numList))