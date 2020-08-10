n = int(input())
for i in range(n):
    print("{0}{1}".format( " "*(n - i - 1), "*"*(i + 1) ))