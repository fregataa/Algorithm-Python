n = int(input())
n = n-1
for i in range(n*2 + 1):
    print("{0}".format('*'* (n-abs(n-i)+1) ))