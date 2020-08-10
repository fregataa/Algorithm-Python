import sys

for line in sys.stdin:
    print(int(line.split()[0]) + int(line.split()[1]))


#   This code is also possible
# try:
#     a, b = map(int, input().split())
#     print(a+b)
# except:
#     exit()

