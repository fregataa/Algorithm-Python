import sys
tc = int(input())
while tc > 0:
    repeat, string = sys.stdin.readline().split()
    for c in string:
        print(c*int(repeat), end='')
    print('')
    tc -= 1