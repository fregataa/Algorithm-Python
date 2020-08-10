n = int(input())

for i in range(n):
    line = list(input())
    aggSco = 0
    currentSco = 0
    for j in line:
        if j == 'O':
            currentSco += 1
            aggSco += currentSco
        else:
            currentSco = 0
    print(aggSco)

# if you use input().splice() without any space, 
# it will return one big string index in a list.
# like this ['input']
# but list(input()) return like ['i', 'n', 'p', ...]

# import sys

# line = sys.stdin.readline()
# line = list(line)
# print(line, len(line))