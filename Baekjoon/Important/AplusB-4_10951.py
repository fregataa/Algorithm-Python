import sys

for line in sys.stdin:
    print(int(line.split()[0]) + int(line.split()[1]))

# if we use sys.stdin.readline() or input(), 
# this for loop finish after 1 loop. 
# readline() include '\n' at the last. we can check it by split()

#   This code is also possible
# try:
#     a, b = map(int, input().split())
#     print(a+b)
# except:
#     exit()

